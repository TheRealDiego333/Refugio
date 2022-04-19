import email
from lzma import FORMAT_ALONE
from re import template
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, RegistroMascota, SolicitudAdop 


class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class Agregarmascota (forms.ModelForm):
    class Meta:
        model = RegistroMascota 
        fields = ['nombre','edad','alimentacion','fecha_de_rescate','raza','enfermedades','imagen']

class SolicitudAdopcion(forms.ModelForm):
    class Meta:
        model = SolicitudAdop
        fields = "__all__"

