from django.shortcuts import redirect, render
import pytest
from nuevoshorizontes.models import (
    Administrador,
    Alumno,
    Apoderado,
    Docente,
    Sede,
    Region,
    Comuna,
    Curso,
    Tipo_Sala,
    Sala,
    Postulaciones,
    Noticias,
    Asignatura,
)
from nuevoshorizontes.views import (
    listar_admins,
    listar_alumnos,
    listar_apoderados,
    listar_docentes,
    listar_sedes_admin,
    listar_postulaciones,
    listar_noticias,
    listar_salas,
    listar_asignaturas,
    listar_cursos,
)
from django.conf import settings
from django.urls import reverse
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime
from django.core.paginator import Paginator

# Listar vista administrador


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.oracle",
        "NAME": "127.0.0.1:1521/xe",
        "USER": "C##NOVO",
        "PASSWORD": "NOVO2023",
        "TEST": {
            "USER": "default_test",
            "TBLSPACE": "default_test_tbls",
            "TBLSPACE_TMP": "default_test_tbls_tmp",
        },
    }


# Listar administradores


def listar_admins(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin_actual = Administrador.objects.get(correo_admin=correo_admin)
        if admin_actual.id != 1:
            admins = Administrador.objects.exclude(id=1).order_by("id")
        else:
            admins = Administrador.objects.all().order_by("id")

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


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_admins(rf):
    # Crea un administrador para utilizarlo en la sesión
    administrador_actual = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crea algunos administradores para listar
    Administrador.objects.create(
        nombre_admin="Jane",
        apellido_admin="Doe",
        correo_admin="jane@example.com",
        password="password",
    )
    Administrador.objects.create(
        nombre_admin="Bob",
        apellido_admin="Smith",
        correo_admin="bob@example.com",
        password="password",
    )

    # Definir la cantidad de elementos por página
    items_por_pagina = 10

    # Obtiene el queryset de administradores ordenados por algún campo
    admins = Administrador.objects.order_by("id")

    # Pagina el queryset ordenado
    paginator = Paginator(admins, items_por_pagina)

    # Crea un request mock con el administrador actual en la sesión
    request = rf.get(reverse("listar_admins"))
    request.session = {"correo_admin": administrador_actual.correo_admin}

    # Llama a la vista y obtiene la respuesta
    response = listar_admins(request)

    # Verifica que la vista retorne un código de estado exitoso (200)
    assert response.status_code == 200

    # Verifica que los administradores estén presentes en la respuesta
    assert "Jane" in response.content.decode()
    assert "Bob" in response.content.decode()


# Listar alumnos


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_alumnos(rf):
    # Crear un administrador de ejemplo
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    # Crear algunas sedes de ejemplo
    region = Region.objects.create(id_region=999, nombre_region="Región A")
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="123 Street",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )

    # Crear algunos apoderados de ejemplo
    apoderado1 = Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="Jane",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="456 Avenue",
        telefono_apoderado=987654321,
        correo_apoderado="jane@example.com",
        password="password",
    )
    apoderado2 = Apoderado.objects.create(
        rut_apoderado="98765432-1",
        nombre_apoderado="Bob",
        appaterno_apoderado="Smith",
        apmaterno_apoderado="Doe",
        direccion_apoderado="789 Road",
        telefono_apoderado=123456789,
        correo_apoderado="bob@example.com",
        password="password",
    )

    # Crear algunos cursos de ejemplo
    docente = Docente.objects.create(
        rut_docente="12345678-9",
        nombre_docente="John",
        appaterno_docente="Doe",
        apmaterno_docente="Smith",
        direccion_docente="123 Street",
        telefono_docente=123456789,
        correo_docente="john@example.com",
        password="password",
        sede_docente=sede,
    )
    tipo_sala = Tipo_Sala.objects.create(
        id_tipo_sala=999, nombre_tipo_sala="Tipo Sala A"
    )
    sala = Sala.objects.create(
        id_sala=999,
        nombre_sala="Sala A",
        sede_sala=sede,
        tipo_sala=tipo_sala,
    )
    curso1 = Curso.objects.create(
        id_curso="1",
        nombre_curso="Curso A",
        docente_curso=docente,
        sala_curso=sala,
    )
    curso2 = Curso.objects.create(
        id_curso="2",
        nombre_curso="Curso B",
        docente_curso=docente,
        sala_curso=sala,
    )

    # Crear algunos alumnos de ejemplo asignados a la sede, apoderado, curso y sala
    alumno1 = Alumno.objects.create(
        rut_alumno="12345678-9",
        nombre_alumno="Alice",
        appaterno_alumno="Doe",
        apmaterno_alumno="Smith",
        correo_alumno="alice@example.com",
        password="password",
        sede_alumno=sede,
        apoderado_alumno=apoderado1,
        curso_alumno=curso1,
    )
    alumno2 = Alumno.objects.create(
        rut_alumno="98765432-1",
        nombre_alumno="Bob",
        appaterno_alumno="Smith",
        apmaterno_alumno="Doe",
        correo_alumno="bob@example.com",
        password="password",
        sede_alumno=sede,
        apoderado_alumno=apoderado2,
        curso_alumno=curso2,
    )

    # Crear una solicitud GET simulada para listar los alumnos
    request = rf.get(reverse("listar_alumnos"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Llamar a la vista y obtener la respuesta
    response = listar_alumnos(request)

    # Verificar que la respuesta sea exitosa (código 200)
    assert response.status_code == 200


def listar_alumnos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)

        # Obtener el queryset de alumnos y ordénalo por nombre
        alumnos = Alumno.objects.order_by("nombre_alumno")

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


# Listar docente


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_docentes(rf):
    # Crear un administrador de ejemplo
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    # Crear algunas sedes de ejemplo
    region = Region.objects.create(id_region=999, nombre_region="Región A")
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="123 Street",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )

    # Crear algunos docentes de ejemplo asignados a la sede
    docente1 = Docente.objects.create(
        rut_docente="12345678-9",
        nombre_docente="Jane",
        appaterno_docente="Doe",
        apmaterno_docente="Smith",
        direccion_docente="456 Avenue",
        telefono_docente=987654321,
        correo_docente="jane@example.com",
        password="password",
        sede_docente=sede,
    )
    docente2 = Docente.objects.create(
        rut_docente="98765432-1",
        nombre_docente="Bob",
        appaterno_docente="Smith",
        apmaterno_docente="Doe",
        direccion_docente="789 Road",
        telefono_docente=123456789,
        correo_docente="bob@example.com",
        password="password",
        sede_docente=sede,
    )

    # Crear un request mock con el administrador en la sesión
    request = rf.get(reverse("listar_docentes"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Llamar a la vista y obtener la respuesta
    response = listar_docentes(request)

    # Verificar que la vista retorne un código de estado exitoso (200)
    assert response.status_code == 200


def listar_docentes(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        docentes = Docente.objects.order_by("nombre_docente")

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


# Listar apoderados


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_apoderados(rf):
    # Crea un administrador para utilizarlo en la sesión
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crea algunos apoderados para listar
    Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="Jane",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="123 Street",
        telefono_apoderado=123456789,
        correo_apoderado="jane@example.com",
        password="password",
    )
    Apoderado.objects.create(
        rut_apoderado="98765432-1",
        nombre_apoderado="Bob",
        appaterno_apoderado="Smith",
        apmaterno_apoderado="Doe",
        direccion_apoderado="456 Avenue",
        telefono_apoderado=987654321,
        correo_apoderado="bob@example.com",
        password="password",
    )

    # Crea un request mock con el administrador en la sesión
    request = rf.get(reverse("listar_apoderados"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Llama a la vista y obtiene la respuesta
    response = listar_apoderados(request)

    # Verifica que la vista retorne un código de estado exitoso (200)
    assert response.status_code == 200


def listar_apoderados(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        apoderados = Apoderado.objects.order_by("nombre_apoderado")

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


# Listar sedes


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_sedes(rf):
    # Crear un administrador de ejemplo
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    # Crear algunas regiones y comunas de ejemplo
    region = Region.objects.create(id_region=999, nombre_region="Región A")
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )

    # Crear algunas sedes para listar
    Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="Dirección A",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )
    Sede.objects.create(
        nombre_sede="Sede B",
        direccion_sede="Dirección B",
        telefono_sede=987654321,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )

    # Crear un request mock con el administrador en la sesión
    request = rf.get(reverse("listar_sedes"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Llamar a la vista y obtener la respuesta
    response = listar_sedes_admin(request)

    # Verificar que la vista retorne un código de estado exitoso (200)
    assert response.status_code == 200

    # Verificar que las sedes estén presentes en la respuesta
    assert "Sede A" in response.content.decode()
    assert "Sede B" in response.content.decode()


# Listar postulaciones


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_postulaciones(rf):
    # Crear un administrador de ejemplo
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crear algunas postulaciones de ejemplo
    postulacion1 = Postulaciones.objects.create(
        nombres="John",
        apellidos="Doe",
        email="john@example.com",
        telefono=123456789,
        sede="Sede A",
        mensaje="Mensaje de postulación 1",
    )
    postulacion2 = Postulaciones.objects.create(
        nombres="Jane",
        apellidos="Smith",
        email="jane@example.com",
        telefono=987654321,
        sede="Sede B",
        mensaje="Mensaje de postulación 2",
    )

    # Crear un request mock con el administrador en la sesión
    request = rf.get(reverse("listar_postulaciones"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Llamar a la vista y obtener la respuesta
    response = listar_postulaciones(request)

    # Verificar que la vista retorne un código de estado exitoso (200)
    assert response.status_code == 200

    # Verificar que las postulaciones estén presentes en la respuesta
    assert "John" in response.content.decode()
    assert "Jane" in response.content.decode()
    assert "Doe" in response.content.decode()
    assert "Smith" in response.content.decode()
    assert "john@example.com" in response.content.decode()
    assert "jane@example.com" in response.content.decode()
    assert "123456789" in response.content.decode()
    assert "987654321" in response.content.decode()
    assert "Sede A" in response.content.decode()
    assert "Sede B" in response.content.decode()
    assert "Mensaje de postulación 1" in response.content.decode()
    assert "Mensaje de postulación 2" in response.content.decode()


def listar_postulaciones(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        postulaciones = Postulaciones.objects.order_by("id")

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


# Listar noticias


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_noticias(rf):
    # Create a request factory

    # Create an example administrator
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Create a sample date
    fecha_publi = datetime.date(2023, 7, 3)

    # Create a sample image
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    # Create some example news
    noticia1 = Noticias.objects.create(
        titulo="Noticia 1",
        descripcion="Descripción de noticia 1",
        fecha_publi=fecha_publi,
        foto_noticia=imagen,
    )
    noticia2 = Noticias.objects.create(
        titulo="Noticia 2",
        descripcion="Descripción de noticia 2",
        fecha_publi=fecha_publi,
        foto_noticia=imagen,
    )

    # Create a request with the administrator in the session
    request = rf.get(reverse("listar_noticias"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Call the view function and get the response
    response = listar_noticias(request)

    # Verify that the view returns a successful status code (200)
    assert response.status_code == 200

    # Verify that the news is present in the response
    assert "Noticia 1" in response.content.decode()
    assert "Noticia 2" in response.content.decode()
    assert "Descripción de noticia 1" in response.content.decode()
    assert "Descripción de noticia 2" in response.content.decode()


# Listar salas


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_salas(rf):
    # Create an example administrator
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crear una instancia de Región
    region = Region.objects.create(id_region=999, nombre_region="Región A")

    # Crear una instancia de Comuna
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )

    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    # Crear una instancia de Sede
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="Dirección A",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )

    # Crear una instancia de Tipo_Sala
    tipo_sala = Tipo_Sala.objects.create(
        id_tipo_sala=99, nombre_tipo_sala="Tipo Sala A"
    )

    # Crear una instancia de Sala
    sala1 = Sala.objects.create(
        id_sala=99, nombre_sala="Sala A", sede_sala=sede, tipo_sala=tipo_sala
    )

    sala2 = Sala.objects.create(
        id_sala=100, nombre_sala="Sala B", sede_sala=sede, tipo_sala=tipo_sala
    )

    # Create a request with the administrator in the session
    request = rf.get(reverse("listar_salas"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Call the view function and get the response
    response = listar_salas(request)

    # Verify that the view returns a successful status code (200)
    assert response.status_code == 200


def listar_salas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        salas = Sala.objects.order_by("id_sala")
        
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


# Listar asignaturas


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_asignaturas(rf):
    # Create an example administrator
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crear una instancia de Región
    region = Region.objects.create(id_region=999, nombre_region="Región A")

    # Crear una instancia de Comuna
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )

    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    # Crear una instancia de Sede
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="Dirección A",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )
    # Crear una instancia de Docente
    docente = Docente.objects.create(
        rut_docente="12345678-9",
        nombre_docente="Nombre Docente",
        appaterno_docente="Apellido Paterno",
        apmaterno_docente="Apellido Materno",
        direccion_docente="Dirección",
        telefono_docente=123456789,
        correo_docente="correo@docente.com",
        password="password",
        sede_docente=sede,
    )

    # Crear una instancia de Asignatura
    asignatura1 = Asignatura.objects.create(
        id_asignatura="ASG001",
        nombre_asignatura="Asignatura A",
        profesor_asignatura=docente,
    )

    asignatura2 = Asignatura.objects.create(
        id_asignatura="ASG002",
        nombre_asignatura="Asignatura B",
        profesor_asignatura=docente,
    )

    # Create a request with the administrator in the session
    request = rf.get(reverse("listar_asignaturas"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Call the view function and get the response
    response = listar_asignaturas(request)

    # Verify that the view returns a successful status code (200)
    assert response.status_code == 200


def listar_asignaturas(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        asignaturas = Asignatura.objects.order_by("id_asignatura")
        
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


# Listar cursos


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.mark.django_db
def test_listar_cursos(rf):
    # Crear un administrador de ejemplo
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="admin@example.com",
        password="password",
    )

    # Crear una instancia de Región
    region = Region.objects.create(id_region=999, nombre_region="Región A")

    # Crear una instancia de Comuna
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )

    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    # Crear una instancia de Sede
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="Dirección A",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )
    # Crear una instancia de Docente
    docente = Docente.objects.create(
        rut_docente="12345678-9",
        nombre_docente="Nombre Docente",
        appaterno_docente="Apellido Paterno",
        apmaterno_docente="Apellido Materno",
        direccion_docente="Dirección",
        telefono_docente=123456789,
        correo_docente="correo@docente.com",
        password="password",
        sede_docente=sede,
    )

    # Crear una instancia de Tipo_Sala
    tipo_sala = Tipo_Sala.objects.create(
        id_tipo_sala=99, nombre_tipo_sala="Tipo Sala A"
    )

    # Crear una instancia de Sala
    sala = Sala.objects.create(
        id_sala=99, nombre_sala="Sala A", sede_sala=sede, tipo_sala=tipo_sala
    )

    # Crear una instancia de Curso
    curso1 = Curso.objects.create(
        id_curso="CUR001",
        nombre_curso="Curso A",
        docente_curso=docente,
        sala_curso=sala,
    )

    curso2 = Curso.objects.create(
        id_curso="CUR002",
        nombre_curso="Curso B",
        docente_curso=docente,
        sala_curso=sala,
    )

    # Crear un request mock con el administrador en la sesión
    request = rf.get(reverse("listar_cursos"))
    request.session = {"correo_admin": administrador.correo_admin}

    # Llamar a la vista y obtener la respuesta
    response = listar_cursos(request)

    # Verificar que la vista retorne un código de estado exitoso (200)
    assert response.status_code == 200

    # Verificar que los cursos estén presentes en la respuesta
    assert "CUR001" in response.content.decode()
    assert "Curso A" in response.content.decode()
    assert "CUR002" in response.content.decode()
    assert "Curso B" in response.content.decode()


def listar_cursos(request):
    correo_admin = request.session.get("correo_admin", None)
    if correo_admin:
        admin = Administrador.objects.get(correo_admin=correo_admin)
        cursos = Curso.objects.order_by("id_curso")
        
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
