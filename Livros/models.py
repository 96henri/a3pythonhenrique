from django.db import models

# Create your models here.

class Livro(models.Model):
    nomeLivro = models.CharField(max_length=255)
    categoriaLivro = models.CharField(max_length=255)


    def __str__(self):
        return self.nomeLivro
        return self.categoriaLivro

    class Meta:
        verbose_name_plural ="Livro"


