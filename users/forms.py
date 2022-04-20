import email
from lzma import FORMAT_ALONE
from re import template
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from matplotlib import widgets
from .models import Profile, RegistroMascota, SolicitudAdop 
from django.forms import *


class UserRegisterForm (UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    email = EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': TextInput(
                attrs={
                    'readonly':'readonly',
                }
            )
        }

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','image']
        widgets = {
            'name': TextInput(
                attrs={
                    'readonly':'readonly',
                }
            )
        }
        

class Agregarmascota (ModelForm):
    class Meta:
        model = RegistroMascota 
        fields = ['nombre','edad','alimentacion','fecha_de_rescate','raza','enfermedades','imagen']

class SolicitudAdopcion(ModelForm):
    class Meta:
        model = SolicitudAdop
        fields = "__all__"

