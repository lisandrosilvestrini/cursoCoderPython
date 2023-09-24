from django.db import models

# Create your models here.

class Item(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField

class User(models.Model):

    name = models.CharField
    last_name = models.CharField
    password = models.CharField
    email = models.EmailField
    created_date = models.DateTimeField

class Sold_items(models.Model):

    item_id = models.UUIDField
    units = models.IntegerField
    sold_date = models.DateTimeField

class Purchased_items(models.Model):

    item_id = models.UUIDField
    units = models.IntegerField
    purchase_date = models.DateTimeField

class Seller(models.Model):
    
    name = models.CharField
    score = models.IntegerField
    reputation = models.CharField
    address = models.CharField