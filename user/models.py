from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify

# Create your models here.


class Main_routes(models.Model):
    city_name = models.CharField(max_length=100)
    bus_count  = models.CharField(max_length=100)
    val = models.SlugField(max_length=150) 
    
def _str_(self):
    return self.name

class rout_detailes(models.Model):
    bus_number = models.CharField(max_length=100)
    bus_type = models.CharField(max_length=100)
    travel_hour = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    seating = models.CharField(max_length=100)
    city_2 = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
   
def _str_(self):
    return self.name
    
class Bus_booking(models.Model):
    username = models.CharField(max_length=100,blank=False,null=False)
    email = models.EmailField(max_length=254,blank=False,null=False)
    phone_number = models.CharField(max_length=100,blank=False,null=False)
    place = models.CharField(max_length=100,blank=False,null=False)
    
class User(models.Model):
    Username = models.CharField(max_length=100)
    Password1 = models.CharField(max_length=50)
    Password2 = models.CharField(max_length=50)
    email = models.EmailField()