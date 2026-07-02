from django.shortcuts import render
from motorartigos.models import Autor, Artigo, EixoTecnologia
from django.shortcuts import render, get_object_or_404

def index(request):
    autores = Autor.objects.all()
    artigos = Artigo.objects.filter(publicada=True)
    eixos = EixoTecnologia.objects.all()

    eixo = request.GET.get('eixo')

    if eixo: artigos = artigos.filter(id_fk_eixo_id=eixo)
   
    return render(request,'motorartigos/index.html', {
        'artigos': artigos, 'artigos_recentes': Artigo.objects.filter(publicada=True)[:4], 'eixos': eixos, 'eixo_selecionado': eixo})

def artigo(request, id):
    artigo = get_object_or_404(Artigo, id=id, publicada=True)
    return render(request, 'motorartigos/artigo.html', {'artigo': artigo})