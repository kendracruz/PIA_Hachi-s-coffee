from django.contrib import admin
from . import models 
# Register your models here.
admin.site.register(models.Producto)
admin.site.register(models.Sucursal)
admin.site.register(models.Auto)
admin.site.register(models.Evento)
admin.site.register(models.Comentario)
