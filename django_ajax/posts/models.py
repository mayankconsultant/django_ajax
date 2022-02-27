from statistics import mode
from turtle import title
from django.db import models
from django.conf import settings
# Create your models here.

from profiles.models import Profile

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=50,verbose_name='Post Title')
    body = models.TextField(verbose_name="Scripts Steps")
    liked = models.ManyToManyField(User,related_name='liked', blank = True )
    author = models.ForeignKey(Profile,on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return f"{self.title} by {self.profile.user.username}"

    class Meta:
        ordering =['-created','-updated']