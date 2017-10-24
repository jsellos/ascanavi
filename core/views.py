from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader, RequestContext
from .models import Index, QuemSomos, NossaHistoria, Memoria, Associado, Dica, DicasCategoria, Noticia, \
    NoticiasCategoria, Contato, Contribuir, ContribuirItem, LinkUtil

def index(request):
    reg     = Index.objects.latest('id')
    itens   = Noticia.objects.order_by('-dt_hora')[:5]
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'reg': reg,
               'itens': itens,
               'contato': contato,
               'links': links}

    return render(request, 'index.html', context)


def quemsomos(request):
    reg     = QuemSomos.objects.latest('id')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'reg': reg,
               'contato': contato,
               'links': links}

    return render(request, 'quem-somos.html', context)


def nossahistoria(request):
    reg     = NossaHistoria.objects.latest('id')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'reg': reg,
               'contato': contato,
               'links': links}

    return render(request, 'nossa-historia.html', context)


def memorias(request):
    itens   = Memoria.objects.order_by('-data')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'itens': itens,
               'contato': contato,
               'links': links}

    return render(request, 'memorias.html', context)


def associados(request):
    itens   = Associado.objects.order_by('nome')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'itens': itens,
               'contato': contato,
               'links': links}

    return render(request, 'associados.html', context)


def dicas(request):
    cat     = DicasCategoria.objects.order_by('nome')
    itens   = Dica.objects.order_by('-dt_hora')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'cat': cat,
               'itens': itens,
               'contato': contato,
               'links': links}

    return render(request, 'dicas.html', context)


def dica(request, id):
    reg     = Dica.objects.get(pk=id)
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'reg': reg,
               'contato': contato,
               'links': links}

    return render(request, 'dica.html', context)


def noticias(request):
    cat     = NoticiasCategoria.objects.order_by('nome')
    itens   = Noticia.objects.order_by('-dt_hora')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'cat': cat,
               'itens': itens,
               'contato': contato,
               'links': links}

    return render(request, 'noticias.html', context)


def noticia(request, id):
    reg     = Noticia.objects.get(pk=id)
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'reg': reg,
               'contato': contato,
               'links': links}

    return render(request, 'noticia.html', context)


def contato(request):
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'contato': contato,
               'links': links}

    return render(request, 'contato.html', context)


def contribuir(request):
    reg     = Contribuir.objects.latest('id')
    itens   = ContribuirItem.objects.order_by('-id')
    contato = Contato.objects.latest('id')
    links   = LinkUtil.objects.order_by('descricao')

    context = {'reg': reg,
               'itens': itens,
               'contato': contato,
               'links': links}

    return render(request, 'contribuir.html', context)