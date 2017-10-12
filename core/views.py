from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader, RequestContext
from .models import Index, QuemSomos, NossaHistoria, Memoria, Associado, Dica, DicasCategoria, Noticia, NoticiasCategoria, Contato, Contribuir, ContribuirItem

# Create your views here.
def index(request):
    try:
        reg = Index.objects.latest('id')
    except Index.DoesNotExist:
        reg = None

    try:
        itens = Noticia.objects.order_by('-dt_hora')[:5]
    except Noticia.DoesNotExist:
        itens = None

    context = {'reg': reg,
               'itens': itens}
    return render(request, 'index.html', context)

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
        itens = Memoria.objects.order_by('-data')
    except Memoria.DoesNotExist:
        itens = None

    context = {'itens': itens}
    return render(request, 'memorias.html', context)

def associados(request):
    try:
        itens = Associado.objects.order_by('nome')
    except Associado.DoesNotExist:
        itens = None

    context = {'itens': itens}
    return render(request, 'associados.html', context)

def dicas(request):
    try:
        cat = DicasCategoria.objects.order_by('nome')
    except DicasCategoria.DoesNotExist:
        cat = None

    try:
        itens = Dica.objects.order_by('-dt_hora')
    except Dica.DoesNotExist:
        itens = None

    context = {'cat': cat,
               'itens': itens}
    return render(request, 'dicas.html', context)

def dica(request, id):
    try:
        reg = Dica.objects.get(pk = id)
    except Dica.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'dica.html', context)

def noticias(request):
    try:
        cat = NoticiasCategoria.objects.order_by('nome')
    except NoticiasCategoria.DoesNotExist:
        cat = None

    try:
        itens = Noticia.objects.order_by('-dt_hora')
    except Noticia.DoesNotExist:
        itens = None

    context = {'cat': cat,
               'itens': itens}
    return render(request, 'noticias.html', context)

def noticia(request, id):
    try:
        reg = Noticia.objects.get(pk = id)
    except Noticia.DoesNotExist:
        reg = None

    context = {'reg': reg}
    return render(request, 'noticia.html', context)

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