from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo
