from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('agregar-producto/<nombre>/<ingredientes>/<precio>', crea_producto),
    path('lista_empanadas/', lista_productos),     
    path('',inicio),
    path('empanada/',empanada),
    path('pizza/',pizza),
    path('hamburguesa/',hamburguesa),

]
