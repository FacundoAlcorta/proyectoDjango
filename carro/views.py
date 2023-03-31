from django.shortcuts import render
from django.shortcuts import redirect

from .carro import Carro

from tienda.models import Producto
# Create your views here.

def carro(request):
    carro = Carro(request)
    return render(request,"carro/carro.html",{"carro":carro})

def agregar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)  
    if producto:
        carro.agregar(producto=producto)
    return redirect("/carro")

def eliminar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)  
    if producto:
        carro.eliminar(producto=producto)   
    return redirect("/carro")

def restar_producto(request,producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)  
    if producto:
        carro.restar_producto(producto=producto)   
    return redirect("/carro")


def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("/carro")


