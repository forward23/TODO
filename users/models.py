from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/anonymous.png')
