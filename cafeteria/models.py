from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=60)
    presentacion = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion