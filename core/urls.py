from django.conf.urls import url
from .views import index, quemsomos, nossahistoria, memorias, associados, dicas, dica, noticias, noticia, contato, contribuir

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^quem-somos$', quemsomos, name='quem-somos'),
    url(r'^nossa-historia$', nossahistoria, name='nossa-historia'),
    url(r'^memorias', memorias, name='memorias'),
    url(r'^associados$', associados, name='associados'),
    url(r'^dicas$', dicas, name='dicas'),
    url(r'^dicas/(?P<id>[0-9])$', dica, name='dica'),
    url(r'^noticias$', noticias, name='noticias'),
    url(r'^noticias/(?P<id>[0-9])$', noticia, name='noticia'),
    url(r'^contato$', contato, name='contato'),
    url(r'^contribuir$', contribuir, name='contribuir'),
]