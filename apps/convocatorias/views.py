from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import *
from django import *
from django import forms
from .forms import *
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import get_template

# Create your views here.
def index_view(request):
    obj = Convocatorias.objects.all()
    context = {
        'conv': obj
    }
    return render(request, "index.html", context)

def inicio_view(request):
    obj = Convocatorias.objects.all()
    form = ConvocatoriaForm(request.POST or None)
    context = {
        'conv': obj
    }
    return render(request, "index.html", context)

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def registrarse_view(request, *args, **kwargs):
    return render(request, "newaccount.html", {})

def perfil_view(request, pk=None):
    if pk:
        datosUser = User.objects.get(pk=pk)
    else:
        datosUser = request.user
    context = {
        'user': datosUser
        }
    return render(request, "perfil.html", context)

def editarperfil_view(request, pk=None):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = AlumnosForm(request.POST, instance=request.user.alumnos)

        if form.is_valid() or profile_form.is_valid():
         
            form.save()
            profile_form.save()
            if pk:
                datosUser = User.objects.get(pk=pk)
            else:
                datosUser = request.user
            context = {
                'user': datosUser
                }
            return render(request, 'perfil.html', context)
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = AlumnosForm(instance=request.user.alumnos)
        args = {'form': form,'profile_form':profile_form}
        return render(request, 'editperfil.html', args)
    

def logout_view(request):
    conv_smarconnect= Convocatorias.objects.all()
    context = {
        'conv_smarconnect':conv_smarconnect
        }
    return render(request,'logout.html',context)

def eliminarConvocatoriaCliente(request, pk=None):
    return render(request, 'historial.html')


def agregarConvocatoriaCliente(request, pk=None):
    if pk:
        convocatoria = Convocatorias.objects.get(pk=pk)
    
        #user = User.objects.get(pku=pku)  
        #context = {'eventosss':eventosss}
    request.user.alumnos.convocatorias.add(convocatoria.id)
    print("-----------------------ESTA COSITA-----------------------------")
   
    print("-----------------------ESTA COSITA-----------------------------")
    
    

        
        
        #User.empresa.add(eventosss)
        #User.clientes.save()

    return render(request, 'convsaved.html')
    '''
    context = {
        'nombre': obj.nombre,
        'informacion': obj.informacion,
        'duracion': obj.duracion,
        'video': obj.video,
        'link': obj.link
    }
'''

''' print("-----------------------ESTA COSITA-----------------------------")
    print(request.user.clientes.eventos)
    print(evento.id)
    print("-----------------------ESTA COSITA-----------------------------")
    if pk:
        evento = Eventos.objects.get(pk=pk)
    print("-----------------------ESTA COSITA-----------------------------")
    print(request.user.alumnos.convocatorias)
    print(convocatorias.id)
    print("-----------------------ESTA COSITA-----------------------------")
        #user = User.objects.get(pku=pku)  
        #context = {'eventosss':eventosss}
    request.user.alumnos.convocatorias.remove(convocatoria.id)
    print("-----------------------ESTA COSITA-----------------------------")
    print(request.user.alumnos.convocatorias)
    print(convocatorias.id)
    print("-----------------------ESTA COSITA-----------------------------")
        
        
        #User.empresa.add(eventosss)
        #User.clientes.save()

    return render(request, 'historial.html')
    '''
    
