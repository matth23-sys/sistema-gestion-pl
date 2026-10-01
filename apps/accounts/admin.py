from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Permission,
    Role,
    RolePermission,
    User,
)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Pro Legacy Information",
            {
                "fields": (
                    "phone",
                    "role",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Pro Legacy Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "role",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "is_superuser",
        "role",
    )

    search_fields = (
        "username",
        "email",
        "first_name",
        "last_name",
    )


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "is_active",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "module",
        "action",
        "name",
    )

    list_filter = (
        "module",
        "action",
    )

    search_fields = (
        "code",
        "name",
        "module",
        "action",
    )


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):

    list_display = (
        "role",
        "permission",
        "created_at",
    )

    list_filter = (
        "role",
        "permission__module",
    )

    search_fields = (
        "role__name",
        "permission__code",
    )