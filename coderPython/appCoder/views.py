from django.shortcuts import render
from django.http import HttpResponse
from appCoder.forms import *
from appCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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

    # item_1 = Item(title="Bicicleta amarilla", price=155.65, description="Bici casi nueva, joyita nunca taxi")
    # item_1.save()

    # return HttpResponse(f"El item que creaste es: {item_1.title} {item_1.price} {item_1.description}")

def user(request):
    
    return render(request,"appCoder/user.html")

def seller(request):
    
    return render(request,"appCoder/seller.html")

def sold_items(request):
    
    return render(request,"appCoder/sold_items.html")

def purchased_items(request):
    
    return render(request,"appCoder/purchased_items.html")




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


def readItems(request):

    items = Item.objects.all()

    context = {"items":items}

    return render(request, "appCoder/readItems.html", context)

class ListItems(ListView):

    model = Item

class DetailItems(DetailView):

    model = Item

class CreateItems(CreateView):

    model = Item
    success_url = "/appCoder/items/list"
    fields = ["title","price","description","created_date","condition"]

class UpdateItems(UpdateView):

    model = Item
    success_url = "/appCoder/items/list"
    fields = ["title","price","description","created_date","condition"]

class DeleteItems(DeleteView):

    model = Item
    success_url = "/appCoder/items/list"
    