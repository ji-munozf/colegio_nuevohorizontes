from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sede, Noticias, Alumno, Docente, Apoderado, Administrador
from .forms import *
from datetime import date

# Create your views here.

def home(request):
    
    return render(request, 'nuevoshorizontes/home.html')

def nosotros(request):
    
    return render(request, 'nuevoshorizontes/nosotros.html')

def portales(request):

    return render(request, 'nuevoshorizontes/portales.html')

def sedes(request):
    lista_sedes = Sede.objects.all()
    
    return render(request, 'nuevoshorizontes/sedes.html', {'lista_sedes': lista_sedes})

def noticias(request):
    fecha_actual = date.today()
    noticias = Noticias.objects.filter(fecha_publi__year=fecha_actual.year, fecha_publi__month=fecha_actual.month)
    
    return render(request, 'nuevoshorizontes/noticias.html', {'noticias':noticias})

def login_alumno(request):
    if request.method == 'POST':
        try:
            detalleAlumno = Alumno.objects.get(correo_alumno = request.POST['email'], password = request.POST['password'])
            request.session['correo_alumno'] = detalleAlumno.correo_alumno
            return redirect("home")
        except Alumno.DoesNotExist as e:
            messages.error(request, 'El correo electrónico o la contraseña no son correctos')

    return render(request, 'nuevoshorizontes/login_portales/login_alumno.html')

def login_docente(request):
    if request.method == 'POST':
        try:
            detalleDocente = Docente.objects.get(correo_docente = request.POST['email'], password = request.POST['password'])
            request.session['correo_docente'] = detalleDocente.correo_docente
            return redirect("home")
        except Docente.DoesNotExist as e:
            messages.error(request, 'El correo electrónico o la contraseña no son correctos')

    return render(request, 'nuevoshorizontes/login_portales/login_docente.html')

def login_apoderado(request):
    if request.method == 'POST':
        try:
            detalleApoderado = Apoderado.objects.get(correo_apoderado = request.POST['email'], password = request.POST['password'])
            request.session['correo_apoderado'] = detalleApoderado.correo_apoderado
            return redirect("home")
        except Apoderado.DoesNotExist as e:
            messages.error(request, 'El correo electrónico o la contraseña no son correctos')

    return render(request, 'nuevoshorizontes/login_portales/login_apoderado.html')

def login_administrativo(request):
    if request.method == 'POST':
        try:
            detalleAdmin = Administrador.objects.get(correo_admin = request.POST['email'], password = request.POST['password'])
            request.session['Correo'] = detalleAdmin.correo_admin
            return redirect("home_admin")
        except Administrador.DoesNotExist as e:
            messages.success(request, 'El correo electrónico o la contraseña no son correctos')

    return render(request, 'nuevoshorizontes/login_portales/login_administrativo.html')

def cerrar_sesion(request):
    try:
        del request.session['Correo']
    except:
        return redirect("home")
    
    return redirect("home")   

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