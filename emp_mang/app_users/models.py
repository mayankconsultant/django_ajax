#from typing_extensions import Required
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import appUserManger

# Create your models here.

class appuser(AbstractUser):
    username= None
    email   =models.EmailField(_('email address'),unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    objects = appUserManger()


    def __str__(self):
        return f"{self.email}!"