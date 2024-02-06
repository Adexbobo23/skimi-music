from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class UserAccount(AbstractUser):
    # Additional fields can be added here if needed
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    # Add related_name arguments
    groups = models.ManyToManyField(Group, related_name='userAccount')
    user_permissions = models.ManyToManyField(Permission, related_name='userAccount_permissions')

