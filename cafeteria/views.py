from django.shortcuts import render
from . import models
from .models import Evento
from .models import Sucursal

# Create your views here.
def index(request):
    return render(request, "index.html")

def menu(request):
    datos = {
        "info": models.Producto.objects.all()
    }
    return render(request, "menu.html", context=datos)

def eventos(request):
    eventos = Evento.objects.all()

    return render(request, "eventos.html", {'eventos': eventos})

def nosotros(request):
    return render(request, "nosotros.html")

def tienda_online(request):
    return render(request, "tienda_online.html")

def ubicacion(request):
    sucursales = Sucursal.objects.all()

    return render(request, "ubicacion.html", {'sucursales': sucursales})