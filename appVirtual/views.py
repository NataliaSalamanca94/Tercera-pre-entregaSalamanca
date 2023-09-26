from django.shortcuts import render, redirect
from .forms import ClienteForm, ArticuloForm, TiendaForm
from .models import Cliente, Articulo, Tienda

def inicio(request):
    return render(request, 'inicio.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ClienteForm()
    return render(request, 'crear_cliente.html', {'form': form})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ArticuloForm()
    return render(request, 'crear_articulo.html', {'form': form})

def crear_tienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = TiendaForm()
    return render(request, 'crear_tienda.html', {'form': form})


def consultar_base_datos(request):
    clientes = Cliente.objects.all()
    articulos = Articulo.objects.all()
    tiendas = Tienda.objects.all()
    return render(request, 'consultar_base_datos.html', {
        'clientes': clientes,
        'articulos': articulos,
        'tiendas': tiendas,
    })