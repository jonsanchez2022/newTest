from django.shortcuts import render, redirect, get_object_or_404
from .models import Hazte_Socio
from .forms import CustomUserCreationForm, FormularioSocio, FormularioSocioAdmin, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
# Create your views here.




def Socio (request):
    data={
        'form': FormularioSocio()
    }
    if request.method == 'POST':
        formulario = FormularioSocio(data=request.POST)
        if formulario.is_valid:
           formulario.save()
           messages.success(request,"Solicitud Enviada Correctamente, Tiempo estimado 7-10 días")
        else:
            data["form"]=formulario
    return render (request, "hazte_socio/hazte_socio.html", data)


def ListarSocios (request):
    lista = Hazte_Socio.objects.all()

    data = {
        'lista':lista
    }
    return render (request, "hazte_socio/listar.html", data)



def ModificarSocio (request, id):
    modificar = get_object_or_404(Hazte_Socio, id=id)
    data ={
        'form': FormularioSocioAdmin(instance=modificar)
    }
 
    if request.method =='POST':
        formulario = FormularioSocioAdmin(data=request.POST, instance=modificar)
        if formulario.is_valid():
            formulario.save()
            nombre=formulario.cleaned_data['nombre']
            correo_electronico=formulario.cleaned_data['correo_electronico']
            estado=formulario.cleaned_data['estado']
            messages.success(request,"Modificado Correctamente")

            html= render_to_string('hazte_socio/correo_socios/socioCorreo.html',{
            'Nombre':nombre,
            'Email':correo_electronico,
            'Estado':estado,

            
            })
            send_mail('Estado Solicitud de Nuevo Socio', '', 'noreply@hotmail.com', ['jonatan_manuel_sanchez@hotmail.com'], html_message=html)


            return redirect(to="/Hazte_Socio/Listar_Socios")


        data["form"]=formulario
    return render (request, "hazte_socio/modificar.html", data)



def RegistroUsuario (request):
    data ={
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid:
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            messages.success(request,"Usuario Registrado Correctamente")
            return redirect (to="listar_socios")
        data["form"]=formulario
    return render (request, "registration/registro.html", data)