from django.urls import path
from appCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("items/", item, name="Items"),
    path("about/", about, name="about"),
    path("categorias/", categoria, name="Categorias"),
    path("tecnologia/", tecnologia, name="Tecnologia"),
    path("muebles/", muebles, name="Muebles"),
    path("cocina/", ListItemsCocina.as_view(), name="Cocina"),
    path("decoracion/", decoracion, name="Decoracion"),
    path("busqueda_categ/", busquedaCateg, name="busqueda_categ"),
    path("mostrar_categ/", mostrarCateg, name="mostrar_categ"),
    
    #user actions
    path("login/", login_req, name="login"),
    path("signup/", registro, name="signup"),
    path("logout/", LogoutView.as_view(template_name="appCoder/logout.html"), name="logout"),
    path("update_profile/", update_user, name="update_profile"),
    path("addAvatar/", agregar_avatar, name="addAvatar"),

    #CRUD items using classes
    path("items/list/", ListItems.as_view(), name="list_items"),
    path("items/detail/<int:pk>", DetailItems.as_view(), name="detail_items"),
    path("items/create/", CreateItems.as_view(), name="create_items"),
    path("items/update/<int:pk>", UpdateItems.as_view(), name="update_items"),
    path("items/delete/<int:pk>", DeleteItems.as_view(), name="delete_items"),

    #CRUD category using classes
    path("category/list/", ListCat.as_view(), name="list_cat"),
    path("category/detail/<int:pk>", DetailCat.as_view(), name="detail_cat"),
    path("category/create/", CreateCat.as_view(), name="create_cat"),
    path("category/update/<int:pk>", UpdateCat.as_view(), name="update_cat"),
    path("category/delete/<int:pk>", DeleteCat.as_view(), name="delete_cat"),
]