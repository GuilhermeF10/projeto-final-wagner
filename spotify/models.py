

# spotify/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    idade = models.PositiveIntegerField(null=True, blank=True)

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
