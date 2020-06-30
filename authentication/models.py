from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager 

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField("Name", max_length=255, blank=True)
    email = models.EmailField("Email", blank=True, unique=True)
    phone = models.CharField("Phone", max_length=17, blank=False, unique=True, primary_key=True)
    dp = models.FileField("Profile Picture", blank=True, editable=True)
    is_verified = models.BooleanField("Is Verified", default=False)

    USERNAME_FIELD = 'phone'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return  self.name

class Country(models.Model):
    name = models.CharField("Country Name", max_length=255)
    code = models.CharField("Country Code", max_length=255)
    dial_code = models.CharField("Dial Code", max_length=10)

    def __str__(self):
        return self.dial_code
