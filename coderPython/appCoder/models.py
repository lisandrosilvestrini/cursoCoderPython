from django.db import models

# Create your models here.

class Item(models.Model):

    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    