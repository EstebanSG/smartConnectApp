from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
from django.core.paginator import Paginator

# Create your views here.

def index_view(request):
    obj = Convocatorias.objects.all()
    paginator = Paginator(obj, 10)

    page = request.GET.get('page')
    convlist = paginator.get_page(page)
    context = {

        'convlist': convlist
    }
    return render(request, "inicio.html", context)

def search_view(request):

    return render(request, "search.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def registrarse_view(request):
    if request.method =='POST':
        form = RegistroForm(request.POST)
        
        if form.is_valid(): 
            form.save()
            return redirect('login')
        else:
            
            form = RegistroForm()
         
            
            args = {
                'form': form
                }
            return render(request, 'newaccount.html', args)
   
    else:
        form = RegistroForm()
        args = {'form': form}

    return render(request, 'newaccount.html',args)
    

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

    return render(request,'logout.html')

def eliminarConvocatoriaCliente(request, pk=None):
    if pk:
        convocatoria = Convocatorias.objects.get(pk=pk)
    
        #user = User.objects.get(pku=pku)  
        #context = {'eventosss':eventosss}
    request.user.alumnos.convocatorias.delete(convocatoria.id)
    print("-----------------------ESTA COSITA-----------------------------")
   
    print("-----------------------ESTA COSITA-----------------------------")
    
    

        
        
        #User.empresa.add(eventosss)
        #User.clientes.save()

    return render(request, 'convsaved.html')

def misconvocatorias_view(request,):
    
    return render(request, 'convsaved.html')

def agregarConvocatoriaCliente(request, pk=None):
    if pk:
        convocatoria = Convocatorias.objects.get(pk=pk)
    
        #user = User.objects.get(pku=pku)  
        #context = {'eventosss':eventosss}
    request.user.alumnos.convocatorias.add(convocatoria.id)
    print("-----------------------ESTA COSITA1-----------------------------")
   
    print("-----------------------ESTA COSITA1-----------------------------")
    
    

        
        
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
    
