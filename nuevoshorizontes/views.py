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
            return redirect("home_alumno")
        except Alumno.DoesNotExist as e:
            messages.error(request, 'El correo electrónico o la contraseña no son correctos')

    return render(request, 'nuevoshorizontes/login_portales/login_alumno.html')

def login_docente(request):
    if request.method == 'POST':
        try:
            detalleDocente = Docente.objects.get(correo_docente = request.POST['email'], password = request.POST['password'])
            request.session['correo_docente'] = detalleDocente.correo_docente
            return redirect("home_docente")
        except Docente.DoesNotExist as e:
            messages.error(request, 'El correo electrónico o la contraseña no son correctos')

    return render(request, 'nuevoshorizontes/login_portales/login_docente.html')

def login_apoderado(request):
    if request.method == 'POST':
        try:
            detalleApoderado = Apoderado.objects.get(correo_apoderado = request.POST['email'], password = request.POST['password'])
            request.session['correo_apoderado'] = detalleApoderado.correo_apoderado
            return redirect("home_apoderado")
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

def cerrar_sesion_admin(request):
    try:
        del request.session['Correo']
    except:
        return redirect("home")
    
    return redirect("home") 

def cerrar_sesion_apoderado(request):
    try:
        del request.session['correo_apoderado']
    except:
        return redirect("home")
    
    return redirect("home")

def cerrar_sesion_alumno(request):
    try:
        del request.session['correo_alumno']
    except:
        return redirect("home")
    
    return redirect("home")

def cerrar_sesion_docente(request):
    try:
        del request.session['correo_docente']
    except:
        return redirect("home")
    
    return redirect("home")

def home_admin(request):
    correo_admin = request.session.get('Correo', None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_admin/home_admin.html', {'admin': admin})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")

def home_agregar(request):
    correo_admin = request.session.get('Correo', None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_admin/agregar.html', {'admin': admin})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")

def home_listado(request):
    correo_admin = request.session.get('Correo', None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_admin/listar.html', {'admin': admin})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")

def home_pagos(request):
    correo_admin = request.session.get('Correo', None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_admin/pagos.html', {'admin': admin})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")

def agregar_admins(request):

    data = {
        'form': AdminForm()
    }

    if request.method == 'POST':
        formulario = AdminForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_admins.html', data)

def agregar_alumnos(request):

    data = {
        'form': AlumnoForm()
    }

    if request.method == 'POST':
        formulario = AlumnoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_alumnos.html', data)

def agregar_docentes(request):

    data = {
        'form': DocenteForm()
    }

    if request.method == 'POST':
        formulario = DocenteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_docentes.html', data)

def agregar_apoderados(request):

    data = {
        'form': ApoderadoForm()
    }

    if request.method == 'POST':
        formulario = ApoderadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'nuevoshorizontes/portal_admin/formularios/agregar_apoderados.html', data)

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

def home_alumno(request):
    correo_alumno = request.session.get('correo_alumno', None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_alumno/home_alumno.html', {'alumno': alumno})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_alumno")
    
def miperfil_alumno(request):
    correo_alumno = request.session.get('correo_alumno', None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)
        return render(request, 'nuevoshorizontes/portal_alumno/miperfil.html', {'alumno': alumno})

    else:
        return redirect("login_alumno")
    
def guardar_perfil_alumno(request):
    if request.method == 'POST':
        correo_alumno = request.session.get('correo_alumno', None)
        if correo_alumno:
            alumno = Alumno.objects.get(correo_alumno=correo_alumno)
            alumno.nombre_alumno = request.POST.get('nombre')
            alumno.appaterno_alumno = request.POST.get('paterno')
            alumno.apmaterno_alumno = request.POST.get('materno')
            alumno.direccion_alumno = request.POST.get('direccion')
            alumno.telefono_alumno = request.POST.get('telefono')
            # Actualizar otros campos del modelo "Apoderado" según sea necesario
            alumno.save()  # Guardar los cambios en el modelo
            messages.success(request, "Los cambios se guardaron exitosamente.")
        else:
            messages.error(request, "No se pudo guardar los cambios. Por favor, intenta nuevamente.")

    return redirect('miperfil_alumno')

def notas_alumno(request):

    return render(request, 'nuevoshorizontes/portal_alumno/notas_alumno.html')

def horario_alumno(request):

    return render(request, 'nuevoshorizontes/portal_alumno/horario_alumno.html')

def home_apoderado(request):
    correo_apoderado = request.session.get('correo_apoderado', None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_apoderado/home_apoderado.html', {'apoderado': apoderado})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_apoderado")
    
def miperfil_apoderado(request):
    correo_apoderado = request.session.get('correo_apoderado', None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        return render(request, 'nuevoshorizontes/portal_apoderado/miperfil.html', {'apoderado': apoderado})

    else:
        return redirect("login_apoderado")
    
def guardar_perfil_apoderado(request):
    if request.method == 'POST':
        correo_apoderado = request.session.get('correo_apoderado', None)
        if correo_apoderado:
            apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
            apoderado.nombre_apoderado = request.POST.get('nombre')
            apoderado.appaterno_apoderado = request.POST.get('paterno')
            apoderado.apmaterno_apoderado = request.POST.get('materno')
            apoderado.direccion_apoderado = request.POST.get('direccion')
            apoderado.telefono_apoderado = request.POST.get('telefono')
            # Actualizar otros campos del modelo "Apoderado" según sea necesario
            apoderado.save()  # Guardar los cambios en el modelo
            messages.success(request, "Los cambios se guardaron exitosamente.")
        else:
            messages.error(request, "No se pudo guardar los cambios. Por favor, intenta nuevamente.")

    return redirect('miperfil_apoderado')

def lista_hijos(request):
    correo_apoderado = request.session.get('correo_apoderado', None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumnos = Alumno.objects.filter(apoderado_alumno=apoderado)
        return render(request, 'nuevoshorizontes/portal_apoderado/lista_hijos.html', {'apoderado': apoderado, 'alumnos': alumnos})

    else:
        return redirect("login_apoderado")
    
def horarios_apoderado(request):

    return render(request, 'nuevoshorizontes/portal_apoderado/horarios_apoderado.html')

def asistencias_apoderado(request):

    return render(request, 'nuevoshorizontes/portal_apoderado/asistencias_apoderado.html')

def notas_apoderado(request):

    return render(request, 'nuevoshorizontes/portal_apoderado/notas_apoderado.html')

def pagos_apoderado(request):

    return render(request, 'nuevoshorizontes/portal_apoderado/pagos_apoderado.html')

def home_docente(request):
    correo_docente = request.session.get('correo_docente', None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(request, 'nuevoshorizontes/portal_docente/home_docente.html', {'docente': docente})
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_docente")
    
def  miperfil_docente(request):
    correo_docente = request.session.get('correo_docente', None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        return render(request, 'nuevoshorizontes/portal_docente/miperfil.html', {'docente': docente})

    else:
        return redirect("login_docente")
    
def guardar_perfil_docente(request):
    if request.method == 'POST':
        correo_docente = request.session.get('correo_docente', None)
        if correo_docente:
            docente = Docente.objects.get(correo_docente=correo_docente)
            docente.nombre_docente = request.POST.get('nombre')
            docente.appaterno_docente = request.POST.get('paterno')
            docente.apmaterno_docente = request.POST.get('materno')
            docente.direccion_docente = request.POST.get('direccion')
            docente.telefono_docente = request.POST.get('telefono')
            # Actualizar otros campos del modelo "Apoderado" según sea necesario
            docente.save()  # Guardar los cambios en el modelo
            messages.success(request, "Los cambios se guardaron exitosamente.")
        else:
            messages.error(request, "No se pudo guardar los cambios. Por favor, intenta nuevamente.")

    return redirect('miperfil_docente')

def curso_docente(request):

    return render(request, 'nuevoshorizontes/portal_docente/curso_docente.html')

def asignaturas_docente(request):

    return render(request, 'nuevoshorizontes/portal_docente/asignaturas_docente.html')