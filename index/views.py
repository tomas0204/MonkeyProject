from django.shortcuts import render
from .models import Pelicula


def hello(request):
    return render(request, 'index.html')

def movie(request):
    if 'q' in request.GET:
        query = request.GET['q']
        resultados = Pelicula.objects.filter(titulo__icontains=query)
        return render(request, 'result.html', {'resultados': resultados, 'query': query})
    else:
        return render(request, "index.html")