from django.shortcuts import render
from . import models

# Create your views here.
def index (request):
    return render(request, "index.html")

def menu(request):
    datos = {
        "info" : models.Producto.objects.all()
    }
    return render(request, "menu.html", context=datos)