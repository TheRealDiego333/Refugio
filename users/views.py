from cgitb import html
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from matplotlib.style import context
from .forms import Agregarmascota, UserRegisterForm, UserUpdateForm, ProfileUpdateForm, SolicitudAdopcion
from .models import RegistroMascota, Profile, SolicitudAdop

def catalogo(request):
    lista_catalogo = RegistroMascota.objects.all()
    return render(request,'users/Catalogo.html', {'lista_catalogo': lista_catalogo })



def registromascota(request):
    if request.method == 'POST':
        registro = Agregarmascota(request.POST, request.FILES)
        if registro.is_valid(): 
            registro.save()
            return redirect('catalogo')
    else:
        registro = Agregarmascota()
    return render(request, 'users/registromascota.html', {'registro':registro})



def solicitud(request):

    if request.method == 'POST':
        lista_solicitudes = SolicitudAdopcion(request.POST, request)
        if lista_solicitudes.is_valid():
            lista_solicitudes.save()
            return redirect('catalogo')
    else:
        registro = Agregarmascota()
    return render(request, 'users/formulario.html', {'registro':registro})


def listado_solicitantes(request):
    lista_solicitantes = SolicitudAdop.objects.all()
    return render(request,'users/listado_solicitantes.html',{'lista_solicitantes':lista_solicitantes})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!, You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})


#def actualizarcomida(request):
#    actucomida = CambiarComida(request.POST)
#    lista_catalogo = RegistroMascota.objects.all()
#    lista_nombres = Profile.objects.all()
#    if request.method == 'POST':
#        actucomida = CambiarComida(request.POST)
#        if actucomida.is_valid():
#            actucomida.save
#            messages.success(request, f'La alimentacion a sido actualizada')
#            return redirect ('profile')
#    context = {
#        'actucomida':actucomida,
#        'lista_catalogo': lista_catalogo, 
#        'lista_nombres': lista_nombres
#    }
#
#    return render(request, 'users/actualizar_comida.html',context)

@login_required  
def profile(request):
    lista_catalogo = RegistroMascota.objects.all()
    lista_nombres = Profile.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Su cuenta ha sido actualizada')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form,
        'lista_catalogo': lista_catalogo, 
        'lista_nombres': lista_nombres
    }


    return render(request, 'users/profile.html', context)



