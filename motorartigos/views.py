from django.shortcuts import render
from motorartigos.models import Autor, Artigo

def index(request):
    autores = Autor.objects.all()
    artigos = Artigo.objects.filter(publicada=True)
   
    return render(request,'motorartigos/index.html', {'artigos': artigos})

def artigo(request):
    return render(request,'motorartigos/artigo.html')