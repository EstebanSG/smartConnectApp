from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hola mundo</h1>")
    return render(request, "index.html", {})

def inicio_view(request, *args, **kwargs):
    return render(request, "inicio.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def registrarse_view(request, *args, **kwargs):
    return render(request, "newaccount.html", {})

def perfil_view(request, *args, **kwargs):
    return render(request, "perfil.html", {})

def editarperfil_view(request, *args, **kwargs):
    return render(request, "editperfil.html", {})

def logaout_view(request, *args, **kwargs):
    return render(request, "index.html", {})
