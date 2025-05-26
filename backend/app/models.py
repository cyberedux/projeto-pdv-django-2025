from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()
    custo = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descricao} - {self.categoria}'