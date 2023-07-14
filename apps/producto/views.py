from django.shortcuts import render

def home(request):
    contexto = {"app": "Producto"}
    return render(request, "producto/index.html", contexto)
