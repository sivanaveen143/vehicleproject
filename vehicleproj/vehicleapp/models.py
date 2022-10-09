from email.policy import default
from statistics import mode
from urllib import request
from django.db import models

# Create your models here.

class userdetail(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    requested = models.CharField(max_length=50, default="none")
    status = models.CharField(max_length=50, default="pending")
class vmechanic(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    response = models.CharField(max_length=50, default="none")
    status = models.CharField(max_length=50, default="pending")
    
    