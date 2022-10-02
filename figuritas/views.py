

from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from numpy import NaN
from . import forms
from .models import figus_totales, tipos_figus

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else: 
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('figuritas')
            except:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    'error': 'Usuario existente'
                })
        else:
            return render(request, 'signup.html',{
                'form' : UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })

@login_required
def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:

            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': "El usuario o contraseña es incorrecto"
            })
        else:
            login(request, user)
            return redirect('verFigus')
        
    
@login_required
def figurita(request):
    
    if request.method == 'GET':
        return render(request, 'figus.html',{
            'form': forms.agregarFigurita
        })
    else:
    
        numero = request.POST['num_figu']
        tipo1 = request.POST['type']
       
        tipo = tipos_figus.objects.get(id=tipo1)
       
        if str(tipo) == "FWC" and int(numero)>30:
            
            return render(request, 'figus.html',{
                'form': forms.agregarFigurita,
                'error': 'Esa figurita no existe'
            })


        if str(tipo) == "COCA" and int(numero)>8:
            
            return render(request, 'figus.html',{
                'form': forms.agregarFigurita,
                'error': 'Esa figurita no existe'
            })
            
        
        if str(tipo) != 'FWC' and (int(numero)<=0 or int(numero)>20):
            return render(request, 'figus.html',{
                'form': forms.agregarFigurita,
                'error': 'Esa figurita no existe'
            })

        
        
        try:
        
            figus_totales.objects.create(num_figu = numero, type=tipo, figurita = str(tipo)+numero, user = request.user)
        except IntegrityError:
            return render(request, 'figus.html',{
                'form': forms.agregarFigurita,
                'error': "Figurita repetida"
            })
        
        return redirect('verFigus')
       
        
        
 

@login_required 
def delete_figus(request, figu):
    figus = get_object_or_404(figus_totales, figurita=figu)
    if request.method == 'POST':
        figus.delete()
        return redirect('verFigus')

def home(request):
    return render(request, 'home.html')

def buscador(request):
    busqueda = request.GET.get('buscar')
    figuritas = figus_totales.objects.all()

    if busqueda:
        figuritas = figus_totales.objects.filter(
            figurita__icontains=busqueda
        ).distinct()
    
    return render(request, 'verFigus.html', {
        'figus': figuritas
    })

@login_required
def verFigus(request):
    busqueda = request.GET.get('buscar')
    figuritas = figus_totales.objects.filter(user = request.user)
   
    cantidad = figus_totales.objects.filter(user = request.user).count()
    porcentaje = (cantidad * 100)/638
    
    
    if busqueda:
        figuritas = figus_totales.objects.filter(
            figurita__icontains=busqueda
        ).distinct().order_by()
  
    

    return render(request, 'verFigus.html',{
        'figus': figuritas,
        'porcentaje': porcentaje.__round__,
        'cantidad': cantidad,
        'form': forms.filtrarFigurita
    })           
        