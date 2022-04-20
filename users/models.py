from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.forms import modelform_factory
from sklearn.model_selection import RandomizedSearchCV
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name  = models.CharField(max_length= 50)
    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300  or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class RegistroMascota (models.Model):
    imagen           = models.ImageField(default='default.jpg', upload_to='fotos_mascotas')
    alimentacion     = models.CharField(max_length= 50)
    vacunacion       = models.CharField(max_length= 100)
    edad             = models.CharField(max_length= 30)
    fecha_de_rescate = models.DateTimeField(default=timezone.now)
    raza             = models.CharField(max_length= 50)
    enfermedades     = models.CharField(max_length= 50)
    nombre           = models.CharField(max_length= 50)
    adoptante        = models.CharField(default='Disponible', max_length= 50)

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        super(RegistroMascota, self).save(*args, **kwargs)

        img = Image.open(self.imagen.path)
        if (img.height > 300  or img.width >300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.imagen.path)


class SolicitudAdop (models.Model):
    Nombre     = models.CharField(max_length=50)
    Edad       = models.CharField(max_length=50)
    Correo     = models.EmailField()
    Telefono   = models.CharField(max_length=8)
    Domicilio  = models.CharField(max_length=100)
    NumeroMasc = models.IntegerField()
    Razones    = models.CharField(max_length=150)
    
    def __str__(self):
        return self.Nombre

    def save(self):
        super().save()
