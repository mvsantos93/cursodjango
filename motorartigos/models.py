from django.db import models

# Create your models here.
# aqui vou criar minhas classses de entidade

class Autor(models.Model):
    #O atributo id é automático.
    # chave primária: imutável, universal e única
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'autor'


class EixoTecnologia(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'eixo'