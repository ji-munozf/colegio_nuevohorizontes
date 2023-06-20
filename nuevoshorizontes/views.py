from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from datetime import date
from django.http import JsonResponse

# Create your views here.


def home(request):
    correo_admin = request.session.get("correo_admin", None)
    correo_alumno = request.session.get("correo_alumno", None)
    correo_apoderado = request.session.get("correo_apoderado", None)
    correo_docente = request.session.get("correo_docente", None)

    return render(
        request,
        "nuevoshorizontes/home.html",
        {
            "correo_admin": correo_admin,
            "correo_alumno": correo_alumno,
            "correo_apoderado": correo_apoderado,
            "correo_docente": correo_docente,
        },
    )


def nosotros(request):
    correo_admin = request.session.get("correo_admin", None)
    correo_alumno = request.session.get("correo_alumno", None)
    correo_apoderado = request.session.get("correo_apoderado", None)
    correo_docente = request.session.get("correo_docente", None)

    return render(
        request,
        "nuevoshorizontes/nosotros.html",
        {
            "correo_admin": correo_admin,
            "correo_alumno": correo_alumno,
            "correo_apoderado": correo_apoderado,
            "correo_docente": correo_docente,
        },
    )


def portales(request):
    correo_admin = request.session.get("correo_admin", None)
    correo_alumno = request.session.get("correo_alumno", None)
    correo_apoderado = request.session.get("correo_apoderado", None)
    correo_docente = request.session.get("correo_docente", None)

    return render(
        request,
        "nuevoshorizontes/portales.html",
        {
            "correo_admin": correo_admin,
            "correo_alumno": correo_alumno,
            "correo_apoderado": correo_apoderado,
            "correo_docente": correo_docente,
        },
    )


def sedes(request):
    correo_admin = request.session.get("correo_admin", None)
    correo_alumno = request.session.get("correo_alumno", None)
    correo_apoderado = request.session.get("correo_apoderado", None)
    correo_docente = request.session.get("correo_docente", None)

    lista_sedes = Sede.objects.all()

    return render(
        request,
        "nuevoshorizontes/sedes.html",
        {
            "correo_admin": correo_admin,
            "correo_alumno": correo_alumno,
            "correo_apoderado": correo_apoderado,
            "correo_docente": correo_docente,
            "lista_sedes": lista_sedes,
        },
    )


def registrar_contacto(request):
    nombres = request.POST["nombres"]
    apellidos = request.POST["apellidos"]
    correo = request.POST["correo"]
    telefono = request.POST["telefono"]
    sede_id = request.POST.get("sede")
    mensaje = request.POST["mensaje"]

    sede_obj = None
    if sede_id:
        try:
            sede_obj = Sede.objects.get(id=sede_id)
        except Sede.DoesNotExist:
            pass

    Postulaciones.objects.create(
        nombres=nombres,
        apellidos=apellidos,
        email=correo,
        telefono=telefono,
        sede=sede_obj,
        mensaje=mensaje,
    )

    messages.success(request, "Contacto enviado correctamente")

    return redirect("sedes")


def noticias(request):
    correo_admin = request.session.get("correo_admin", None)
    correo_alumno = request.session.get("correo_alumno", None)
    correo_apoderado = request.session.get("correo_apoderado", None)
    correo_docente = request.session.get("correo_docente", None)

    fecha_actual = date.today()
    noticias = Noticias.objects.filter(
        fecha_publi__year=fecha_actual.year, fecha_publi__month=fecha_actual.month
    )

    return render(
        request,
        "nuevoshorizontes/noticias.html",
        {
            "correo_admin": correo_admin,
            "correo_alumno": correo_alumno,
            "correo_apoderado": correo_apoderado,
            "correo_docente": correo_docente,
            "noticias": noticias,
        },
    )


def login_alumno(request):
    if request.method == "POST":
        try:
            detalleAlumno = Alumno.objects.get(
                correo_alumno=request.POST["email"], password=request.POST["password"]
            )
            request.session["correo_alumno"] = detalleAlumno.correo_alumno
            return redirect("home_alumno")
        except Alumno.DoesNotExist as e:
            messages.error(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_alumno.html")


def login_docente(request):
    if request.method == "POST":
        try:
            detalleDocente = Docente.objects.get(
                correo_docente=request.POST["email"], password=request.POST["password"]
            )
            request.session["correo_docente"] = detalleDocente.correo_docente
            return redirect("home_docente")
        except Docente.DoesNotExist as e:
            messages.error(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_docente.html")


def login_apoderado(request):
    if request.method == "POST":
        try:
            detalleApoderado = Apoderado.objects.get(
                correo_apoderado=request.POST["email"],
                password=request.POST["password"],
            )
            request.session["correo_apoderado"] = detalleApoderado.correo_apoderado
            return redirect("home_apoderado")
        except Apoderado.DoesNotExist as e:
            messages.error(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_apoderado.html")


def login_administrativo(request):
    if request.method == "POST":
        try:
            detalleAdmin = Administrador.objects.get(
                correo_admin=request.POST["email"], password=request.POST["password"]
            )
            request.session["correo_admin"] = detalleAdmin.correo_admin
            return redirect("home_admin")
        except Administrador.DoesNotExist as e:
            messages.success(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_administrativo.html")


def cerrar_sesion(request):
    if "correo_admin" in request.session:
        del request.session["correo_admin"]
    elif "correo_apoderado" in request.session:
        del request.session["correo_apoderado"]
    elif "correo_alumno" in request.session:
        del request.session["correo_alumno"]
    elif "correo_docente" in request.session:
        del request.session["correo_docente"]

    return redirect("home")


def home_admin(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request, "nuevoshorizontes/portal_admin/home_admin.html", {"admin": admin}
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def home_agregar(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request, "nuevoshorizontes/portal_admin/agregar.html", {"admin": admin}
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def home_listado(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request, "nuevoshorizontes/portal_admin/listar.html", {"admin": admin}
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def home_pagos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request, "nuevoshorizontes/portal_admin/pagos.html", {"admin": admin}
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def agregar_admins(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": AdminForm()}

        if request.method == "POST":
            formulario = AdminForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Administrador agregado correctamente")
            else:
                data["form"] = formulario
        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_admins.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_alumnos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": AlumnoForm()}

        if request.method == "POST":
            formulario = AlumnoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Alumno agregado correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_alumnos.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_docentes(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": DocenteForm()}

        if request.method == "POST":
            formulario = DocenteForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Docente agregado correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_docentes.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_apoderados(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": ApoderadoForm()}

        if request.method == "POST":
            formulario = ApoderadoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Apoderado agregado correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_apoderados.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_asignaturas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": AsignaturaForm()}

        if request.method == "POST":
            formulario = AsignaturaForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Asignatura agregada correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_asignaturas.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_cursos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": CursoForm()}

        if request.method == "POST":
            formulario = CursoForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Curso agregado correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_cursos.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_noticias(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": NoticiaForm()}

        if request.method == "POST":
            formulario = NoticiaForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Noticia agregada correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_noticias.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_salas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": SalaForm()}

        if request.method == "POST":
            formulario = SalaForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Sala agregada correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_salas.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def agregar_sedes(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": SedeForm()}

        if request.method == "POST":
            formulario = SedeForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Sede agregada correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_sedes.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def obtener_comunas(request):
    region_id = request.GET.get(
        "region", None
    )  # Obtener el ID de la región desde los parámetros de la solicitud

    # Obtener las comunas de la región especificada
    comunas = Comuna.objects.filter(region_comuna_id=region_id).values(
        "id_comuna", "nombre_comuna"
    )

    # Devolver las comunas en formato JSON
    return JsonResponse(list(comunas), safe=False)


def listar_admins(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin_actual = Administrador.objects.get(correo_admin=correo_admin)
        admins = Administrador.objects.exclude(
            id=1
        )  # Excluir al administrador específico
        admins = Administrador.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_admins.html",
            {"admins": admins, "admin_actual": admin_actual},
        )
    else:
        return redirect("login_administrativo")


def cambiar_pass_admin(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        administrador = get_object_or_404(Administrador, id=id)

        data = {
            "form": AdminForm(instance=administrador),
            "administrador": administrador,
            "admin": admin,
        }

        if request.method == "POST":
            formulario = AdminForm(data=request.POST, instance=administrador)

            [
                formulario.fields.pop(field, None)
                for field in [
                    "id",
                    "nombre_admin",
                    "apellido_admin",
                    "correo_admin",
                ]
            ]

            nueva_contraseña = request.POST.get("password")
            repetir_contraseña = request.POST.get("repetir_contraseña")

            if len(nueva_contraseña) < 8:
                messages.error(
                    request, "La contraseña debe tener al menos 8 caracteres"
                )
            elif nueva_contraseña != repetir_contraseña:
                messages.error(request, "Las contraseñas no coinciden")
            else:
                if formulario.is_valid():
                    administrador.password = nueva_contraseña
                    administrador.save()
                    messages.success(request, "Contraseña cambiada con éxito")
                    return redirect(to="listar_admins")

        return render(
            request,
            "nuevoshorizontes/portal_admin/cambiar_pass/cambiar_pass_admin.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def listar_alumnos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        alumnos = Alumno.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_alumnos.html",
            {"alumnos": alumnos, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def cambiar_pass_alumno(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        alumno = get_object_or_404(Alumno, rut_alumno=id)

        data = {"form": AlumnoForm(instance=alumno), "alumno": alumno, "admin": admin}

        if request.method == "POST":
            formulario = AlumnoForm(data=request.POST, instance=alumno)

            [
                formulario.fields.pop(field, None)
                for field in [
                    "rut_alumno",
                    "nombre_alumno",
                    "appaterno_alumno",
                    "apmaterno_alumno",
                    "direccion_alumno",
                    "telefono_alumno",
                    "correo_alumno",
                    "sede_alumno",
                    "apoderado_alumno",
                    "curso_alumno",
                ]
            ]

            nueva_contraseña = request.POST.get("password")
            repetir_contraseña = request.POST.get("repetir_contraseña")

            if len(nueva_contraseña) < 8:
                messages.error(
                    request, "La contraseña debe tener al menos 8 caracteres"
                )
            elif nueva_contraseña != repetir_contraseña:
                messages.error(request, "Las contraseñas no coinciden")
            else:
                if formulario.is_valid():
                    alumno.password = nueva_contraseña
                    alumno.save()
                    messages.success(request, "Contraseña cambiada con éxito")
                    return redirect(to="listar_alumnos")

        return render(
            request,
            "nuevoshorizontes/portal_admin/cambiar_pass/cambiar_pass_alumno.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def listar_docentes(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        docentes = Docente.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_docentes.html",
            {"docentes": docentes, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def cambiar_pass_docente(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        docente = get_object_or_404(Docente, rut_docente=id)

        data = {
            "form": DocenteForm(instance=docente),
            "docente": docente,
            "admin": admin,
        }

        if request.method == "POST":
            formulario = DocenteForm(data=request.POST, instance=docente)

            [
                formulario.fields.pop(field, None)
                for field in [
                    "rut_docente",
                    "nombre_docente",
                    "appaterno_docente",
                    "apmaterno_docente",
                    "direccion_docente",
                    "telefono_docente",
                    "correo_docente",
                    "sede_docente",
                    "asignaturas_docente",
                ]
            ]

            nueva_contraseña = request.POST.get("password")
            repetir_contraseña = request.POST.get("repetir_contraseña")

            if len(nueva_contraseña) < 8:
                messages.error(
                    request, "La contraseña debe tener al menos 8 caracteres"
                )
            elif nueva_contraseña != repetir_contraseña:
                messages.error(request, "Las contraseñas no coinciden")
            else:
                if formulario.is_valid():
                    docente.password = nueva_contraseña
                    docente.save()
                    messages.success(request, "Contraseña cambiada con éxito")
                    return redirect(to="listar_docentes")

        return render(
            request,
            "nuevoshorizontes/portal_admin/cambiar_pass/cambiar_pass_docente.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def listar_apoderados(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        apoderados = Apoderado.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_apoderados.html",
            {"apoderados": apoderados, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def cambiar_pass_apoderado(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        apoderado = get_object_or_404(Apoderado, rut_apoderado=id)

        data = {
            "form": ApoderadoForm(instance=apoderado),
            "apoderado": apoderado,
            "admin": admin,
        }

        if request.method == "POST":
            formulario = ApoderadoForm(data=request.POST, instance=apoderado)

            [
                formulario.fields.pop(field, None)
                for field in [
                    "rut_apoderado",
                    "nombre_apoderado",
                    "appaterno_apoderado",
                    "apmaterno_apoderado",
                    "direccion_apoderado",
                    "telefono_apoderado",
                    "correo_apoderado",
                ]
            ]

            nueva_contraseña = request.POST.get("password")
            repetir_contraseña = request.POST.get("repetir_contraseña")

            if len(nueva_contraseña) < 8:
                messages.error(
                    request, "La contraseña debe tener al menos 8 caracteres"
                )
            elif nueva_contraseña != repetir_contraseña:
                messages.error(request, "Las contraseñas no coinciden")
            else:
                if formulario.is_valid():
                    apoderado.password = nueva_contraseña
                    apoderado.save()
                    messages.success(request, "Contraseña cambiada con éxito")
                    return redirect(to="listar_apoderados")

        return render(
            request,
            "nuevoshorizontes/portal_admin/cambiar_pass/cambiar_pass_apoderado.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def listar_noticias(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        noticias = Noticias.objects.order_by("fecha_publi").all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_noticias.html",
            {"noticias": noticias, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_asignaturas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        asignaturas = Asignatura.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_asignaturas.html",
            {"asignaturas": asignaturas, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_cursos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        cursos = Curso.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_cursos.html",
            {"cursos": cursos, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_sedes_admin(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        sedes = Sede.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_sedes.html",
            {"sedes": sedes, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_salas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        salas = Sala.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_salas.html",
            {"salas": salas, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_postulaciones(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        postulaciones = Postulaciones.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_postulaciones.html",
            {"postulaciones": postulaciones, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def modificar_alumnos(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        alumno = get_object_or_404(Alumno, rut_alumno=id)

        data = {"form": AlumnoForm(instance=alumno), "admin": admin}

        if request.method == "POST":
            formulario = AlumnoForm(data=request.POST, instance=alumno)

            [
                formulario.fields.pop(
                    field, None
                )  # Elimina el campo 'field' del diccionario 'formulario.fields'
                for field in [  # Itera sobre cada campo de la lista
                    "rut_alumno",  # Campo: rut del alumno
                    "password",  # Campo: contraseña
                ]
            ]

            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Alumno modificado correctamente")
                return redirect(to="listar_alumnos")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_alumnos.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_docentes(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        docente = get_object_or_404(Docente, rut_docente=id)

        data = {"form": DocenteForm(instance=docente), "admin": admin}

        if request.method == "POST":
            formulario = DocenteForm(data=request.POST, instance=docente)

            [
                formulario.fields.pop(
                    field, None
                )  # Elimina el campo 'field' del diccionario 'formulario.fields'
                for field in [  # Itera sobre cada campo de la lista
                    "rut_docente",  # Campo: rut del docente
                    "password",  # Campo: contraseña
                ]
            ]

            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Docente modificado correctamente")
                return redirect(to="listar_docentes")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_docentes.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_apoderados(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        apoderado = get_object_or_404(Apoderado, rut_apoderado=id)

        data = {"form": ApoderadoForm(instance=apoderado), "admin": admin}

        if request.method == "POST":
            formulario = ApoderadoForm(data=request.POST, instance=apoderado)

            [
                formulario.fields.pop(
                    field, None
                )  # Elimina el campo 'field' del diccionario 'formulario.fields'
                for field in [  # Itera sobre cada campo de la lista
                    "rut_apoderado",
                    "password",  # Campo: contraseña
                ]
            ]

            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Apoderado modificado correctamente")
                return redirect(to="listar_apoderados")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_apoderado.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_admins(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        administrador = get_object_or_404(Administrador, id=id)

        data = {"form": AdminForm(instance=administrador), "admin": admin}

        if request.method == "POST":
            formulario = AdminForm(data=request.POST, instance=administrador)

            [
                formulario.fields.pop(
                    field, None
                )  # Elimina el campo 'field' del diccionario 'formulario.fields'
                for field in [  # Itera sobre cada campo de la lista
                    "id",  # Campo: id del admin
                    "password",  # Campo: contraseña
                ]
            ]

            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Administrador modificado correctamente")
                return redirect(to="listar_admins")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_admins.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_noticias(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        noticias = get_object_or_404(Noticias, id=id)

        data = {"form": NoticiaForm(instance=noticias), "admin": admin}

        if request.method == "POST":
            formulario = NoticiaForm(
                data=request.POST, instance=noticias, files=request.FILES
            )
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Noticia modificada correctamente")
                return redirect(to="listar_noticias")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_noticias.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_asignaturas(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        asignaturas = get_object_or_404(Asignatura, id_asignatura=id)

        data = {"form": AsignaturaForm(instance=asignaturas), "admin": admin}

        if request.method == "POST":
            formulario = AsignaturaForm(data=request.POST, instance=asignaturas)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Asignatura modificada correctamente")
                return redirect(to="listar_asignaturas")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_asignaturas.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_cursos(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        cursos = get_object_or_404(Curso, id_curso=id)

        data = {"form": CursoForm(instance=cursos), "admin": admin}

        if request.method == "POST":
            formulario = CursoForm(data=request.POST, instance=cursos)
            [
                formulario.fields.pop(
                    field, None
                )  # Elimina el campo 'field' del diccionario 'formulario.fields'
                for field in [  # Itera sobre cada campo de la lista
                    "id_curso",
                ]
            ]
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Curso modificado correctamente")
                return redirect(to="listar_cursos")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_cursos.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_sedes(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        sedes = get_object_or_404(Sede, id=id)

        data = {"form": SedeForm(instance=sedes), "admin": admin}

        if request.method == "POST":
            formulario = SedeForm(
                data=request.POST, instance=sedes, files=request.FILES
            )
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Sede modificada correctamente")
                return redirect(to="listar_sedes")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_sedes.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_administrativo")


def modificar_salas(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        sala = get_object_or_404(Sala, id_sala=id)
        data = {"form": SalaForm(instance=sala), "admin": admin}

        if request.method == "POST":
            formulario = SalaForm(data=request.POST, instance=sala)
            [
                formulario.fields.pop(
                    field, None
                )  # Elimina el campo 'field' del diccionario 'formulario.fields'
                for field in [  # Itera sobre cada campo de la lista
                    "id_sala",
                ]
            ]
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Sala modificada correctamente")
                return redirect(to="listar_salas")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_salas.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def eliminar_alumno(request, id):
    alumno = get_object_or_404(Alumno, rut_alumno=id)
    alumno.delete()
    messages.success(request, "Alumno eliminado correctamente")
    return redirect(to="listar_alumnos")


def eliminar_docentes(request, id):
    docente = get_object_or_404(Docente, rut_docente=id)
    docente.delete()
    messages.success(request, "Docente eliminado correctamente")
    return redirect(to="listar_docentes")


def eliminar_apoderado(request, id):
    apoderado = get_object_or_404(Apoderado, rut_apoderado=id)
    apoderado.delete()
    messages.success(request, "Apoderado eliminado correctamente")
    return redirect(to="listar_apoderados")


def eliminar_noticias(request, id):
    noticias = get_object_or_404(Noticias, id=id)
    noticias.delete()
    messages.success(request, "Noticia eliminada correctamente")
    return redirect(to="listar_noticias")


def eliminar_asignatura(request, id):
    asignaturas = get_object_or_404(Asignatura, id_asignatura=id)
    asignaturas.delete()
    messages.success(request, "Asignatura eliminada correctamente")
    return redirect(to="listar_asignaturas")


def eliminar_curso(request, id):
    cursos = get_object_or_404(Curso, id_curso=id)
    cursos.delete()
    messages.success(request, "Curso eliminado correctamente")
    return redirect(to="listar_cursos")


def eliminar_sedes(request, id):
    sedes = get_object_or_404(Sede, id=id)
    sedes.delete()
    messages.success(request, "Sede eliminada correctamente")
    return redirect(to="listar_sedes")


def eliminar_salas(request, id):
    salas = get_object_or_404(Sala, id_sala=id)
    salas.delete()
    messages.success(request, "Sala eliminada correctamente")
    return redirect(to="listar_salas")


def eliminar_admin(request, id):
    admin = get_object_or_404(Administrador, id=id)
    admin.delete()
    messages.success(request, "Administrador eliminado correctamente")
    return redirect(to="listar_admins")


def eliminar_postulacion(request, id):
    postulacion = get_object_or_404(Postulaciones, id=id)
    postulacion.delete()
    messages.success(request, "Postulación eliminada correctamente")
    return redirect(to="listar_postulaciones")


def home_alumno(request):
    correo_alumno = request.session.get("correo_alumno", None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request,
            "nuevoshorizontes/portal_alumno/home_alumno.html",
            {"alumno": alumno},
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_alumno")


def miperfil_alumno(request):
    correo_alumno = request.session.get("correo_alumno", None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)
        return render(
            request, "nuevoshorizontes/portal_alumno/miperfil.html", {"alumno": alumno}
        )

    else:
        return redirect("login_alumno")


def guardar_perfil_alumno(request):
    if request.method == "POST":
        correo_alumno = request.session.get("correo_alumno", None)
        if correo_alumno:
            alumno = Alumno.objects.get(correo_alumno=correo_alumno)
            alumno.nombre_alumno = request.POST.get("nombre")
            alumno.appaterno_alumno = request.POST.get("paterno")
            alumno.apmaterno_alumno = request.POST.get("materno")
            alumno.direccion_alumno = request.POST.get("direccion")
            alumno.telefono_alumno = request.POST.get("telefono")
            alumno.save()  # Guardar los cambios en el modelo
            messages.success(request, "Los cambios se guardaron exitosamente.")
        else:
            messages.error(
                request,
                "No se pudo guardar los cambios. Por favor, intenta nuevamente.",
            )

    return redirect("miperfil_alumno")


def notas_alumno(request):
    return render(request, "nuevoshorizontes/portal_alumno/notas_alumno.html")


def horario_alumno(request):
    return render(request, "nuevoshorizontes/portal_alumno/horario_alumno.html")


def home_apoderado(request):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request,
            "nuevoshorizontes/portal_apoderado/home_apoderado.html",
            {"apoderado": apoderado},
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_apoderado")


def miperfil_apoderado(request):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        return render(
            request,
            "nuevoshorizontes/portal_apoderado/miperfil.html",
            {"apoderado": apoderado},
        )

    else:
        return redirect("login_apoderado")


def guardar_perfil_apoderado(request):
    if request.method == "POST":
        correo_apoderado = request.session.get("correo_apoderado", None)
        if correo_apoderado:
            apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
            apoderado.nombre_apoderado = request.POST.get("nombre")
            apoderado.appaterno_apoderado = request.POST.get("paterno")
            apoderado.apmaterno_apoderado = request.POST.get("materno")
            apoderado.direccion_apoderado = request.POST.get("direccion")
            apoderado.telefono_apoderado = request.POST.get("telefono")
            # Actualizar otros campos del modelo "Apoderado" según sea necesario
            apoderado.save()  # Guardar los cambios en el modelo
            messages.success(request, "Los cambios se guardaron exitosamente.")
        else:
            messages.error(
                request,
                "No se pudo guardar los cambios. Por favor, intenta nuevamente.",
            )

    return redirect("miperfil_apoderado")


def lista_hijos(request):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumnos = Alumno.objects.filter(apoderado_alumno=apoderado)
        return render(
            request,
            "nuevoshorizontes/portal_apoderado/lista_hijos.html",
            {"apoderado": apoderado, "alumnos": alumnos},
        )

    else:
        return redirect("login_apoderado")


def horarios_apoderado(request):
    return render(request, "nuevoshorizontes/portal_apoderado/horarios_apoderado.html")


def asistencias_apoderado(request):
    return render(
        request, "nuevoshorizontes/portal_apoderado/asistencias_apoderado.html"
    )


def notas_apoderado(request):
    return render(request, "nuevoshorizontes/portal_apoderado/notas_apoderado.html")


def pagos_apoderado(request):
    return render(request, "nuevoshorizontes/portal_apoderado/pagos_apoderado.html")


def home_docente(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request,
            "nuevoshorizontes/portal_docente/home_docente.html",
            {"docente": docente},
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_docente")


def miperfil_docente(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        return render(
            request,
            "nuevoshorizontes/portal_docente/miperfil.html",
            {"docente": docente},
        )

    else:
        return redirect("login_docente")


def guardar_perfil_docente(request):
    if request.method == "POST":
        correo_docente = request.session.get("correo_docente", None)
        if correo_docente:
            docente = Docente.objects.get(correo_docente=correo_docente)
            docente.nombre_docente = request.POST.get("nombre")
            docente.appaterno_docente = request.POST.get("paterno")
            docente.apmaterno_docente = request.POST.get("materno")
            docente.direccion_docente = request.POST.get("direccion")
            docente.telefono_docente = request.POST.get("telefono")
            # Actualizar otros campos del modelo "Apoderado" según sea necesario
            docente.save()  # Guardar los cambios en el modelo
            messages.success(request, "Los cambios se guardaron exitosamente.")
        else:
            messages.error(
                request,
                "No se pudo guardar los cambios. Por favor, intenta nuevamente.",
            )

    return redirect("miperfil_docente")


def curso_docente(request):
    # Obtiene el valor de la clave "correo_docente" de la sesión del objeto request
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:  # Verifica si correo_docente tiene un valor
        # Busca un objeto Docente en la base de datos con correo_docente igual al valor obtenido anteriormente
        docente = Docente.objects.get(correo_docente=correo_docente)
        # Obtiene el primer curso relacionado con el docente
        curso = docente.curso_set.first()
        if curso:  # Verifica si curso tiene un valor
            # Obtiene todos los objetos Alumno de la base de datos con curso_alumno igual al valor de curso
            alumnos = Alumno.objects.filter(curso_alumno=curso)
            # Obtiene el primer alumno de la lista de alumnos
            primer_alumno = alumnos.first()
        else:
            alumnos = []  # Establece una lista vacía
            primer_alumno = None  # Establece primer_alumno como None
        # Devuelve una respuesta de renderizado utilizando la plantilla y pasando un diccionario de contexto
        return render(
            request,
            "nuevoshorizontes/portal_docente/curso_docente.html",
            {"docente": docente, "alumnos": alumnos, "primer_alumno": primer_alumno},
        )
    else:
        # Devuelve una respuesta de redirección a la vista con nombre "login_docente"
        return redirect("login_docente")


def asignaturas_docente(request):
    return render(request, "nuevoshorizontes/portal_docente/asignaturas_docente.html")


def asistencia_docente(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        return render(
            request,
            "nuevoshorizontes/portal_docente/asistencia_docente.html",
            {"docente": docente},
        )

    else:
        return redirect("login_docente")


def buscar_asistencia(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        return render(
            request,
            "nuevoshorizontes/portal_docente/asistencia/buscar_asistencia.html",
            {"docente": docente},
        )

    else:
        return redirect("login_docente")


def agregar_asistencia(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)

        if request.method == "POST":
            fecha_actual = date.today()

            # Obtener la lista de alumnos del curso del docente
            curso = Curso.objects.get(docente_curso=docente)
            alumnos = Alumno.objects.filter(curso_alumno=curso)

            # Guardar la asistencia de cada alumno
            for alumno in alumnos:
                tipo_asistencia_id = request.POST.get(str(alumno.rut_alumno))
                tipo_asistencia = tipoAsistencia.objects.get(pk=tipo_asistencia_id)

                Asistencia.objects.create(
                    tipo_asistencia=tipo_asistencia,
                    fecha_asistencia=fecha_actual,
                    alumno=alumno,
                )

            messages.success(request, "Asistencia guardada exitosamente.")
            return redirect("asistencia_docente")

        fecha_actual = date.today().strftime("%d/%m/%Y")
        estados_asistencia = tipoAsistencia.objects.all()
        curso = Curso.objects.get(docente_curso=docente)
        alumnos = Alumno.objects.filter(curso_alumno=curso)

        return render(
            request,
            "nuevoshorizontes/portal_docente/asistencia/agregar_asistencia.html",
            {
                "docente": docente,
                "fecha_actual": fecha_actual,
                "alumnos": alumnos,
                "estados_asistencia": estados_asistencia,
            },
        )
    else:
        return redirect("login_docente")
