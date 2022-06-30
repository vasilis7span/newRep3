from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_student = models.BooleanField('Is student', default=False)
    university = models.CharField(max_length=80, null=True)
    firstName = models.CharField(max_length=80, null=True)
    lastName = models.CharField(max_length=80, null=True)


    