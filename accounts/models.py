from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    mobile = models.CharField(null=True,max_length=16)
    avatar = models.CharField(max_length=256)
    bio = models.TextField()
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=1)