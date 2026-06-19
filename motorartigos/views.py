from django.shortcuts import render
from motorartigos.models import Autor

def index(request):
    """autores = {
        1: {'nome': "Marcos",
            'biografia': "Game Designer",
            'email': "mvsantos@email.com"},

        2: {'nome': "Kesia",
            'biografia': "Pintora",
            'email': "kesia@email.com"},

        3: {'nome': "Samantha",
            'biografia': 'Filha de Marcos e Kesia',
            'email': "samantha@email.com"},
            }
    """
    autores = Autor.objects.all()
    
    return render(request,'motorartigos/index.html', {"autores":autores})


def artigo(request):
    return render(request, 'motorartigos/artigo.html')