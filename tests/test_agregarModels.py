import pytest
from django.conf import settings
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
    Asignatura
)
from django.core.files.uploadedfile import SimpleUploadedFile
import datetime


# Agregar models BD


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


# Agregar administrador


@pytest.mark.django_db
def test_admin_creation():
    admin = Administrador.objects.create(
        nombre_admin="Jane",
        apellido_admin="Doe",
        correo_admin="jane@example.com",
        password="password",
    )
    assert admin.nombre_admin == "Jane"


# Agregar apoderado


@pytest.mark.django_db
def test_apoderado_creation():
    apodereado = Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="Jane",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="123 Street",
        telefono_apoderado=123456789,
        correo_apoderado="jane@example.com",
        password="password",
    )
    assert apodereado.rut_apoderado == "12345678-9"


# Agregar alumno


@pytest.mark.django_db
def test_alumno_creation():
    region = Region.objects.create(id_region=999, nombre_region="Región A")
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
    )
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="123 Street",
        telefono_sede=123456789,
        fotoSede=None,
        region_sede=region,
        comuna_sede=comuna,
    )

    # Crear algunos apoderados de ejemplo
    apoderado = Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="Jane",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="456 Avenue",
        telefono_apoderado=987654321,
        correo_apoderado="jane@example.com",
        password="password",
    )
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
    curso = Curso.objects.create(
        id_curso="2",
        nombre_curso="Curso B",
        docente_curso=docente,
        sala_curso=sala,
    )

    alumno = Alumno.objects.create(
        rut_alumno="98765432-1",
        nombre_alumno="Bob",
        appaterno_alumno="Smith",
        apmaterno_alumno="Doe",
        correo_alumno="bob@example.com",
        password="password",
        sede_alumno=sede,
        apoderado_alumno=apoderado,
        curso_alumno=curso,
    )
    assert alumno.rut_alumno == "98765432-1"


# Agregar docente


@pytest.mark.django_db
def test_docente_creation():
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
    docente = Docente.objects.create(
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
    assert docente.rut_docente == "12345678-9"


# Agregar sedes


@pytest.mark.django_db
def test_sede_creation():
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
    sede = Sede.objects.create(
        nombre_sede="Sede A",
        direccion_sede="Dirección A",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )
    assert sede.nombre_sede == "Sede A"


# Agregar postulaciones


@pytest.mark.django_db
def test_postulaciones_creation():
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
    assert postulacion1.nombres == "John"
    assert postulacion2.nombres == "Jane"


# Agregar noticias


@pytest.mark.django_db
def test_noticias_creation():
    # Crear una fecha de ejemplo
    fecha_publi = datetime.date(2023, 7, 3)
    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    noticia = Noticias.objects.create(
        titulo="Noticia 1",
        descripcion="Descripción de noticia",
        fecha_publi=fecha_publi,
        foto_noticia=imagen,
    )
    assert noticia.titulo == "Noticia 1"


# Agregar salas


@pytest.mark.django_db
def test_salas_creation():
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
    sala = Sala.objects.create(
        id_sala=99, nombre_sala="Sala A", sede_sala=sede, tipo_sala=tipo_sala
    )
    assert sala.id_sala == 99


#Agregar asignatura


@pytest.mark.django_db
def test_asignaturas_creation():
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
        sede_docente=sede
    )

    # Crear una instancia de Asignatura
    asignatura = Asignatura.objects.create(
        id_asignatura="ASG001",
        nombre_asignatura="Asignatura A",
        profesor_asignatura=docente
    )
    assert asignatura.id_asignatura == "ASG001"


#Agregar curso


@pytest.mark.django_db
def test_cursos_creation():
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
    curso = Curso.objects.create(
        id_curso="CUR001",
        nombre_curso="Curso A",
        docente_curso=docente,
        sala_curso=sala,
    )
    assert curso.id_curso == "CUR001"