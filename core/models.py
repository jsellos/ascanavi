from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class DicasCategoria(models.Model):
    nome = models.CharField(max_length=30, verbose_name='categoria')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name        = 'categoria de dicas'
        verbose_name_plural = 'categorias de dicas'

class Dica(models.Model):
    idCat  = models.ForeignKey('DicasCategoria', verbose_name='categoria')
    dthora = models.DateTimeField(auto_now=True, verbose_name='data e hora da inclusão')
    titulo = models.CharField(max_length=100, verbose_name='título')
    texto  = models.TextField()
    imagem = ResizedImageField(size=[480, 375], upload_to='dicas')

    def __str__(self):
        return self.titulo

class NoticiasCategoria(models.Model):
    nome = models.CharField(max_length=30, verbose_name='categoria')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name        = 'categoria de notícias'
        verbose_name_plural = 'categorias de notícias'

class Noticia(models.Model):
    idCat  = models.ForeignKey('NoticiasCategoria', verbose_name='categoria')
    dthora = models.DateTimeField(auto_now=True, verbose_name='data e hora da inclusão')
    titulo = models.CharField(max_length=100, verbose_name='título')
    texto  = models.TextField()
    imagem = ResizedImageField(size=[480, 375], upload_to='noticias')

    def __str__(self):
        return self.titulo

class Associado(models.Model):
    nome   = models.CharField(max_length=50)
    imagem = ResizedImageField(size=[300,300], upload_to='associados', verbose_name='foto')

    def __str__(self):
        return self.nome

class Memoria(models.Model):
    data      = models.DateField(auto_now=True)
    descricao = models.TextField(max_length=500, verbose_name='descrição')
    imagem    = ResizedImageField(size=[780,600], upload_to='memorias')

    def __str__(self):
        return self.descricao[0:20]

    class Meta:
        verbose_name = 'memória'

class QuemSomos(models.Model):
    subtitulo      = models.TextField(verbose_name='subtítulo', max_length=200)
    texto_destaque = models.TextField(max_length=500)
    imagem    = ResizedImageField(size=[1920,790], upload_to='quem_somos')

    def __str__(self):
        return self.subtitulo[0:20]

    class Meta:
        verbose_name_plural = 'quem somos'