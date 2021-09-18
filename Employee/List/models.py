from django.db import models

from django.conf import settings
# Create your models here.

class Ta_Da(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=50)
    travel_cost = models.FloatField()
    lunch_cost = models.FloatField()
    instrument_cost = models.FloatField()
    total_cost = models.FloatField()
    Paid = models.CharField(max_length=20)


   

class Employee(models.Model):
    name = models.CharField(max_length=50)
    