from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from .models import *
from .forms import *
from datetime import date, datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Count, Case, When
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models import Q


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
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            alumno = Alumno.objects.get(correo_alumno=email)
            if check_password(password, alumno.password):
                request.session["correo_alumno"] = alumno.correo_alumno
                return redirect("home_alumno")
            else:
                messages.error(
                    request, "El correo electrónico o la contraseña no son correctos"
                )
        except Alumno.DoesNotExist:
            messages.error(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_alumno.html")


def login_docente(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            docente = Docente.objects.get(correo_docente=email)
            if check_password(password, docente.password):
                request.session["correo_docente"] = docente.correo_docente
                return redirect("home_docente")
            else:
                messages.error(
                    request, "El correo electrónico o la contraseña no son correctos"
                )
        except Docente.DoesNotExist:
            messages.error(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_docente.html")


def login_apoderado(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            apoderado = Apoderado.objects.get(correo_apoderado=email)
            if check_password(password, apoderado.password):
                request.session["correo_apoderado"] = apoderado.correo_apoderado
                return redirect("home_apoderado")
            else:
                messages.error(
                    request, "El correo electrónico o la contraseña no son correctos"
                )
        except Apoderado.DoesNotExist:
            messages.error(
                request, "El correo electrónico o la contraseña no son correctos"
            )

    return render(request, "nuevoshorizontes/login_portales/login_apoderado.html")


def login_administrativo(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            administrador = Administrador.objects.get(correo_admin=email)
            if check_password(password, administrador.password):
                request.session["correo_admin"] = administrador.correo_admin
                return redirect("home_admin")
            else:
                messages.error(
                    request, "El correo electrónico o la contraseña no son correctos"
                )
        except Administrador.DoesNotExist:
            messages.error(
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


def agregar_admins(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": AdminForm()}

        if request.method == "POST":
            formulario = AdminForm(data=request.POST)
            if formulario.is_valid():
                administrador = formulario.save(commit=False)
                administrador.password = make_password(
                    formulario.cleaned_data["password"]
                )  # Encriptar la contraseña
                administrador.save()
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
                alumno = formulario.save(commit=False)
                alumno.password = make_password(formulario.cleaned_data["password"])
                alumno.save()
                messages.success(request, "Alumno agregado correctamente")
                return redirect("agregar_alumnos")
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
            nueva_contraseña = request.POST.get("password")
            repetir_contraseña = request.POST.get("repetir_contraseña")

            if len(nueva_contraseña) < 8:
                messages.error(
                    request, "La contraseña debe tener al menos 8 caracteres"
                )
                data["form"] = formulario
            elif nueva_contraseña != repetir_contraseña:
                messages.error(request, "Las contraseñas no coinciden")
                data["form"] = formulario
            else:
                if formulario.is_valid():
                    docente = formulario.save(commit=False)
                    docente.password = make_password(nueva_contraseña)
                    docente.save()
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
            nueva_contraseña = request.POST.get("password")
            repetir_contraseña = request.POST.get("repetir_contraseña")

            if len(nueva_contraseña) < 8:
                messages.error(
                    request, "La contraseña debe tener al menos 8 caracteres"
                )
                data["form"] = formulario
            elif nueva_contraseña != repetir_contraseña:
                messages.error(request, "Las contraseñas no coinciden")
                data["form"] = formulario
            else:
                if formulario.is_valid():
                    apoderado = formulario.save(commit=False)
                    apoderado.password = make_password(nueva_contraseña)
                    apoderado.save()
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


def agregar_pagos_colegio(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        data = {"admin": admin, "form": PagosColegioForm()}

        if request.method == "POST":
            formulario = PagosColegioForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Pago colegio agregado correctamente")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_pagos_colegio.html",
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


def agregar_horariocurso(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        # Puedes pasar el objeto 'admin' al contexto de renderizado
        nombres_bloque_html = [
            "lun_block1",
            "mar_block1",
            "mie_block1",
            "jue_block1",
            "vie_block1",
            "lun_block2",
            "mar_block2",
            "mie_block2",
            "jue_block2",
            "vie_block2",
            "lun_block3",
            "mar_block3",
            "mie_block3",
            "jue_block3",
            "vie_block3",
            "lun_block4",
            "mar_block4",
            "mie_block4",
            "jue_block4",
            "vie_block4",
            "lun_block5",
            "mar_block5",
            "mie_block5",
            "jue_block5",
            "vie_block5",
            "lun_block6",
            "mar_block6",
            "mie_block6",
            "jue_block6",
            "vie_block6",
            "lun_block7",
            "mar_block7",
            "mie_block7",
            "jue_block7",
            "vie_block7",
            "lun_block8",
            "mar_block8",
            "mie_block8",
            "jue_block8",
            "vie_block8",
            "lun_block9",
            "mar_block9",
            "mie_block9",
            "jue_block9",
            "vie_block9",
        ]

        nombres_bloques = [
            "L01",
            "M01",
            "X01",
            "J01",
            "V01",
            "L02",
            "M02",
            "X02",
            "J02",
            "V02",
            "L03",
            "M03",
            "X03",
            "J03",
            "V03",
            "L04",
            "M04",
            "X04",
            "J04",
            "V04",
            "L05",
            "M05",
            "X05",
            "J05",
            "V05",
            "L06",
            "M06",
            "X06",
            "J06",
            "V06",
            "L07",
            "M07",
            "X07",
            "J07",
            "V07",
            "L08",
            "M08",
            "X08",
            "J08",
            "V08",
            "L09",
            "M09",
            "X09",
            "J09",
            "V09",
        ]

        if request.method == "POST":
            curso_id = request.POST.get("curso")

            if not curso_id:
                messages.error(request, "Debes seleccionar un curso.")
                return redirect("agregar_horariocurso")

            if Bloque.objects.filter(curso_bloque=curso_id).exists():
                messages.error(request, "Ya existe un horario creado para este curso")
                return redirect("agregar_horariocurso")

            curso = Curso.objects.get(id_curso=curso_id)

            if not request.POST.get("lun_block1"):
                messages.error(request, "No puedes dejar todos los bloques vacíos.")
                return redirect("agregar_horariocurso")

            for i in range(len(nombres_bloque_html)):
                asignatura_id = request.POST.get(nombres_bloque_html[i])
                if asignatura_id:
                    asignatura = Asignatura.objects.get(id_asignatura=asignatura_id)
                    docente = asignatura.profesor_asignatura

                    Bloque.objects.create(
                        nombre_bloque=nombres_bloques[i],
                        curso_bloque=curso,
                        asignatura_bloque=asignatura,
                        docente_bloque=docente,
                    )
                else:
                    Bloque.objects.create(
                        nombre_bloque=nombres_bloques[i],
                        curso_bloque=curso,
                        asignatura_bloque=None,
                        docente_bloque=None,
                    )

            messages.success(request, "Horario guardado exitosamente.")

        data = {
            "cursos": Curso.objects.order_by("nombre_curso"),
            "salas": Sala.objects.order_by("nombre_sala"),
            "asignaturas": Asignatura.objects.order_by("nombre_asignatura"),
            "profesores": Docente.objects.all(),
            "admin": admin,
        }

        return render(
            request,
            "nuevoshorizontes/portal_admin/formularios/agregar_horariocurso.html",
            data,
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
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
        if admin_actual.id != 1:
            admins = Administrador.objects.exclude(id=1)
        else:
            admins = Administrador.objects.all()

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(admins, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_admins.html",
            {"page_obj": page_obj, "admin_actual": admin_actual},
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
                    administrador.password = make_password(
                        nueva_contraseña
                    )  # Encriptar la nueva contraseña
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

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(alumnos, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_alumnos.html",
            {"page_obj": page_obj, "admin": admin},
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
                    alumno.password = make_password(
                        nueva_contraseña
                    )  # Encriptar la nueva contraseña
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

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(docentes, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_docentes.html",
            {"page_obj": page_obj, "admin": admin},
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
                    docente.password = make_password(
                        nueva_contraseña
                    )  # Encriptar la nueva contraseña
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

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(apoderados, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_apoderados.html",
            {"page_obj": page_obj, "admin": admin},
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
                    apoderado.password = make_password(
                        nueva_contraseña
                    )  # Encriptar la nueva contraseña
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

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(asignaturas, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_asignaturas.html",
            {"page_obj": page_obj, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_cursos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        cursos = Curso.objects.all()

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(cursos, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_cursos.html",
            {"page_obj": page_obj, "admin": admin},
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

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(salas, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_salas.html",
            {"page_obj": page_obj, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_postulaciones(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        postulaciones = Postulaciones.objects.all()

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(postulaciones, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_postulaciones.html",
            {"page_obj": page_obj, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_pago_colegio(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        pago_colegio = Pagos_colegio.objects.all()

        # Cantidad de elementos por página
        items_por_pagina = 10

        # Inicializar el objeto Paginator
        paginator = Paginator(pago_colegio, items_por_pagina)

        # Obtener el número de página de la URL
        page_number = request.GET.get("page")

        # Obtener la página actual del paginador
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_pagos_colegio.html",
            {"page_obj": page_obj, "admin": admin},
        )
    else:
        return redirect("login_administrativo")


def listar_horarios_cursos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)

        cursos_con_bloques = Curso.objects.filter(bloque__isnull=False).distinct()
        # Obtener los cursos que tienen al menos un bloque asociado

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_horarios_curso.html",
            {"admin": admin, "cursos_con_bloques": cursos_con_bloques},
        )
    else:
        return redirect("login_administrativo")


def listar_horarios(request, id_curso):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        curso = Curso.objects.get(id_curso=id_curso)

        # Obtener los bloques del alumno
        bloques = Bloque.objects.filter(curso_bloque=curso.id_curso)

        # Crear un diccionario para mapear los nombres de bloque del HTML con los nombres de la base de datos
        nombres_bloque_html = [
            "lun_block1",
            "mar_block1",
            "mie_block1",
            "jue_block1",
            "vie_block1",
            "lun_block2",
            "mar_block2",
            "mie_block2",
            "jue_block2",
            "vie_block2",
            "lun_block3",
            "mar_block3",
            "mie_block3",
            "jue_block3",
            "vie_block3",
            "lun_block4",
            "mar_block4",
            "mie_block4",
            "jue_block4",
            "vie_block4",
            "lun_block5",
            "mar_block5",
            "mie_block5",
            "jue_block5",
            "vie_block5",
            "lun_block6",
            "mar_block6",
            "mie_block6",
            "jue_block6",
            "vie_block6",
            "lun_block7",
            "mar_block7",
            "mie_block7",
            "jue_block7",
            "vie_block7",
            "lun_block8",
            "mar_block8",
            "mie_block8",
            "jue_block8",
            "vie_block8",
            "lun_block9",
            "mar_block9",
            "mie_block9",
            "jue_block9",
            "vie_block9",
        ]

        nombres_bloques = [
            "L01",
            "M01",
            "X01",
            "J01",
            "V01",
            "L02",
            "M02",
            "X02",
            "J02",
            "V02",
            "L03",
            "M03",
            "X03",
            "J03",
            "V03",
            "L04",
            "M04",
            "X04",
            "J04",
            "V04",
            "L05",
            "M05",
            "X05",
            "J05",
            "V05",
            "L06",
            "M06",
            "X06",
            "J06",
            "V06",
            "L07",
            "M07",
            "X07",
            "J07",
            "V07",
            "L08",
            "M08",
            "X08",
            "J08",
            "V08",
            "L09",
            "M09",
            "X09",
            "J09",
            "V09",
        ]

        # Obtener los nombres de asignatura y docente para cada bloque
        horarios = []
        for i, bloque in enumerate(bloques):
            nombre_bloque_html = nombres_bloque_html[i]
            nombre_bloque_db = nombres_bloques[i]
            asignatura = (
                bloque.asignatura_bloque.nombre_asignatura
                if bloque.asignatura_bloque
                else None
            )
            docente = (
                bloque.docente_bloque.nombre_completo()
                if bloque.docente_bloque
                else None
            )
            horarios.append((nombre_bloque_html, nombre_bloque_db, asignatura, docente))

        # Crear un diccionario con los horarios para pasar a la plantilla
        horarios_dict = {}
        for horario in horarios:
            horarios_dict[horario[0]] = {
                "nombre_bloque_db": horario[1],
                "asignatura": horario[2],
                "docente": horario[3],
            }

        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_horarios.html",
            {
                "admin": admin,
                "curso": curso,
                "horarios": horarios_dict,
                "bloques": bloques,
            },
        )
    else:
        return redirect("login_administrativo")


def listar_asistencias(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        asistencias = Asistencia.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_asistencias.html",
            {"admin": admin, "asistencias": asistencias},
        )
    else:
        return redirect("login_administrativo")


def listar_notas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        notas = Calificacion.objects.all()
        return render(
            request,
            "nuevoshorizontes/portal_admin/listados/listar_notas.html",
            {"admin": admin, "notas": notas},
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


def modificar_horario_curso(request, id_curso):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        curso = Curso.objects.get(id_curso=id_curso)

        # Obtener los bloques del alumno
        bloques = Bloque.objects.filter(curso_bloque=curso.id_curso)

        # Crear un diccionario para mapear los nombres de bloque del HTML con los nombres de la base de datos
        nombres_bloque_html = [
            "lun_block1",
            "mar_block1",
            "mie_block1",
            "jue_block1",
            "vie_block1",
            "lun_block2",
            "mar_block2",
            "mie_block2",
            "jue_block2",
            "vie_block2",
            "lun_block3",
            "mar_block3",
            "mie_block3",
            "jue_block3",
            "vie_block3",
            "lun_block4",
            "mar_block4",
            "mie_block4",
            "jue_block4",
            "vie_block4",
            "lun_block5",
            "mar_block5",
            "mie_block5",
            "jue_block5",
            "vie_block5",
            "lun_block6",
            "mar_block6",
            "mie_block6",
            "jue_block6",
            "vie_block6",
            "lun_block7",
            "mar_block7",
            "mie_block7",
            "jue_block7",
            "vie_block7",
            "lun_block8",
            "mar_block8",
            "mie_block8",
            "jue_block8",
            "vie_block8",
            "lun_block9",
            "mar_block9",
            "mie_block9",
            "jue_block9",
            "vie_block9",
        ]

        nombres_bloques = [
            "L01",
            "M01",
            "X01",
            "J01",
            "V01",
            "L02",
            "M02",
            "X02",
            "J02",
            "V02",
            "L03",
            "M03",
            "X03",
            "J03",
            "V03",
            "L04",
            "M04",
            "X04",
            "J04",
            "V04",
            "L05",
            "M05",
            "X05",
            "J05",
            "V05",
            "L06",
            "M06",
            "X06",
            "J06",
            "V06",
            "L07",
            "M07",
            "X07",
            "J07",
            "V07",
            "L08",
            "M08",
            "X08",
            "J08",
            "V08",
            "L09",
            "M09",
            "X09",
            "J09",
            "V09",
        ]

        # Obtener los nombres de asignatura y docente para cada bloque
        horarios = []
        for i, bloque in enumerate(bloques):
            nombre_bloque_html = nombres_bloque_html[i]
            nombre_bloque_db = nombres_bloques[i]
            asignatura = (
                bloque.asignatura_bloque.nombre_asignatura
                if bloque.asignatura_bloque
                else None
            )
            docente = (
                bloque.docente_bloque.nombre_completo()
                if bloque.docente_bloque
                else None
            )
            horarios.append((nombre_bloque_html, nombre_bloque_db, asignatura, docente))

        # Crear un diccionario con los horarios para pasar a la plantilla
        horarios_dict = {}
        for horario in horarios:
            horarios_dict[horario[0]] = {
                "nombre_bloque_db": horario[1],
                "asignatura": horario[2],
                "docente": horario[3],
            }

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_horario_curso.html",
            {
                "admin": admin,
                "curso": curso,
                "horarios": horarios_dict,
                "bloques": bloques,
                "asignaturas": Asignatura.objects.order_by("nombre_asignatura"),
                "profesores": Docente.objects.all(),
            },
        )

    else:
        return redirect("login_administrativo")


def modificar_pago_colegio(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        pago_colegio = get_object_or_404(Pagos_colegio, id_pago_colegio=id)
        data = {"form": PagosColegioForm(instance=pago_colegio), "admin": admin}

        if request.method == "POST":
            formulario = PagosColegioForm(data=request.POST, instance=pago_colegio)
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
                messages.success(request, "Pago colegio modificado correctamente")
                return redirect(to="listar_pago_colegio")
            else:
                data["form"] = formulario

        return render(
            request,
            "nuevoshorizontes/portal_admin/modificar/modificar_pagos_colegio.html",
            data,
        )
    else:
        return redirect("login_administrativo")


def eliminar_alumno(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        alumno = get_object_or_404(Alumno, rut_alumno=id)
        alumno.delete()
        messages.success(request, "Alumno eliminado correctamente")
        return redirect("listar_alumnos")
    else:
        return redirect("login_administrativo")


def eliminar_docentes(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        docente = get_object_or_404(Docente, rut_docente=id)
        docente.delete()
        messages.success(request, "Docente eliminado correctamente")
        return redirect("listar_docentes")
    else:
        return redirect("login_administrativo")


def eliminar_apoderado(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        apoderado = get_object_or_404(Apoderado, rut_apoderado=id)
        apoderado.delete()
        messages.success(request, "Apoderado eliminado correctamente")
        return redirect("listar_apoderados")
    else:
        return redirect("login_administrativo")


def eliminar_noticias(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        noticia = get_object_or_404(Noticias, id=id)
        noticia.delete()
        messages.success(request, "Noticia eliminada correctamente")
        return redirect("listar_noticias")
    else:
        return redirect("login_administrativo")


def eliminar_asignatura(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        asignatura = get_object_or_404(Asignatura, id_asignatura=id)
        asignatura.delete()
        messages.success(request, "Asignatura eliminada correctamente")
        return redirect("listar_asignaturas")
    else:
        return redirect("login_administrativo")


def eliminar_curso(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        curso = get_object_or_404(Curso, id_curso=id)
        curso.delete()
        messages.success(request, "Curso eliminado correctamente")
        return redirect("listar_cursos")
    else:
        return redirect("login_administrativo")


def eliminar_sedes(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        sede = get_object_or_404(Sede, id=id)
        sede.delete()
        messages.success(request, "Sede eliminada correctamente")
        return redirect("listar_sedes")
    else:
        return redirect("login_administrativo")


def eliminar_salas(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        sala = get_object_or_404(Sala, id_sala=id)
        sala.delete()
        messages.success(request, "Sala eliminada correctamente")
        return redirect("listar_salas")
    else:
        return redirect("login_administrativo")


def eliminar_admin(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = get_object_or_404(Administrador, id=id)
        admin.delete()
        messages.success(request, "Administrador eliminado correctamente")
        return redirect("listar_admins")
    else:
        return redirect("login_administrativo")


def eliminar_postulacion(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        postulacion = get_object_or_404(Postulaciones, id=id)
        postulacion.delete()
        messages.success(request, "Postulación eliminada correctamente")
        return redirect("listar_postulaciones")
    else:
        return redirect("login_administrativo")


def eliminar_pagos_colegio(request, id):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        pago_colegio = get_object_or_404(Pagos_colegio, id_pago_colegio=id)
        pago_colegio.delete()
        messages.success(request, "Pago colegio eliminado correctamente")
        return redirect("listar_pago_colegio")
    else:
        return redirect("login_administrativo")


def eliminar_horario(request, id_curso):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        curso = get_object_or_404(Curso, id_curso=id_curso)
        bloques = Bloque.objects.filter(curso_bloque=curso)
        bloques.delete()
        messages.success(request, "Horario eliminado correctamente")
        return redirect("listar_horarios_cursos")
    else:
        return redirect("login_administrativo")


def eliminar_asistencias(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        Asistencia.objects.all().delete()
        messages.success(request, "Todas las asistencias se eliminaron correctamente")
        return redirect("listar_asistencias")
    else:
        return redirect("login_administrativo")


def eliminar_notas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        Calificacion.objects.all().delete()
        messages.success(
            request, "Todas las calificaciones se eliminaron correctamente"
        )
        return redirect("listar_notas")
    else:
        return redirect("login_administrativo")


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


def notas_alumno(request):
    correo_alumno = request.session.get("correo_alumno", None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)

        # Obtener el curso asignado al alumno
        curso_alumno = alumno.curso_alumno

        # Obtener los bloques relacionados con el curso del alumno que no estén en blanco y que tengan asignatura y docente
        bloques = Bloque.objects.filter(
            curso_bloque=curso_alumno,
            nombre_bloque__isnull=False,
            asignatura_bloque__isnull=False,
            docente_bloque__isnull=False,
        )

        # Obtener las asignaturas correspondientes a los bloques sin repetir
        asignaturas = sorted(
            set(bloque.asignatura_bloque for bloque in bloques),
            key=lambda x: x.nombre_asignatura,
        )

        return render(
            request,
            "nuevoshorizontes/portal_alumno/notas_alumno.html",
            {"alumno": alumno, "asignaturas": asignaturas},
        )
    else:
        return redirect("login_alumno")


def notas_por_asignatura(request, asignatura_id):
    correo_alumno = request.session.get("correo_alumno", None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)
        asignatura = Asignatura.objects.get(id_asignatura=asignatura_id)
        calificaciones = Calificacion.objects.filter(
            alumno=alumno, asignatura=asignatura
        )
        # Calcular el promedio de las notas
        total_notas = calificaciones.count()
        suma_notas = calificaciones.aggregate(Sum("valor")).get("valor__sum")
        promedio = suma_notas / total_notas if total_notas > 0 else 0

        return render(
            request,
            "nuevoshorizontes/portal_alumno/notas_por_asignatura.html",
            {"alumno": alumno, "calificaciones": calificaciones, "promedio": promedio},
        )
    else:
        return redirect("login_alumno")


def horario_alumno(request):
    correo_alumno = request.session.get("correo_alumno", None)
    if correo_alumno:
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)

        # Obtener los bloques del alumno
        bloques = Bloque.objects.filter(curso_bloque=alumno.curso_alumno)

        # Crear un diccionario para mapear los nombres de bloque del HTML con los nombres de la base de datos
        nombres_bloque_html = [
            "lun_block1",
            "mar_block1",
            "mie_block1",
            "jue_block1",
            "vie_block1",
            "lun_block2",
            "mar_block2",
            "mie_block2",
            "jue_block2",
            "vie_block2",
            "lun_block3",
            "mar_block3",
            "mie_block3",
            "jue_block3",
            "vie_block3",
            "lun_block4",
            "mar_block4",
            "mie_block4",
            "jue_block4",
            "vie_block4",
            "lun_block5",
            "mar_block5",
            "mie_block5",
            "jue_block5",
            "vie_block5",
            "lun_block6",
            "mar_block6",
            "mie_block6",
            "jue_block6",
            "vie_block6",
            "lun_block7",
            "mar_block7",
            "mie_block7",
            "jue_block7",
            "vie_block7",
            "lun_block8",
            "mar_block8",
            "mie_block8",
            "jue_block8",
            "vie_block8",
            "lun_block9",
            "mar_block9",
            "mie_block9",
            "jue_block9",
            "vie_block9",
        ]

        nombres_bloques = [
            "L01",
            "M01",
            "X01",
            "J01",
            "V01",
            "L02",
            "M02",
            "X02",
            "J02",
            "V02",
            "L03",
            "M03",
            "X03",
            "J03",
            "V03",
            "L04",
            "M04",
            "X04",
            "J04",
            "V04",
            "L05",
            "M05",
            "X05",
            "J05",
            "V05",
            "L06",
            "M06",
            "X06",
            "J06",
            "V06",
            "L07",
            "M07",
            "X07",
            "J07",
            "V07",
            "L08",
            "M08",
            "X08",
            "J08",
            "V08",
            "L09",
            "M09",
            "X09",
            "J09",
            "V09",
        ]

        # Obtener los nombres de asignatura y docente para cada bloque
        horarios = []
        for i, bloque in enumerate(bloques):
            nombre_bloque_html = nombres_bloque_html[i]
            nombre_bloque_db = nombres_bloques[i]
            asignatura = (
                bloque.asignatura_bloque.nombre_asignatura
                if bloque.asignatura_bloque
                else None
            )
            docente = (
                bloque.docente_bloque.nombre_completo()
                if bloque.docente_bloque
                else None
            )
            horarios.append((nombre_bloque_html, nombre_bloque_db, asignatura, docente))

        # Crear un diccionario con los horarios para pasar a la plantilla
        horarios_dict = {}
        for horario in horarios:
            horarios_dict[horario[0]] = {
                "nombre_bloque_db": horario[1],
                "asignatura": horario[2],
                "docente": horario[3],
            }

        return render(
            request,
            "nuevoshorizontes/portal_alumno/horario_alumno.html",
            {"alumno": alumno, "horarios": horarios_dict, "bloques": bloques},
        )

    else:
        return redirect("login_alumno")


def asistencia_alumno(request):
    # Obtener el correo del alumno desde la sesión
    correo_alumno = request.session.get("correo_alumno", None)

    if correo_alumno:
        # Obtener el objeto Alumno correspondiente al correo
        alumno = Alumno.objects.get(correo_alumno=correo_alumno)

        # Obtener el recuento de asistencias por tipo
        asistencias = (
            Asistencia.objects.filter(alumno=alumno)
            .values("alumno")
            .annotate(
                presentes=Count(
                    Case(When(tipo_asistencia_id=1, then=1))
                ),  # Esta línea cuenta el número de asistencias de tipo "presente" para el alumno actual.
                ausentes=Count(
                    Case(When(tipo_asistencia_id=2, then=1))
                ),  # Esta línea cuenta el número de asistencias de tipo "ausente" para el alumno actual.
                justificados=Count(
                    Case(When(tipo_asistencia_id=3, then=1))
                ),  # Esta línea cuenta el número de asistencias de tipo "justificado" para el alumno actual.
            )
        )

        # Calcular el porcentaje de asistencia
        total_asistencias = sum(
            a["presentes"] + a["ausentes"] + a["justificados"] for a in asistencias
        )
        if total_asistencias > 0:
            porcentaje_asistencia = (
                sum(a["presentes"] + a["justificados"] for a in asistencias)
                / total_asistencias
            ) * 100
        else:
            porcentaje_asistencia = 0

        return render(
            request,
            "nuevoshorizontes/portal_alumno/asistencia_alumno.html",
            {
                "alumno": alumno,  # Objeto Alumno
                "asistencias": asistencias,  # Asistencias por tipo
                "porcentaje_asistencia": porcentaje_asistencia,  # Porcentaje de asistencia
                "total_asistencias": total_asistencias,
            },
        )
    else:
        return redirect("login_alumno")  # Redireccionar al inicio de sesión del alumno


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
        return redirect("login_docente")


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
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumnos = Alumno.objects.filter(apoderado_alumno=apoderado)
        return render(
            request,
            "nuevoshorizontes/portal_apoderado/horarios_apoderado.html",
            {"apoderado": apoderado, "alumnos": alumnos},
        )

    else:
        return redirect("login_apoderado")


def ver_horario_hijo(request, rut_alumno):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumno = Alumno.objects.get(rut_alumno=rut_alumno)

        # Obtener los bloques del alumno
        bloques = Bloque.objects.filter(curso_bloque=alumno.curso_alumno)

        # Crear un diccionario para mapear los nombres de bloque del HTML con los nombres de la base de datos
        nombres_bloque_html = [
            "lun_block1",
            "mar_block1",
            "mie_block1",
            "jue_block1",
            "vie_block1",
            "lun_block2",
            "mar_block2",
            "mie_block2",
            "jue_block2",
            "vie_block2",
            "lun_block3",
            "mar_block3",
            "mie_block3",
            "jue_block3",
            "vie_block3",
            "lun_block4",
            "mar_block4",
            "mie_block4",
            "jue_block4",
            "vie_block4",
            "lun_block5",
            "mar_block5",
            "mie_block5",
            "jue_block5",
            "vie_block5",
            "lun_block6",
            "mar_block6",
            "mie_block6",
            "jue_block6",
            "vie_block6",
            "lun_block7",
            "mar_block7",
            "mie_block7",
            "jue_block7",
            "vie_block7",
            "lun_block8",
            "mar_block8",
            "mie_block8",
            "jue_block8",
            "vie_block8",
            "lun_block9",
            "mar_block9",
            "mie_block9",
            "jue_block9",
            "vie_block9",
        ]

        nombres_bloques = [
            "L01",
            "M01",
            "X01",
            "J01",
            "V01",
            "L02",
            "M02",
            "X02",
            "J02",
            "V02",
            "L03",
            "M03",
            "X03",
            "J03",
            "V03",
            "L04",
            "M04",
            "X04",
            "J04",
            "V04",
            "L05",
            "M05",
            "X05",
            "J05",
            "V05",
            "L06",
            "M06",
            "X06",
            "J06",
            "V06",
            "L07",
            "M07",
            "X07",
            "J07",
            "V07",
            "L08",
            "M08",
            "X08",
            "J08",
            "V08",
            "L09",
            "M09",
            "X09",
            "J09",
            "V09",
        ]

        # Obtener los nombres de asignatura y docente para cada bloque
        horarios = []
        for i, bloque in enumerate(bloques):
            nombre_bloque_html = nombres_bloque_html[i]
            nombre_bloque_db = nombres_bloques[i]
            asignatura = (
                bloque.asignatura_bloque.nombre_asignatura
                if bloque.asignatura_bloque
                else None
            )
            docente = (
                bloque.docente_bloque.nombre_completo()
                if bloque.docente_bloque
                else None
            )
            horarios.append((nombre_bloque_html, nombre_bloque_db, asignatura, docente))

        # Crear un diccionario con los horarios para pasar a la plantilla
        horarios_dict = {}
        for horario in horarios:
            horarios_dict[horario[0]] = {
                "nombre_bloque_db": horario[1],
                "asignatura": horario[2],
                "docente": horario[3],
            }

        return render(
            request,
            "nuevoshorizontes/portal_apoderado/ver_horario_hijo.html",
            {
                "apoderado": apoderado,
                "alumno": alumno,
                "horarios": horarios_dict,
                "bloques": bloques,
            },
        )

    else:
        return redirect("login_apoderado")


def asistencias_apoderado(request):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumnos = Alumno.objects.filter(apoderado_alumno=apoderado)

        asistencias_alumnos = []
        for alumno in alumnos:
            asistencias = Asistencia.objects.filter(alumno=alumno)
            presentes = asistencias.filter(tipo_asistencia_id=1).count()
            ausentes = asistencias.filter(tipo_asistencia_id=2).count()
            justificados = asistencias.filter(tipo_asistencia_id=3).count()
            total_asistencias = presentes + ausentes + justificados

            if total_asistencias > 0:
                porcentaje_asistencia = (
                    (presentes + justificados) / total_asistencias
                ) * 100
            else:
                porcentaje_asistencia = 0

            asistencias_alumnos.append(
                {
                    "alumno": alumno,
                    "total_asistencias": total_asistencias,
                    "presentes": presentes,
                    "ausentes": ausentes,
                    "justificados": justificados,
                    "porcentaje_asistencia": porcentaje_asistencia,
                }
            )

        return render(
            request,
            "nuevoshorizontes/portal_apoderado/asistencias_apoderado.html",
            {"apoderado": apoderado, "asistencias_alumnos": asistencias_alumnos},
        )
    else:
        return redirect("login_apoderado")


def notas_apoderado(request):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumnos = Alumno.objects.filter(apoderado_alumno=apoderado)
        return render(
            request,
            "nuevoshorizontes/portal_apoderado/notas_apoderado.html",
            {"apoderado": apoderado, "alumnos": alumnos},
        )

    else:
        return redirect("login_apoderado")


def listar_asignatura_hijos(request, rut_alumno):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumno = Alumno.objects.get(rut_alumno=rut_alumno)

        # Obtener el curso asignado al alumno
        curso_alumno = alumno.curso_alumno

        # Obtener los bloques relacionados con el curso del alumno que no estén en blanco y que tengan asignatura y docente
        bloques = Bloque.objects.filter(
            curso_bloque=curso_alumno,
            nombre_bloque__isnull=False,
            asignatura_bloque__isnull=False,
            docente_bloque__isnull=False,
        )

        # Obtener las asignaturas correspondientes a los bloques sin repetir
        asignaturas = sorted(
            set(bloque.asignatura_bloque for bloque in bloques),
            key=lambda x: x.nombre_asignatura,
        )

        return render(
            request,
            "nuevoshorizontes/portal_apoderado/lista_asignaturas_hijos.html",
            {"apoderado": apoderado, "alumno": alumno, "asignaturas": asignaturas},
        )

    else:
        return redirect("login_apoderado")


def notas_por_asignatura_apoderado(request, rut_alumno, id_asignatura):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumno = Alumno.objects.get(rut_alumno=rut_alumno)

        # Obtener las calificaciones del alumno en la asignatura seleccionada
        calificaciones = Calificacion.objects.filter(
            alumno=alumno, asignatura_id=id_asignatura
        )

        # Calcular el promedio de las notas
        total_notas = calificaciones.count()
        suma_notas = calificaciones.aggregate(Sum("valor")).get("valor__sum")
        promedio = suma_notas / total_notas if total_notas > 0 else 0

        return render(
            request,
            "nuevoshorizontes/portal_apoderado/notas_por_asignatura_hijos.html",
            {
                "apoderado": apoderado,
                "alumno": alumno,
                "calificaciones": calificaciones,
                "promedio": promedio,
            },
        )
    else:
        return redirect("login_apoderado")


def pagos_apoderado(request):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumnos = Alumno.objects.filter(apoderado_alumno=apoderado)

        return render(
            request,
            "nuevoshorizontes/portal_apoderado/pagos_apoderado.html",
            {
                "apoderado": apoderado,
                "alumnos": alumnos,
            },
        )
    else:
        return redirect("login_apoderado")


def listar_pagos_apoderado(request, rut_alumno):
    correo_apoderado = request.session.get("correo_apoderado", None)
    if correo_apoderado:
        apoderado = Apoderado.objects.get(correo_apoderado=correo_apoderado)
        alumno = Alumno.objects.get(rut_alumno=rut_alumno)
        pagos = Pagos_colegio.objects.all()

        return render(
            request,
            "nuevoshorizontes/portal_apoderado/listar_pagos_apoderado.html",
            {
                "apoderado": apoderado,
                "alumno": alumno,
                "pagos": pagos,
            },
        )
    else:
        return redirect("login_apoderado")


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


def curso_docente(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        # Busca un objeto Docente en la base de datos con correo_docente igual al valor obtenido anteriormente
        docente = Docente.objects.get(correo_docente=correo_docente)
        # Obtiene el primer curso relacionado con el docente
        curso = docente.curso_set.first()
        if curso:
            # Obtiene todos los objetos Alumno de la base de datos con curso_alumno igual al valor de curso
            alumnos = Alumno.objects.filter(curso_alumno=curso)
            # Obtiene el primer alumno de la lista de alumnos
            primer_alumno = alumnos.first()
        else:
            alumnos = []  # Establece una lista vacía
            primer_alumno = None  # Establece primer_alumno como None
        return render(
            request,
            "nuevoshorizontes/portal_docente/curso_docente.html",
            {"docente": docente, "alumnos": alumnos, "primer_alumno": primer_alumno},
        )
    else:
        return redirect("login_docente")


def asignaturas_docente(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        asignaturas = (
            docente.asignatura_set.all()
        )  # Obtener todas las asignaturas del docente
        return render(
            request,
            "nuevoshorizontes/portal_docente/asignaturas_docente.html",
            {
                "docente": docente,
                "asignaturas": asignaturas,
            },  # Pasar las asignaturas al template
        )
    else:
        return redirect("login_docente")


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
        if request.method == "POST":
            fecha = request.POST.get("fecha")
            if fecha:
                fecha = datetime.strptime(fecha, "%Y-%m-%d").date()
                asistencias = Asistencia.objects.filter(
                    alumno__curso_alumno__docente_curso=docente, fecha_asistencia=fecha
                )
                if asistencias:
                    return render(
                        request,
                        "nuevoshorizontes/portal_docente/asistencia/buscar_asistencia.html",
                        {"docente": docente, "asistencias": asistencias},
                    )
                else:
                    return render(
                        request,
                        "nuevoshorizontes/portal_docente/asistencia/buscar_asistencia.html",
                        {"docente": docente, "no_asistencias": True},
                    )
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
            fecha_ingresada = request.POST.get(
                "fecha"
            )  # Obtener la fecha ingresada desde el formulario
            fecha_asistencia = datetime.strptime(
                fecha_ingresada, "%Y-%m-%d"
            ).date()  # Convertir la fecha a un objeto de tipo `date`

            # Verificar si ya se registró la asistencia en la fecha especificada
            asistencia_existente = Asistencia.objects.filter(
                fecha_asistencia=fecha_asistencia,
                curso__docente_curso=docente,
            ).exists()

            if asistencia_existente:
                messages.error(request, "Ya se realizó la asistencia en esta fecha.")
                return redirect("agregar_asistencia")

            # Obtener la lista de cursos del docente
            cursos = Curso.objects.filter(docente_curso=docente)
            if cursos.exists():
                curso = cursos.first()
                alumnos = Alumno.objects.filter(curso_alumno=curso)
            else:
                alumnos = []

            # Guardar la asistencia de cada alumno
            for alumno in alumnos:
                tipo_asistencia_id = request.POST.get(str(alumno.rut_alumno))
                tipo_asistencia = Tipo_asis.objects.get(pk=tipo_asistencia_id)

                Asistencia.objects.create(
                    tipo_asistencia=tipo_asistencia,
                    fecha_asistencia=fecha_asistencia,
                    alumno=alumno,
                    curso=curso,  # Guardar el curso en el modelo de `Asistencia`
                    docente=docente,  # Guardar el docente en el modelo de `Asistencia`
                )

            messages.success(request, "Asistencia guardada exitosamente.")
            return redirect("asistencia_docente")

        estados_asistencia = Tipo_asis.objects.all()
        cursos = Curso.objects.filter(docente_curso=docente)
        if cursos.exists():
            curso = cursos.first()
            alumnos = Alumno.objects.filter(curso_alumno=curso)
        else:
            alumnos = []

        return render(
            request,
            "nuevoshorizontes/portal_docente/asistencia/agregar_asistencia.html",
            {
                "docente": docente,
                "alumnos": alumnos,
                "estados_asistencia": estados_asistencia,
            },
        )
    else:
        return redirect("login_docente")


def modificar_asistencia(request, rut_alumno):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        if request.method == "POST":
            tipo_asistencia_id = request.POST.get("tipo_asistencia")

            alumno = Alumno.objects.get(rut_alumno=rut_alumno)
            asistencia = Asistencia.objects.filter(alumno=alumno).first()

            if asistencia:
                asistencia.tipo_asistencia_id = tipo_asistencia_id
                asistencia.save()

                messages.success(
                    request, "La asistencia del alumno se ha modificado correctamente."
                )
            else:
                messages.error(request, "No se encontró la asistencia del alumno.")

            return redirect("asistencia_docente")

        alumno = Alumno.objects.get(rut_alumno=rut_alumno)
        estados_asistencia = Tipo_asis.objects.all()

        return render(
            request,
            "nuevoshorizontes/portal_docente/asistencia/modificar_asistencia.html",
            {
                "docente": docente,
                "alumno": alumno,
                "estados_asistencia": estados_asistencia,
                "asistencia_actual": alumno.asistencia_set.first(),
            },
        )
    else:
        return redirect("login_docente")


def notas_docente(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        # Puedes pasar el objeto 'apoderado' al contexto de renderizado
        return render(
            request,
            "nuevoshorizontes/portal_docente/notas_docente.html",
            {"docente": docente},
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_docente")


def agregar_notas(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        asignaturas = Asignatura.objects.filter(profesor_asignatura=docente)

        asignatura_seleccionada = None
        alumnos = None
        mostrar_tabla = False

        if request.method == "POST" and "ramos_hidden" in request.POST:
            asignatura_id = request.POST["ramos_hidden"]
            asignatura_seleccionada = Asignatura.objects.get(
                id_asignatura=asignatura_id
            )
            alumnos = Alumno.objects.filter(
                curso_alumno__bloque__asignatura_bloque=asignatura_seleccionada
            ).distinct()

            if "guardar" in request.POST:
                nombre_nota = request.POST["nombre_nota"]
                nombre_nota_lower = nombre_nota.lower()  # Convertir a minúsculas
                fecha_nota = date.today()

                # Validar si existe una nota con el mismo nombre (ignorando mayúsculas/minúsculas)
                if Calificacion.objects.filter(
                    Q(nombre_nota__iexact=nombre_nota)
                    | Q(nombre_nota__iexact=nombre_nota_lower)
                ).exists():
                    messages.error(request, "Ya existe una nota con el mismo nombre.")
                    mostrar_tabla = True  # Mostrar la tabla con los alumnos
                    return render(
                        request,
                        "nuevoshorizontes/portal_docente/notas/agregar_notas.html",
                        {
                            "docente": docente,
                            "asignaturas": asignaturas,
                            "asignatura_seleccionada": asignatura_seleccionada,
                            "alumnos": alumnos,
                            "mostrar_tabla": mostrar_tabla,
                        },
                    )

                for alumno in alumnos:
                    rut_alumno = alumno.rut_alumno
                    valor_nota = float(request.POST.get(rut_alumno, 0))

                    calificacion = Calificacion(
                        nombre_nota=nombre_nota,
                        valor=valor_nota,
                        fecha_nota=fecha_nota,
                        alumno=alumno,
                        asignatura=asignatura_seleccionada,
                    )
                    calificacion.save()

                messages.success(request, "Las notas se han agregado correctamente.")
                return redirect("notas_docente")

            mostrar_tabla = True

        return render(
            request,
            "nuevoshorizontes/portal_docente/notas/agregar_notas.html",
            {
                "docente": docente,
                "asignaturas": asignaturas,
                "asignatura_seleccionada": asignatura_seleccionada,
                "alumnos": alumnos,
                "mostrar_tabla": mostrar_tabla,
            },
        )
    else:
        return redirect("login_docente")


def buscar_notas(request):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        asignaturas = Asignatura.objects.filter(profesor_asignatura=docente)
        calificaciones = None

        if request.method == "POST" and "ramos" in request.POST:
            asignatura_id = request.POST["ramos"]
            asignatura_seleccionada = Asignatura.objects.get(
                id_asignatura=asignatura_id
            )

            if asignatura_seleccionada:
                calificaciones = Calificacion.objects.filter(
                    asignatura=asignatura_seleccionada
                )

        return render(
            request,
            "nuevoshorizontes/portal_docente/notas/buscar_notas.html",
            {
                "docente": docente,
                "asignaturas": asignaturas,
                "calificaciones": calificaciones,
            },
        )
    else:
        # El usuario no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect("login_docente")


def modificar_notas(request, rut_alumno, calificacion_id):
    correo_docente = request.session.get("correo_docente", None)
    if correo_docente:
        docente = Docente.objects.get(correo_docente=correo_docente)
        alumno = get_object_or_404(Alumno, rut_alumno=rut_alumno)
        calificacion = get_object_or_404(Calificacion, id=calificacion_id)

        if request.method == "POST":
            nueva_nota = float(request.POST.get("nota"))

            if nueva_nota == calificacion.valor:
                messages.error(
                    request,
                    "No se modifico la nota porque la nueva nota es igual a la nota actual.",
                )
                return redirect("notas_docente")

            calificacion.valor = nueva_nota
            calificacion.save()
            messages.success(
                request, "La nota se ha modificado correctamente."
            )  # Mensaje de éxito
            return redirect(
                "notas_docente"
            )  # Redirige a la página de búsqueda de notas
        else:
            messages.error(
                request, "Ha ocurrido un error al modificar la nota."
            )  # Mensaje de error

        return render(
            request,
            "nuevoshorizontes/portal_docente/notas/modificar_notas.html",
            {"docente": docente, "alumno": alumno, "calificacion": calificacion},
        )
    else:
        return redirect("login_docente")
