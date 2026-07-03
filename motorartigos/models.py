from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


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

    titulo = models.CharField(
        max_length=200,
        verbose_name='Título',
        default='Sem título'
    )
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    TAG_NIVEL = [
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    ]
    nivel = models.CharField(
        max_length=1,
        choices=TAG_NIVEL,
        default='B',
        verbose_name='Nível'
    )

    def __str__(self):
        return f"Artigo {self.id} - {self.data_publicacao}"
    
    class Meta:
        db_table = 'artigo'
        ordering = ['-data_publicacao']