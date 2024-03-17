from django.db import models

# Create your models here.
class student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    dob = models.DateField(max_length=20)
    password = models.CharField(max_length=20)