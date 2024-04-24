from django import forms
from .models import Hazte_Socio
from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioSocio (forms.ModelForm):
    
    class Meta:
        model = Hazte_Socio
        fields=["nombre","apellido", "tipo_documento", "numero_documento", "correo_electronico", "fecha_nacimiento", "estado_civil", "telefono", "ocupacion", "direccion", "sector", "provincia"]
        #fields = '__all__'

        

class FormularioSocioAdmin (forms.ModelForm):
    
    class Meta:
        model = Hazte_Socio
        #fields=["nombre","apellido", "tipo_documento", "numero_documento", "correo_electronico", "fecha_nacimiento", "estado_civil", "telefono", "ocupacion", "direccion", "sector", "provincia"]
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields=['username', "first_name", "last_name", "email", "password1", "password2"]