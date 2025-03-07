from django.shortcuts import redirect
from .models import Pedido,LineaPedido
from carro.carro import Carro
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key,value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user = request.user,
            pedidos = pedido
        ))
    LineaPedido.objects.bulk_create(lineas_pedido)
    messages.success(request,"el pedido se realizo correctamente")
    return redirect("../tienda")
