# Generated by Django 4.0.3 on 2022-04-18 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('alimentacion', models.CharField(max_length=50)),
                ('edad', models.CharField(max_length=50)),
            ],
        ),
    ]
