from django.shortcuts import render
from motorartigos.models import Autor

def index(request):
    autores = Autor.objects.all()
   
    return render(request,'motorartigos/index.html')

def artigo(request):
    return render(request,'motorartigos/artigo.html')