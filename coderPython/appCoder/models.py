from django.db import models

# Create your models here.

class Item(models.Model):

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

class User(models.Model):

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    created_date = models.DateTimeField()

class Sold_items(models.Model):

    item_id = models.UUIDField()
    units = models.IntegerField()
    sold_date = models.DateTimeField()

class Purchased_items(models.Model):

    item_id = models.UUIDField()
    units = models.IntegerField()
    purchase_date = models.DateTimeField()

class Seller(models.Model):
    
    name = models.CharField(max_length=200)
    score = models.IntegerField()
    reputation = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class Categ(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


class Categoria(models.Model):
    pass
class Tecnologia(models.Model):
    pass
class Muebles(models.Model):
    pass
class Cocina(models.Model):
    pass
class Decoracion(models.Model):
    pass
