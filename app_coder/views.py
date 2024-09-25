from django.http import HttpResponse
from django.shortcuts import render
from .models import *


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
def crea_producto(req, nombre, ingredientes, precio):
    nueva_hamburguesa = Hamburguesa(nombre=nombre, ingredientes=ingredientes, precio=precio)
    nueva_hamburguesa.save()
    return HttpResponse(f"""
          <p>Producto: {nueva_hamburguesa.nombre} - {nueva_hamburguesa.ingredientes} - {nueva_hamburguesa.precio} creado con exito </p>
""")
def lista_hamburguesa(req):
    lista=hamburguesa.objects.all()
    return render(req, 'lista_hamburguesa.html', {'hamburguesa': lista})
def inicio(req):
    return render(req, 'inicio.html', {})
def empanada(req):
    return render(req, 'empanada.html', {})
def hamburguesa(req):
    return render(req, 'hamburguesa.html', {})
def pizza(req):
    return render(req, 'pizza.html', {})
def empanada_formulario(req):
    print ('method',req.method)
    print('data',req.POST)
    if req.method == 'POST':
        nombre = req.POST.get('nombre','').strip() 
        ingredientes = req.POST.get('ingredientes','').strip()
        precio = req.POST.get('precio', '').strip()
        print('Nombre recibido:', nombre)
        try:
            precio=float(precio)
            if precio<0:
                precio=0
        except ValueError:
            precio=0
        nuevo_producto=Empanada(nombre=nombre,ingredientes=ingredientes,precio=precio)
        nuevo_producto.save()
        return render(req, 'inicio.html', {})
    else:
        return render(req, 'empanada_formulario.html', {})
def hamburguesa_formulario(req):
    print ('method',req.method)
    print('data',req.POST)
    if req.method == 'POST':
        nombre = req.POST.get('nombre','').strip() 
        ingredientes = req.POST.get('ingredientes','').strip()
        precio = req.POST.get('precio', '').strip()
        print('Nombre recibido:', nombre)
        try:
          precio=float(precio)
          if precio<0:
              precio=0
        except ValueError:
            precio=0
        nueva_hamburguesa = Hamburguesa(nombre=nombre, ingredientes=ingredientes, precio=precio)
        nueva_hamburguesa.save()
        return render(req, 'inicio.html', {})
    else:
      return render(req, 'hamburguesa_formulario.html', {})

    





    