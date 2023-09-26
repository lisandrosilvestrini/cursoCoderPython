from django.urls import path
from appCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("items/", item, name="Item"),
    path("sellers/", seller, name="Seller"),
    path("users/", user, name="User"),
    path("sold_items/", sold_items, name="Sold_items"),
    path("purchased_items/", purchased_items, name="Purchase_items"),
    path("categorias/", categoria, name="Categorias"),
    path("tecnologia/", tecnologia, name="Tecnologia"),
    path("muebles/", muebles, name="Muebles"),
    path("cocina/", cocina, name="Cocina"),
    path("decoracion/", decoracion, name="Decoracion"),
    path("busqueda_categ/", busquedaCateg, name="busqueda_categ"),
    path("mostrar_categ/", mostrarCateg, name="mostrar_categ"),
]