from django.shortcuts import render, HttpResponse



# Create your views here.

def home (request):
    return render(request, ("ProyectoWebCoop/home.html"))




def Prestamos (request):
    return render(request, ("ProyectoWebCoop/prestamos.html"))

def Ahorros (request):
    return render(request, ("ProyectoWebCoop/ahorros.html"))




def Nosotros (request):
    return render(request, ("ProyectoWebCoop/nosotros.html"))


