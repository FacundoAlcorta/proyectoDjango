from django.shortcuts import render
from tienda.models import Producto

# Create your views here.

def tienda(request):
    productos = Producto.objects.all()
    return render(request,"tienda/tienda.html",{"productos": productos})


def producto(request,producto_id):
    producto = Producto.objects.filter(id = producto_id).first
    return render(request,"tienda/producto.html",{"producto":producto})

