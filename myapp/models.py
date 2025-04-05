from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone = models.BigIntegerField(unique=True, null=True)
    city = models.CharField(max_length=100, null=True)
    profile_pic = models.ImageField(upload_to='profilePic/', null=True)