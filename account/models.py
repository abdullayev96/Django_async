from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, db_index=True)
    is_premium = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"