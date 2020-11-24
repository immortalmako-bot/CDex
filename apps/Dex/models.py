from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo_seguridad = models.CharField(max_length=4, null=False)
    biografia = models.CharField(max_length=200)


class Criatura(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    edad = models.IntegerField(null=False)
    estatura = models.CharField(max_length=10,null=False)
    naturaleza = models.CharField(max_length=30, null=False)
    origen = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='uploads')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
