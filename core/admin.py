from django.contrib import admin
from . import models


class _index(admin.ModelAdmin):
    Model = models.Index

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class _contribuir(admin.ModelAdmin):
    Model = models.Contribuir

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class _quemsomos(admin.ModelAdmin):
    Model = models.QuemSomos

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class _contato(admin.ModelAdmin):
    Model = models.Contato

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class _nossahistoria(admin.ModelAdmin):
    Model = models.NossaHistoria

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class _dica(admin.ModelAdmin):
    Model = models.Dica
    list_display = ['dt_hora', 'titulo']
    list_filter = ['dt_hora', 'titulo']


class _noticia(admin.ModelAdmin):
    Model = models.Noticia
    list_display = ['dt_hora', 'titulo']
    list_filter = ['dt_hora', 'titulo']


class _memoria(admin.ModelAdmin):
    Model = models.Memoria
    list_display = ['data', 'descricao']
    list_filter = ['data', 'descricao']


admin.site.register(models.Index, _index)
admin.site.register(models.Contribuir, _contribuir)
admin.site.register(models.QuemSomos, _quemsomos)
admin.site.register(models.Contato, _contato)
admin.site.register(models.NossaHistoria, _nossahistoria)
admin.site.register(models.Dica, _dica)
admin.site.register(models.Noticia, _noticia)
admin.site.register(models.Memoria, _memoria)
admin.site.register((
    models.DicasCategoria,
    models.NoticiasCategoria,
    models.Associado,
    models.LinkUtil,
    models.ContribuirItem,
))
