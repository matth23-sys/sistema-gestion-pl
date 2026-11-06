from django.core.management.base import BaseCommand

from apps.accounts.models import Permission
from apps.accounts.permissions import PERMISSION_REGISTRY


class Command(BaseCommand):
    help = "Synchronize application permissions."

    def handle(self, *args, **options):

        created_count = 0
        updated_count = 0

        valid_codes = set()

        for module, module_data in PERMISSION_REGISTRY.items():

            permissions = module_data["permissions"]

            for action, permission_name in permissions.items():

                code = f"{module}.{action}"

                valid_codes.add(code)

                permission, created = Permission.objects.update_or_create(
                    code=code,
                    defaults={
                        "module": module,
                        "action": action,
                        "name": permission_name,
                    },
                )

                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                (
                    "Permissions synchronized. "
                    f"Created: {created_count}. "
                    f"Updated: {updated_count}."
                )
            )
        )

        unknown_permissions = Permission.objects.exclude(
            code__in=valid_codes
        )

        if unknown_permissions.exists():

            self.stdout.write(
                self.style.WARNING(
                    "Permissions exist in the database "
                    "that are not present in the registry:"
                )
            )

            for permission in unknown_permissions:
                self.stdout.write(
                    f" - {permission.code}"
                )