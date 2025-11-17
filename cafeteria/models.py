from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100, default='Sin nombre')
    descripcion = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    horario_apertura = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Auto(models.Model):
    placa = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=80)
    modelo = models.CharField(max_length=80)
    color = models.CharField(max_length=40, blank=True, null=True)
    anio = models.PositiveSmallIntegerField(blank=True, null=True)
    nombre_dueno = models.CharField(max_length=120)
    telefono_dueno = models.CharField(max_length=30, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True, related_name='autos')

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True, related_name='eventos')
    capacidad = models.PositiveIntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    email = models.EmailField(blank=True, null=True)
    mensaje = models.TextField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.SET_NULL, null=True, blank=True, related_name='comentarios')
    evento = models.ForeignKey(Evento, on_delete=models.SET_NULL, null=True, blank=True, related_name='comentarios')

    def __str__(self):
        return f"{self.email}"
