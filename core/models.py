from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome  = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)