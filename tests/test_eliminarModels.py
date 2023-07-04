import pytest
from nuevoshorizontes.models import (
    Administrador,
    Alumno,
    Curso,
    Docente,
    Apoderado,
    Noticias,
    Postulaciones,
    Region,
    Comuna,
    Sala,
    Sede,
    Tipo_Sala,
    Asignatura,
)
from django.conf import settings
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


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


# Eliminar administrador


class AdministradorTestCase(TestCase):
    def setUp(self):
        self.admin = Administrador.objects.create(
            nombre_admin="John",
            apellido_admin="Doe",
            correo_admin="john@example.com",
            password="password123",
        )

    def test_eliminar_administrador(self):
        # Verificar que el administrador existe antes de eliminarlo
        administrador = Administrador.objects.get(nombre_admin="John")
        self.assertEqual(administrador, self.admin)

        # Eliminar el administrador
        self.admin.delete()

        # Verificar que el administrador ha sido eliminado correctamente
        with self.assertRaises(Administrador.DoesNotExist):
            Administrador.objects.get(nombre_admin="John")


# Eliminar alumno


@pytest.mark.django_db
def test_eliminar_alumno():
    # Crear algunas sedes de ejemplo
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

    # Crear algunos alumnos de ejemplo asignados a la sede, apoderado, curso y sala
    alumno = Alumno.objects.create(
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

    # Verificar que la sede existe antes de eliminarla
    assert Alumno.objects.filter(rut_alumno=alumno.rut_alumno).exists()

    # Eliminar la sede
    alumno.delete()

    # Verificar que la sede ha sido eliminada correctamente
    assert not Alumno.objects.filter(rut_alumno=alumno.rut_alumno).exists()


# Eliminar docente


@pytest.mark.django_db
def test_eliminar_docente():
    region = Region.objects.create(id_region=999, nombre_region="Región de ejemplo")

    # Crear una comuna de ejemplo asociada a la región
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna de ejemplo", region_comuna=region
    )

    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )

    sede = Sede.objects.create(
        nombre_sede="Sede de ejemplo",
        direccion_sede="Dirección de ejemplo",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
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

    # Verificar que la sede existe antes de eliminarla
    assert Docente.objects.filter(rut_docente=docente.rut_docente).exists()

    # Eliminar la sede
    docente.delete()

    # Verificar que la sede ha sido eliminada correctamente
    assert not Docente.objects.filter(rut_docente=docente.rut_docente).exists()


# Eliminar apoderado


@pytest.mark.django_db
def test_eliminar_apoderado():
    # Crear un apoderado de ejemplo
    apoderado = Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="John",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="123 Street",
        telefono_apoderado=123456789,
        correo_apoderado="john@example.com",
        password="password",
    )

    # Verificar que la sede existe antes de eliminarla
    assert Apoderado.objects.filter(rut_apoderado=apoderado.rut_apoderado).exists()

    # Eliminar la sede
    apoderado.delete()

    # Verificar que la sede ha sido eliminada correctamente
    assert not Apoderado.objects.filter(rut_apoderado=apoderado.rut_apoderado).exists()


# Eliminar sedes


@pytest.mark.django_db
def test_eliminar_sede():
    # Crear una región de ejemplo
    region = Region.objects.create(id_region=999, nombre_region="Región de ejemplo")

    # Crear una comuna de ejemplo asociada a la región
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna de ejemplo", region_comuna=region
    )

    # Crear una sede de ejemplo con una imagen asociada, y relacionada a la región y comuna
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    sede = Sede.objects.create(
        nombre_sede="Sede de ejemplo",
        direccion_sede="Dirección de ejemplo",
        telefono_sede=123456789,
        fotoSede=imagen,
        region_sede=region,
        comuna_sede=comuna,
    )

    # Verificar que la sede existe antes de eliminarla
    assert Sede.objects.filter(id=sede.id).exists()

    # Eliminar la sede
    sede.delete()

    # Verificar que la sede ha sido eliminada correctamente
    assert not Sede.objects.filter(id=sede.id).exists()


# Eliminar noticias


@pytest.mark.django_db
def test_eliminar_noticia():
    # Crear una noticia de ejemplo con una imagen asociada
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    noticia = Noticias.objects.create(
        titulo="Noticia de prueba",
        descripcion="Esta es una noticia de prueba",
        fecha_publi="2023-07-03",
        foto_noticia=imagen,
    )

    # Verificar que la noticia existe antes de eliminarla
    assert Noticias.objects.filter(id=noticia.id).exists()

    # Eliminar la noticia
    noticia.delete()

    # Verificar que la noticia ha sido eliminada correctamente
    assert not Noticias.objects.filter(id=noticia.id).exists()


# Eliminar postulaciones


@pytest.mark.django_db
def test_eliminar_postulacion():
    # Crear una postulación de ejemplo
    postulacion = Postulaciones.objects.create(
        nombres="John",
        apellidos="Doe",
        email="john@example.com",
        telefono=123456789,
        sede="Sede ejemplo",
        mensaje="Mensaje de ejemplo",
    )

    # Verificar que la postulación existe antes de eliminarla
    assert Postulaciones.objects.filter(id=postulacion.id).exists()

    # Eliminar la postulación
    postulacion.delete()

    # Verificar que la postulación ha sido eliminada correctamente
    assert not Postulaciones.objects.filter(id=postulacion.id).exists()


# Eliminar sala


@pytest.mark.django_db
def test_eliminar_sala():
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

    # Verificar que la sala existe antes de eliminarla
    assert Sala.objects.filter(id_sala=sala.id_sala).exists()

    # Eliminar la sala
    sala.delete()

    # Verificar que la sala ha sido eliminada correctamente
    assert not Sala.objects.filter(id_sala=sala.id_sala).exists()


# Eliminar asignatura


@pytest.mark.django_db
def test_eliminar_asignatura():
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
    asignatura = Asignatura.objects.create(
        id_asignatura="ASG001",
        nombre_asignatura="Asignatura A",
        profesor_asignatura=docente,
    )

    # Verificar que la postulación existe antes de eliminarla
    assert Asignatura.objects.filter(id_asignatura=asignatura.id_asignatura).exists()

    # Eliminar la postulación
    asignatura.delete()

    # Verificar que la postulación ha sido eliminada correctamente
    assert not Asignatura.objects.filter(
        id_asignatura=asignatura.id_asignatura
    ).exists()


# Eliminar cursos


@pytest.mark.django_db
def test_eliminar_curso():
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

    # Verificar que la postulación existe antes de eliminarla
    assert Curso.objects.filter(id_curso=curso.id_curso).exists()

    # Eliminar la postulación
    curso.delete()

    # Verificar que la postulación ha sido eliminada correctamente
    assert not Curso.objects.filter(id_curso=curso.id_curso).exists()
