from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    """
    Custom role used by the Pro Legacy RBAC system.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    Granular application permission.

    Examples:
        clients.view
        clients.create
        estimates.send
        contracts.sign
    """

    module = models.CharField(
        max_length=50,
    )

    action = models.CharField(
        max_length=50,
    )

    name = models.CharField(
        max_length=150,
    )

    code = models.CharField(
        max_length=120,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.code


class RolePermission(models.Model):
    """
    Relationship between roles and permissions.
    """

    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )

    permission = models.ForeignKey(
        Permission,
        on_delete=models.CASCADE,
        related_name="role_permissions",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "role",
                    "permission",
                ],
                name="unique_role_permission",
            )
        ]

    def __str__(self):
        return f"{self.role.name} - {self.permission.code}"


class User(AbstractUser):
    """
    Custom application user.

    IMPORTANT:
    This model must exist because:
    AUTH_USER_MODEL = "accounts.User"
    """

    email = models.EmailField(
        unique=True,
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
    )

    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="users",
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        full_name = self.get_full_name().strip()

        if full_name:
            return full_name

        return self.username