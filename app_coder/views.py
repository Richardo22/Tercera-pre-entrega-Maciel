from django.http import HttpResponse
from django.shortcuts import render
from .models import Empanada

# Create your views here.
def crea_producto(req, nombre, ingredientes, precio):
    nuevo_producto = Empanada(nombre=nombre, ingredientes=ingredientes, precio=precio)
    nuevo_producto.save()
    return HttpResponse(f"""
          <p>Producto: {nuevo_producto.nombre} - {nuevo_producto.ingredientes} - {nuevo_producto.precio} creado con exito </p>
""")
def lista_productos(req):
    lista=Empanada.objects.all()

    return render(req, 'lista_empanadas.html', {'empanadas': lista})
def inicio(req):
    return HttpResponse("Vista de Inicio")
def empanada(req):
    return HttpResponse("Vista de Empanadas")
def hamburguesa(req):
    return HttpResponse("Vista de Hamburguesa")
def pizza(req):
    return HttpResponse("Vista de Pizza")