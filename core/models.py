from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.titulo