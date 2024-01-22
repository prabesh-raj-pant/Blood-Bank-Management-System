# accounts/models.py
from django.db import models
from django.contrib.auth.hashers import check_password

class UserProfile(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username



