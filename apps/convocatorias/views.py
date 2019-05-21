from django.http import HttpResponse
from django.shortcuts import render
from .models import Convocatorias
from .forms import ConvocatoriaForm

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

def perfil_view(request, *args, **kwargs):
    return render(request, "perfil.html", {})

def editarperfil_view(request, *args, **kwargs):
    return render(request, "editperfil.html", {})

def logaout_view(request, *args, **kwargs):
    return render(request, "index.html", {})

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
    
