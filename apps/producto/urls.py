from django.urls import path

from .views import home, ingresar_productos


app_name = "producto"

urlpatterns = [
    path("", home, name="home"),
    path("ingresar_productos/", ingresar_productos, name="ingresar_productos"),

]