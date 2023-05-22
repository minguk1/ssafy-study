from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    pass
    # password = models.CharField(max_length=30)
    # password = models.CharField(max_length=30)
    
    