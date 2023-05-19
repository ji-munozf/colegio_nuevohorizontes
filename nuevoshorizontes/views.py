from django.shortcuts import render
from .models import Sede, Noticias
from .forms import *

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
    lista_noticias = Noticias.objects.all()
    
    return render(request, 'nuevoshorizontes/noticias.html',
        {'lista_noticias': lista_noticias})

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

def agregar_asignaturas(request):

    data = {
        'form': AsignaturaForm()
    }

    if request.method == 'POST':
        formulario = AsignaturaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_asignaturas.html', data)

def agregar_cursos(request):

    data = {
        'form': CursoForm()
    }

    if request.method == 'POST':
        formulario = CursoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_cursos.html', data)

def agregar_noticias(request):

    data = {
        'form': NoticiaForm()
    }

    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_noticias.html', data)

def agregar_salas(request):

    data = {
        'form': SalaForm()
    }

    if request.method == 'POST':
        formulario = SalaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_salas.html', data)

def agregar_sedes(request):

    data = {
        'form': SedeForm()
    }

    if request.method == 'POST':
        formulario = SedeForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_sedes.html', data)