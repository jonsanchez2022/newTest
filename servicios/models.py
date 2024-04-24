from tabnanny import verbose

from django.db import models

# Create your models here.

 
class Servicioss (models.Model):
    nombre=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='servicios')
    cambio=models.CharField(max_length=2)
    created=models.DateTimeField(auto_now_add=True)
    udpated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    def __str__ (self):
        return self.nombre
