from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from users.models import RegistroMascota



def home(request):
    context = {
        'posts': RegistroMascota.objects.all()  
    }
    return render(request, 'blog/home.html',context)


def about(request):
   return render(request, 'blog/about.html',{'title':'About'})



