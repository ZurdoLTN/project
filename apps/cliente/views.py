from django.shortcuts import render
from django import http

from .forms import ClienteForm

from .models import Cliente, Pais




def home(request):
    clientes_registros = Cliente.objects.all()
    context = {"cliente": clientes_registros}
    return render(request, "cliente/index.html", context)

