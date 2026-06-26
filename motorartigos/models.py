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

class Artigo(models.Model):
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    id_fk_eixo = models.ForeignKey(
        EixoTecnologia,
        on_delete=models.CASCADE,
        db_column='id_fk_eixo'
    )
    id_fk_autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        db_column='id_fk_autor'
    )

    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)

    def __str__(self):
        return f"Artigo {self.id} - {self.data_publicação}"
    
    class Meta:
        db_table = 'artigo'