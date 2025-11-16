from django.db import models
from .managers import CustomUserManager
# Create your models here.

from django.contrib.auth.base_user import AbstractBaseUser

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, unique=True)
    date_of_birth = models.DateField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth", "email"]

    objects = CustomUserManager()
    
    def __str__(self):
        return self.email