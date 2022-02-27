from distutils.command.upload import upload
from statistics import mode
from django.db import models

from django.conf import settings


User = settings.AUTH_USER_MODEL

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(default= 'avatar.png',upload_to = 'avatars')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Profile of {self.user.email}"

