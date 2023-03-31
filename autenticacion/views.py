from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout, authenticate
from django.contrib import messages
# Create your views here.


class UserLogin(View):
    def get(self,request):
        form = UserCreationForm()
        return render(request,"autenticacion/register.html",{"form":form})

    def post(self,request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("Home")
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
            return render(request,"autenticacion/register.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    return redirect("Home")

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
              login(request, user)
              return redirect('Home')
            else:
                messages.error(request,"usuario no valido")
        else:
                messages.error(request,"informacion incorrecta")
    form = AuthenticationForm()
    return render(request,"login/login.html",{"form":form})



