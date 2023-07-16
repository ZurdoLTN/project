from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Producto
from django.http import HttpRequest, HttpResponse

from .forms import ProductoForm

def home(request):
    productos_registrados = Producto.objects.all()
    return render(request, "producto/index.html", {"producto": productos_registrados})

# Formulario para ingresar productos

def ingresar_productos(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:home")
    else:
        form = ProductoForm()
    return render(request, "producto/ingresar_productos.html", {"form": form})
        
   




