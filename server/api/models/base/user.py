from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from api.models.base import UserMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_superuser=False, **extra_fields):
        if not email:
            raise ValueError('Username must be set')
        user = self.model(email=email, **extra_fields)
        if is_superuser:
            user.is_superuser = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)
        is_superuser = True
        return self.create_user(email, password, is_superuser, **extra_fields)


class User(AbstractBaseUser, UserMixin, PermissionsMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        app_label = 'api'

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.email

    def name(self):
        return f"{self.first_name} {self.last_name}"
