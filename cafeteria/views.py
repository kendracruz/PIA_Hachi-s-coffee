from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    return render(request, "index.html")

def menu(request):
    datos = {
        "info": models.Producto.objects.all()
    }
    return render(request, "menu.html", context=datos)

def eventos(request):
    return render(request, "eventos.html")

def nosotros(request):
    return render(request, "nosotros.html")

def tienda_online(request):
    return render(request, "tienda_online.html")

def ubicacion(request):
    return render(request, "ubicacion.html")