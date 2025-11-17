from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_of_birth = models.DateField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email


{
    "first_name": "Amr",
    "last_name" : "Moh",
    "email" : "tester@gmail.com",
    "date_of_birth" : '2025-12-29'
}