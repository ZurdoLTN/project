from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .forms import ClienteForm

from .models import Cliente, Pais




def home(request):
    clientes_registros = Cliente.objects.all()
    return render(request, "cliente/index.html", {"cliente": clientes_registros})

def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:
        form = ClienteForm()
    return render(request, "cliente/crear_cliente.html", {"form": form})
    

