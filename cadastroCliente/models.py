from django.db import models

# Create your models here.

class Genero(models.Model):

    sexo = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.sexo}'

class Cadastro_Cliente(models.Model):
    
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=50 )
    nascimento = models.DateField()
    numero = models.CharField(max_length=11)
    Genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE
    )
