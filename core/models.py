from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Index(models.Model):
    principal_titulo    = models.CharField(max_length=100, verbose_name='título principal')
    principal_subtitulo = models.CharField(max_length=100, verbose_name='subtítulo principal')
    principal_imagem    = ResizedImageField(size=[1920, 715], upload_to='index', verbose_name='imagem principal')
    dica_titulo         = models.CharField(max_length=100, verbose_name='título da dica')
    dica1_id            = models.ForeignKey('Dica', related_name='dica1_id', verbose_name='dica da esquerda')
    dica1_imagem        = ResizedImageField(size=[780, 780], upload_to='index', verbose_name='imagem da dica da esquerda')
    dica2_id            = models.ForeignKey('Dica', related_name='dica2_id', verbose_name='dica do meio')
    dica2_imagem        = ResizedImageField(size=[780, 780], upload_to='index', verbose_name='imagem da dica do meio')
    dica3_id            = models.ForeignKey('Dica', related_name='dica3_id', verbose_name='dica da direita')
    dica3_imagem        = ResizedImageField(size=[780, 780], upload_to='index', verbose_name='imagem da dica da direita')
    contribuir_titulo   = models.CharField(max_length=100, verbose_name='texto sobre contribuir')
    contribuir_imagem   = ResizedImageField(size=[1920, 1200], upload_to='index', verbose_name='imagem sobre contribuir')
    contrinuir_botao    = models.CharField(max_length=100, verbose_name='texto do botão sobre contribuir')

    def __str__(self):
        return self.principal_titulo

    class Meta:
        verbose_name        = 'início'
        verbose_name_plural = 'início'

class DicasCategoria(models.Model):
    nome = models.CharField(max_length=30, verbose_name='categoria')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name        = 'categoria de dicas'
        verbose_name_plural = 'categorias de dicas'

class Dica(models.Model):
    id_cat         = models.ForeignKey('DicasCategoria', verbose_name='categoria')
    dt_hora        = models.DateTimeField(auto_now=True, verbose_name='data e hora da inclusão')
    titulo         = models.CharField(max_length=100, verbose_name='título')
    texto_destaque = models.TextField(max_length=500, verbose_name='texto de destaque')
    texto          = models.TextField()
    imagem         = ResizedImageField(size=[480, 375], upload_to='dicas')

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
    id_cat         = models.ForeignKey('NoticiasCategoria', verbose_name='categoria')
    dt_hora        = models.DateTimeField(auto_now=True, verbose_name='data e hora da inclusão')
    titulo         = models.CharField(max_length=100, verbose_name='título')
    texto_destaque = models.TextField(max_length=500, verbose_name='texto de destaque')
    texto          = models.TextField()
    imagem         = ResizedImageField(size=[480, 375], upload_to='noticias')

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
        return self.descricao[0:50]

    class Meta:
        verbose_name = 'memória'

class QuemSomos(models.Model):
    subtitulo      = models.CharField(verbose_name='subtítulo', max_length=200)
    texto_destaque = models.TextField(max_length=500)
    imagem         = ResizedImageField(size=[1920,790], upload_to='quem_somos')

    def __str__(self):
        return self.subtitulo[0:50]

    class Meta:
        verbose_name_plural = 'quem somos'

class NossaHistoria(models.Model):
    subtitulo_cabecalho = models.CharField(verbose_name='subtítulo', max_length=200)
    imagem              = ResizedImageField(size=[1920, 790], upload_to='nossa_historia')
    texto_destaque      = models.TextField(max_length=500)
    titulo_historia     = models.CharField(max_length=200)
    historia            = models.TextField()

    def __str__(self):
        return self.subtitulo_cabecalho[0:50]

    class Meta:
        verbose_name        = 'nossa história'
        verbose_name_plural = 'nossa história'

class LinkUtil(models.Model):
    link       = models.URLField()
    descricao  = models.CharField(verbose_name='descrição', max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name        = 'link útil'
        verbose_name_plural = 'links úteis'

class Contato(models.Model):
    email            = models.EmailField()
    id_dica_coleta   = models.ForeignKey('Dica', verbose_name='Dias e horários de coleta')
    facebook         = models.URLField()

    def __str__(self):
        return self.email

class Contribuir(models.Model):
    subtitulo_cabecalho = models.CharField(verbose_name='subtítulo', max_length=200)
    imagem              = ResizedImageField(size=[1920, 790], upload_to='contribuir')
    titulo_rodape       = models.CharField(max_length=200)
    texto_rodape_1      = models.TextField()
    texto_rodape_2      = models.TextField()
    texto_rodape_3      = models.TextField()

    def __str__(self):
        return self.subtitulo_cabecalho[0:50]

    class Meta:
        verbose_name        = 'contribuir'
        verbose_name_plural = 'contribuir'

class ContribuirItem(models.Model):
    titulo = models.CharField(verbose_name='título', max_length=200)
    texto  = models.TextField(verbose_name='texto')
    imagem = ResizedImageField(size=[1920, 790], upload_to='contribuir_itens')

    def __str__(self):
        return self.titulo[0:50]

    class Meta:
        verbose_name        = 'contribuir item'
        verbose_name_plural = 'contribuir itens'