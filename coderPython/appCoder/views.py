from django.shortcuts import render
from django.http import HttpResponse
from appCoder.models import *

# Create your views here.
def inicio(request):

    return HttpResponse("inicio")

def item(request):

    item_1 = Item(title="Bicicleta amarilla", price=155.65, description="Bici casi nueva, joyita nunca taxi")
    item_1.save()

    return HttpResponse(f"El item que creaste es: {item_1.title} {item_1.price} {item_1.description}")

def user(request):
    
    return HttpResponse("esta es la vista de user")


def seller(request):
    
    return HttpResponse("esta es la vista de seller")

def sold_items(request):
    
    return HttpResponse("esta es la vista de sold_items")

def purchased_items(request):
    
    return HttpResponse("esta es la vista de purchased_items")


