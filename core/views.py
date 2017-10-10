from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader, RequestContext
from .models import QuemSomos, NossaHistoria, Memoria, Associado, Dica, DicasCategoria, Noticia, NoticiasCategoria, Contato, Contribuir, ContribuirItem

# Create your views here.
def index(request):
    return render(request, 'index.html')

def quemsomos(request):
    try:
        reg = QuemSomos.objects.latest('id')
    except QuemSomos.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'quem-somos.html', context)

def nossahistoria(request):
    try:
        reg = NossaHistoria.objects.latest('id')
    except NossaHistoria.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'nossa-historia.html', context)

def memorias(request):
    try:
        reg = Memoria.objects.latest('id')
    except Memoria.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'memorias.html', context)

def associados(request):
    try:
        reg = Associado.objects.latest('id')
    except Associado.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'associados.html', context)

def dicas(request):
    try:
        cat = DicasCategoria.objects.order_by('nome')
    except DicasCategoria.DoesNotExist:
        cat = None

    try:
        itens = Dica.objects.order_by('-id')
    except Dica.DoesNotExist:
        itens = None

    context = {'cat': cat,
               'itens': itens}
    return render(request, 'dicas.html', context)

def noticias(request):
    try:
        reg = Noticia.objects.latest('id')
    except Noticia.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'noticias.html', context)

def contato(request):
    try:
        reg = Contato.objects.latest('id')
    except Contato.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'contato.html', context)

def contribuir(request):
    try:
        reg   = Contribuir.objects.latest('id')
    except Contribuir.DoesNotExist:
        reg = None

    try:
        itens = ContribuirItem.objects.order_by('-id')
    except ContribuirItem.DoesNotExist:
        itens = None

    context = {'reg': reg,
               'itens': itens}
    return render(request, 'contribuir.html', context)

#faltou a dica (item)
#faltou a notícia (item)