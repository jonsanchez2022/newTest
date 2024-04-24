from django.shortcuts import render, redirect
from .import views
from .forms import formularioContacto
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.template.loader import render_to_string


# Create your views here.
def Contacto (request):
    formulario_contacto=formularioContacto()
    if request.method=="POST":

            
        formulario_contacto=formularioContacto(request.POST)
        if formulario_contacto.is_valid():
            nombre=formulario_contacto.cleaned_data['nombre']
            email=formulario_contacto.cleaned_data['email']
            telefono=formulario_contacto.cleaned_data['telefono']
            sujeto=formulario_contacto.cleaned_data['sujeto']
            contenido=formulario_contacto.cleaned_data['contenido']
            messages.success(request,"Su mensaje ha sido enviado correctamente")
            html= render_to_string('contacto/correos_contacto/contactoForm.html',{
                'Nombre':nombre,
                'Email': email,
                'Telefono': telefono,
                'Sujeto':sujeto,
                'Contenido':contenido

            })

            send_mail('Un Socio tiene una nueva sugerencia', 'Este es el mensaje', 'noreply@hotmail.com', ['jonatan_manuel_sanchez@hotmail.com'], html_message=html)


            return redirect ('/Contacto')

        else:
            formulario_contacto=formularioContacto()
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})