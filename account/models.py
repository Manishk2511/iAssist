from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    area = models.CharField(max_length=40)
    contact_no = models.CharField(max_length=14)
