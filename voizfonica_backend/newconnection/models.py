from djongo import models
from django import forms
from datetime import datetime

class Porting(models.Model):
    current_mobile_number=models.CharField(max_length=10)
    current_network=models.CharField(max_length=100)
    upc=models.CharField(max_length=100)
    requested_date_time=models.DateTimeField(default=datetime.now(), blank=True)
    status=models.CharField(max_length=100)
    circle=models.CharField(max_length=100)

    
    def __str__(self):
        return self.upc

class Connection(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    circle=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.first_name



