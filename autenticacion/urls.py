from django.urls import path
from . import views
from .views import UserLogin , cerrar_sesion, logear

urlpatterns = [
    path('',UserLogin.as_view(), name="autenticacion"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('logear/', logear, name="logear"),
    
]
