from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

class Company(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    empcount = models.IntegerField()
    location = models.CharField(max_length=100)
    
