from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from urllib import request
from .models import Producto


# Create your views here.

def Create_producto(request):
    pass

def Get_producto(request, id):
    print(id)
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'get_id.html', {"producto": producto})

def GetAll_producto(request):
    productos = Producto.objects.all()
    context = {"nombre": "Pan",
               "cantidad": 10,
               'productos': productos
               }
    return render(request, 'get_all.html', context)


def Update_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.cantidad = request.POST.get('cantidad')
        producto.descripcion = request.POST.get('descripcion')
        producto.save()
        return redirect('obtener_producto', id=producto.id)
    
    else:
        context = {'producto': producto}
        return render(request, 'update.html', context)        
    

def Delete_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('getall_producto')
    return render(request, 'producto/delete.html', {'producto': producto})
    




