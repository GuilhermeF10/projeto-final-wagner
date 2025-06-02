from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='musicas')
    duracao = models.DurationField()

    def __str__(self):
        return f"{self.titulo} ({self.duracao})"
