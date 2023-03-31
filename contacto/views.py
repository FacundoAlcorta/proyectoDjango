from django.shortcuts import render,redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    if (request.method == "POST"):
        formulario = formularioContacto(data=request.POST)
        if (formulario.is_valid()):
            ##se puede enviar la info del formulario a un correo electronico
            """
            nombre = request.POST("nombre")
            email = request.POST("email")
            contenido = request.POST("contenido")
            email = EmailMessage(
                "Mensaje para contacto",
                "Nombre de usuario {} ({}) , mensaje:\n {}".format(nombre,email,contenido),
                "",["               "],reply_to=[email]
            )      
            """
            try:
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    else:
        formulario = formularioContacto()
    return render(request,"contacto/contacto.html",{"formulario":formulario})