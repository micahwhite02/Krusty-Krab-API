from django.db import models
import uuid as uuid_object

from django.db.models.fields import AutoField

# Create your models here.
# WE USE MODELS TO TALK TO THE DATABASE
class PayRecord(models.Model):
    employee = models.CharField(max_length=120)
    transaction_id = models.UUIDField(default=uuid_object.uuid4)
    timestamp = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2 )

    def __str__(self): 
        return self.employee


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    species = models.CharField(max_length=30)


class Customer(models.Model):
    name = models.CharField(max_length = 30)
    order_number = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)


class Businesses(models.Model):
    business = models.CharField(max_length = 50)
    owner = models.CharField(max_length=50)
    tax_id = models.UUIDField(default=uuid_object.uuid4)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

## Models are a way to interact with the database

## Fetch Data from database 

