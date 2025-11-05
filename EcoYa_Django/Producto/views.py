from django.shortcuts import render, HttpResponse
from urllib import request
from .models import Producto

# Create your views here.

def Create_producto(request):
    pass

def Get_producto(request, id):
    pass    

def GetAll_producto(request):
    productos = Producto.objects.all()
    context = {"nombre": "Pan",
               "cantidad": 10,
               'productos': productos
               }
    return render(request, 'get_all.html', context)


def Update_producto(request):
    pass    

def Delete_producto(request):
    pass




