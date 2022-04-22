from ctypes import alignment
from dataclasses import field
import email
from lzma import FORMAT_ALONE
from pyexpat import model
from re import template
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
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

#class CambiarComida(ModelForm):
#    alimentacion = CharField()
#    class Meta:
#        model = RegistroMascota
#       fields = ['alimentacion']
#

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


class PwdResetForm(PasswordResetForm):
    email = EmailField(max_length=254, widget=TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = User.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Desafortunadamente no pudimos encontrar ningun usuario con este email')
        return email

class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = CharField(
        label='Nueva Contraseña', widget=PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nueva Contraseña', 'id': 'form-newpass'}))
    new_password2 = CharField(
        label='Repite tu Contraseña', widget=PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Nueva Contraseña', 'id': 'form-new-pass2'}))