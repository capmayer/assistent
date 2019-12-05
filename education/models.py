from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conteudo(models.Model):
    nome = models.CharField(max_length=100)

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=15)
    professor = models.CharField(max_length=40)
    ementa = models.ManyToManyField(Conteudo)

class Prova(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    dia = models.DateTimeField()
    conteudo = models.ManyToManyField(Conteudo)
    registred = models.DateTimeField(auto_now=True)

class Trabalho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    entrega = models.DateTimeField()
    registred = models.DateTimeField(auto_now=True)

class Semestre(models.Model):
    sem = models.CharField(max_length=10)
    materias = models.ManyToManyField(Materia)
