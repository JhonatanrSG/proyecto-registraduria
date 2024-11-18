from .models import Ciudadano
from django.contrib import admin




@admin.register(Ciudadano)
class CiudadanoAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'identificacion')

