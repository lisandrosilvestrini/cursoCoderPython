from django.urls import path
from appCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("items/", item, name="Item"),
    path("categorias/", categoria, name="Categorias"),
    path("tecnologia/", tecnologia, name="Tecnologia"),
    path("muebles/", muebles, name="Muebles"),
    path("cocina/", cocina, name="Cocina"),
    path("decoracion/", decoracion, name="Decoracion"),
    path("busqueda_categ/", busquedaCateg, name="busqueda_categ"),
    path("mostrar_categ/", mostrarCateg, name="mostrar_categ"),
    path("busqueda_items/", busquedaItems, name="busqueda_items"),
    path("mostrar_items/", mostrarItems, name="mostrar_items"),
]