from django.db import models
from authentication.models import Usuario
# Create your models here.

class Producto(models.Model):

    Nombre = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=15) 
    Descripcion = models.CharField(max_length=255) 
    Caracteristicas = models.TextField(blank=True, null=True)
    Disponible = models.IntegerField()
    Precio_base = models.DecimalField(max_digits=9, decimal_places=3)
    Porcentaje_plataforma = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    Porcentaje_venta = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    Precio_calculado = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    material = models.CharField(max_length=55, blank=True, null=True)
    Portada = models.ImageField(upload_to='portada')
    Estado = models.BooleanField(default=False)
    Genero = models.CharField(max_length=3, null=True, blank=True)
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre 
    

class ProductImage(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='images')
    Imagen = models.ImageField(upload_to='products', blank=True, null=True)

    def __str__(self):
        return self.Producto.Nombre


class Comentario(models.Model):
    Calificacion = models.IntegerField()
    Comentario = models.TextField(max_length=355)
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.Calificacion + ' ' +self.Producto 

