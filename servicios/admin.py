from django.contrib import admin
from .models import Servicioss


# Register your models here.

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'udpated')
  
admin.site.register(Servicioss, ServiciosAdmin)