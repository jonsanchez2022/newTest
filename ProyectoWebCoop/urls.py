from django import urls
from django.urls import path
from ProyectoWebCoop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path ('', views.home, name="Home"),
    
    path ('Prestamos', views.Prestamos, name="Prestamos"),
    path ('Ahorros', views.Ahorros, name="Ahorros"),

    path ('Nosotros', views.Nosotros, name="Nosotros"),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
