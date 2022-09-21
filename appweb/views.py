from django.shortcuts import render, HttpResponse
from servicios.models import servicio

# Create your views here.

def home (request):
    return render(request,"appweb/home.html")


def tienda (request):
    return render(request,"appweb/tienda.html")



def contacto (request):
    return render(request,"appweb/contacto.html")

