from django.urls import path
from app_coder.views import *

urlpatterns = [
    path('agregar-producto/<nombre>/<ingredientes>/<precio>', crea_producto),
    path('lista_empanadas/', lista_productos),   
    path('',inicio),  
    path('empanada/',empanada, name='empanada'),
    path('pizza/',pizza, name='pizza'),
    path('hamburguesa/',hamburguesa, name='hamburguesa'),
    path('empanada-formulario/',empanada_formulario, name='EmpanadaFormulario'),

]
