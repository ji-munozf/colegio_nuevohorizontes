from django.shortcuts import render
from .models import Sede


# Create your views here.

def home(request):
    
    return render(request, 'nuevoshorizontes/home.html')

def nosotros(request):
    
    return render(request, 'nuevoshorizontes/nosotros.html')

def sedes(request):
    lista_sedes = Sede.objects.all()
    
    return render(request, 'nuevoshorizontes/sedes.html',
        {'lista_sedes': lista_sedes})

def noticias(request):
    
    return render(request, 'nuevoshorizontes/noticias.html')

def login(request):
    
    return render(request, 'nuevoshorizontes/login.html')

def home_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/home_admin.html')

def asignaturas_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/asignaturas.html')

def cursos_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/cursos.html')

def noticias_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/noticias.html')

def salas_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/salas.html')

def sedes_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/sedes.html')

def usuarios_admin(request):

    return render(request, 'nuevoshorizontes/portal_admin/usuarios.html')