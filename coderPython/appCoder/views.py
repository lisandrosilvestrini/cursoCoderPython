from django.shortcuts import render
from django.http import HttpResponse
from appCoder.forms import *
from appCoder.models import *

# Create your views here.
def inicio(request):

    return render(request,"appCoder/inicio.html")

def item(request):

    if request.method == "POST":

        formItem = ItemsForm(request.POST)

        if formItem.is_valid():

            info = formItem.cleaned_data

            obj = Item(title=info["title"], description=info["description"], price=info["price"])

            obj.save()         

            return render(request, "appCoder/inicio.html")
    
    else:
        formItem = ItemsForm()
    
    return render(request,"appCoder/item.html", {"form_item":formItem})


def mostrarItems(request):

    if request.GET["busqueda_items"]:

        item = request.GET["busqueda_items"]
        items = Item.objects.filter(title__icontains=item)
        print("items",items)
        print("item",item)
        return render(request, "appCoder/item.html", {"items":items, "busqueda_items":item})

    else:

        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

def busquedaItems(request):
    
    return render(request,"appCoder/item.html")



def categoria(request):
    
    if request.method == "POST":

        form = CategoriaForm(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            cat = Categ(name=info["name"], description=info["description"])

            cat.save()         

            return render(request, "appCoder/inicio.html")
    
    else:
        form = CategoriaForm()
    
    return render(request,"appCoder/categoria.html", {"form_cat":form})


def busquedaCateg(request):
    
    return render(request,"appCoder/categoria.html")


def mostrarCateg(request):

    if request.GET["busqueda_categ"]:

        categoria = request.GET["busqueda_categ"]
        cat = Categ.objects.filter(name__icontains=categoria)
        print("cat",cat)
        print("categoria",categoria)
        return render(request, "appCoder/categoria.html", {"categorias":cat, "busqueda_categ":categoria})

    else:

        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)


def tecnologia(request):
    
    return render(request,"appCoder/tecnologia.html")

def muebles(request):
    
    return render(request,"appCoder/muebles.html")

def cocina(request):
    
    return render(request,"appCoder/cocina.html")

def decoracion(request):
    
    return render(request,"appCoder/decoracion.html")

