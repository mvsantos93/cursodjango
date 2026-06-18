from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'motorartigos/index.html')

def artigo(request):
    return render(request, 'motorartigos/artigo.html')