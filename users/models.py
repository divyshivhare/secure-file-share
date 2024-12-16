from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    roles = models.CharField(
        max_length=10,
        choices=[('Admin', 'Admin'), ('User', 'User'), ('Guest', 'Guest')],
        default='User',
    )
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Avoid conflict with auth.User
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Avoid conflict with auth.User
        blank=True,
    )
