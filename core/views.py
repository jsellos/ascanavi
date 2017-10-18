from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader, RequestContext
from .models import Index, QuemSomos, NossaHistoria, Memoria, Associado, Dica, DicasCategoria, Noticia, \
    NoticiasCategoria, Contato, Contribuir, ContribuirItem

# Create your views here.


def index(request):
    reg = Index.objects.latest('id')
    itens = Noticia.objects.order_by('-dt_hora')[:5]
    context = {'reg': reg,
               'itens': itens}

    return render(request, 'index.html', context)


def quemsomos(request):
    reg = QuemSomos.objects.latest('id')
    context = {'reg': reg}

    return render(request, 'quem-somos.html', context)


def nossahistoria(request):
    reg = NossaHistoria.objects.latest('id')
    context = {'reg': reg}

    return render(request, 'nossa-historia.html', context)


def memorias(request):
    itens = Memoria.objects.order_by('-data')
    context = {'itens': itens}

    return render(request, 'memorias.html', context)


def associados(request):
    itens = Associado.objects.order_by('nome')
    context = {'itens': itens}

    return render(request, 'associados.html', context)


def dicas(request):
    cat = DicasCategoria.objects.order_by('nome')
    itens = Dica.objects.order_by('-dt_hora')
    context = {'cat': cat,
               'itens': itens}

    return render(request, 'dicas.html', context)


def dica(request, id):
    reg = Dica.objects.get(pk=id)
    context = {'reg': reg}

    return render(request, 'dica.html', context)


def noticias(request):
    cat = NoticiasCategoria.objects.order_by('nome')
    itens = Noticia.objects.order_by('-dt_hora')

    context = {'cat': cat,
               'itens': itens}
    return render(request, 'noticias.html', context)


def noticia(request, id):
    reg = Noticia.objects.get(pk=id)
    context = {'reg': reg}

    return render(request, 'noticia.html', context)


def contato(request):
    reg = Contato.objects.latest('id')
    context = {'reg': reg}

    return render(request, 'contato.html', context)


def contribuir(request):
    reg = Contribuir.objects.latest('id')
    itens = ContribuirItem.objects.order_by('-id')
    context = {'reg': reg,
               'itens': itens}

    return render(request, 'contribuir.html', context)