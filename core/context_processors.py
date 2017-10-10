def contato(request):
    from core.models import Contato

    try:
        contato = Contato.objects.latest('id')

    except Contato.DoesNotExist:
        contato = None

    return {
        'contato': contato,
    }