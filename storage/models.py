from django.db import models

# Create your models here.


class Motorista(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    celular = models.CharField(max_length=11)
    codigo = models.CharField(max_length=8)
    prod_entregar = models.IntegerField()
    prod_falha = models.IntegerField()
    prod_em_curso = models.IntegerField()

    def __str__(self) -> str:
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    codigo = models.CharField(max_length=8)
    endereco_entrega = models.TextField(max_length=250)
    proprietario = models.CharField(max_length=100)
    celular1 = models.CharField(max_length=11)
    celular2 = models.CharField(max_length=11)
    localizacao = models.CharField(max_length=30)
