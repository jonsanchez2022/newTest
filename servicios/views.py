from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Servicioss

def Servicios(request):
    vservicios = Servicioss.objects.all()
    return render(request, "servicios/servicios.html", {"vservicios": vservicios})
