from pickle import TRUE
from tkinter import Widget
from django.db import models
from django.forms import CharField
from datetime import date
# Create your models here.


opciones_tipo_documento = [
    [0, "Cedula"],
    [1, "Pasaporte"]
]

opciones_estado = [
    [0, "Pendiente"],
    [1, "Activo"],
    [2, "Inactivo"]
]

opciones_estado_civil = [
    [0, "Casado/a"],
    [1, "Soltero/a"],
    [2, "Viudo/a"],
    [3, "Separado/a"],
    [4, "Union Libre"],
    [5, "Divorciado/a"]
]

class Hazte_Socio (models.Model):
    nombre=models.CharField(max_length=50, verbose_name="Nombre ")
    apellido=models.CharField(max_length=50, verbose_name="Apellido ")
    tipo_documento=models.IntegerField(choices=opciones_tipo_documento, verbose_name="Tipo de Documento ")
    numero_documento=models.CharField(max_length=11, null=TRUE, verbose_name="Número de Documento ") 
    correo_electronico=models.EmailField(verbose_name="Correo Electrónico ")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento ")
    estado_civil=models.IntegerField(choices=opciones_estado_civil, verbose_name="Estado Civil ")
    telefono=models.CharField(max_length=10, verbose_name="Teléfono ")
    ocupacion=models.CharField(max_length=25, verbose_name="Ocupación ")
    direccion=models.CharField(max_length=100, verbose_name="Dirección ")
    sector=models.CharField(max_length=25, verbose_name="Sector ")
    provincia=models.CharField(max_length=25, verbose_name="Provincia ")
    estado=models.IntegerField(choices=opciones_estado, null=TRUE, verbose_name="Estado ")
    
    class Meta:
        verbose_name='Socio'
        verbose_name_plural='Socios'

    def __str__(self):
        return self.nombre