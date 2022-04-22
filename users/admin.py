from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile, RegistroMascota, SolicitudAdop



admin.site.site_header='Administración del Refugio'



admin.site.register(Profile)
admin.site.register(RegistroMascota)
admin.site.register(SolicitudAdop)