from django.conf.urls import url
from .views import index, quemsomos, nossahistoria, memorias, associados, dicas, noticias, contato, contribuir

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^quem-somos$', quemsomos, name='quem-somos'),
    url(r'^nossa-historia$', nossahistoria, name='nossa-historia'),
    url(r'^memorias', memorias, name='memorias'),
    url(r'^associados$', associados, name='associados'),
    url(r'^dicas$', dicas, name='dicas'),
    url(r'^noticias$', noticias, name='noticias'),
    url(r'^contato$', contato, name='contato'),
    url(r'^contribuir$', contribuir, name='contribuir'),
]