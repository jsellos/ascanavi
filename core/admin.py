from django.contrib import admin
from .models import DicasCategoria, Dica, NoticiasCategoria, Noticia, Associado, Memoria, QuemSomos, NossaHistoria, LinkUtil, Contato, Contribuir, ContribuirItem

class _dica(admin.ModelAdmin):
    Model        = Dica
    list_display = ['dt_hora', 'titulo']
    list_filter  = ['dt_hora', 'titulo']

class _noticia(admin.ModelAdmin):
    Model        = Noticia
    list_display = ['dt_hora', 'titulo']
    list_filter  = ['dt_hora', 'titulo']

class _memoria(admin.ModelAdmin):
    Model        = Memoria
    list_display = ['data', 'descricao']
    list_filter  = ['data', 'descricao']

admin.site.register(Dica, _dica)
admin.site.register(Noticia, _noticia)
admin.site.register(Memoria, _memoria)
admin.site.register((
    DicasCategoria,
    NoticiasCategoria,
    Associado,
    QuemSomos,
    NossaHistoria,
    LinkUtil,
    Contato,
    Contribuir,
    ContribuirItem,
))