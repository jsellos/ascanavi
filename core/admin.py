from django.contrib import admin
from .models import DicasCategoria, Dica, NoticiasCategoria, Noticia, Associado, Memoria

class _dica(admin.ModelAdmin):
    Model        = Dica
    list_display = ['dthora', 'titulo']
    list_filter  = ['dthora', 'titulo']

class _noticia(admin.ModelAdmin):
    Model        = Noticia
    list_display = ['dthora', 'titulo']
    list_filter  = ['dthora', 'titulo']

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
))