from django.urls import path
from appCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("items/", item, name="Items"),
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
    path("login/", login_req, name="login"),
    path("signup/", registro, name="signup"),
    path("logout/", LogoutView.as_view(template_name="appCoder/logout.html"), name="logout"),


    #CRUD items using classes
    path("items/list/", ListItems.as_view(), name="list_items"),
    path("items/detail/<int:pk>", DetailItems.as_view(), name="detail_items"),
    path("items/create/", CreateItems.as_view(), name="create_items"),
    path("items/update/<int:pk>", UpdateItems.as_view(), name="update_items"),
    path("items/delete/<int:pk>", DeleteItems.as_view(), name="delete_items"),
]