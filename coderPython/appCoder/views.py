from django.shortcuts import render
from django.http import HttpResponse
from appCoder.forms import *
from appCoder.models import *

# Create your views here.
def inicio(request):

    return render(request,"appCoder/inicio.html")

def item(request):

    item_1 = Item(title="Bicicleta amarilla", price=155.65, description="Bici casi nueva, joyita nunca taxi")
    item_1.save()

    return HttpResponse(f"El item que creaste es: {item_1.title} {item_1.price} {item_1.description}")

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
    
    return render(request,"appCoder/categoria.html", {"form1":form})


def busquedaCateg(request):
    
    return render(request,"appCoder/busquedaCateg.html")


def mostrar(request):

    if request.GET["categoria"]:

        categoria = request.GET["categoria"]
        cat = Categoria.objects.filter(categoria__icontains=categoria)

        return render(request, "appCoder/resultados.html", )

    return HttpResponse(f"Estas buscando la categoría: {request.GET['categoria']}")

def tecnologia(request):
    
    return render(request,"appCoder/tecnologia.html")

def muebles(request):
    
    return render(request,"appCoder/muebles.html")

def cocina(request):
    
    return render(request,"appCoder/cocina.html")

def decoracion(request):
    
    return render(request,"appCoder/decoracion.html")

