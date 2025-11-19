from django.shortcuts import render, HttpResponse
from urllib import request

# Create your views here.
def app_cosillas(request):
    #return HttpResponse("<h1>Vista de producto</h1>")
    return  render(request, 'inicio.html')

def inicio(request):
    return render(request, 'inicio.html')

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def mapa(request):
    return render(request, "mapa.html")

def puntos(request):
    return render(request, "puntos.html")

def contacto(request):
    return render(request, "contacto.html")