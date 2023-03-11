from django.db import models

# Create your models here.


class Usuario(models.Model):
    Documento = models.BigIntegerField(null=False, blank=False)
    Nombres = models.CharField(max_length= 95)
    Correo = models.CharField(max_length= 255) 
    Direccion = models.CharField(max_length= 255) 
    Rol = models.CharField(max_length=2) 
    Telefono = models.BigIntegerField(null=False, blank=False) 
    Contrasena = models.CharField(max_length=15, blank=False, null=False)
    Foto = models.ImageField(null=True, blank=True, upload_to='profiles' ) 

    def __str__(self): 
        return self.Nombres