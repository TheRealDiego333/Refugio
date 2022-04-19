# Generated by Django 4.0.3 on 2022-04-18 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_registromascota'),
    ]

    operations = [
        migrations.AddField(
            model_name='registromascota',
            name='enfermedades',
            field=models.CharField(default='   ', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registromascota',
            name='fecha_de_rescate',
            field=models.CharField(default='15/12/1998', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registromascota',
            name='raza',
            field=models.CharField(default='No definido', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registromascota',
            name='vacunacion',
            field=models.CharField(default='Desconocido', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registromascota',
            name='edad',
            field=models.CharField(max_length=30),
        ),
    ]
