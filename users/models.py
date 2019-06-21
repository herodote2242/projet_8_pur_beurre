from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=16)


#class Profile(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
