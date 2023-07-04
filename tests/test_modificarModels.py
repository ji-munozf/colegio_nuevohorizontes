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
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile


# Modificar models BD


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


# Modificar Admin


@pytest.mark.django_db
def test_modificar_administrador():
    # Crear una instancia de Administrador
    administrador = Administrador.objects.create(
        nombre_admin="John",
        apellido_admin="Doe",
        correo_admin="john.doe@example.com",
        password="password",
    )

    # Datos actualizados para el administrador
    datos_actualizados = {
        "nombre_admin": "Jane",
        "apellido_admin": "Doe",
        "correo_admin": "jane.doe@example.com",
        "password": "new_password"
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Administrador
    administrador.nombre_admin = datos_actualizados["nombre_admin"]
    administrador.apellido_admin = datos_actualizados["apellido_admin"]
    administrador.correo_admin = datos_actualizados["correo_admin"]
    administrador.password = datos_actualizados["password"]
    administrador.save()

    # Volver a obtener el administrador de la base de datos
    administrador_actualizado = Administrador.objects.get(id=administrador.id)

    # Verificar que los campos se hayan actualizado correctamente
    assert administrador_actualizado.nombre_admin == datos_actualizados["nombre_admin"]
    assert (
        administrador_actualizado.apellido_admin == datos_actualizados["apellido_admin"]
    )
    assert administrador_actualizado.correo_admin == datos_actualizados["correo_admin"]
    assert administrador_actualizado.password == datos_actualizados["password"]


# Modificar alumno


@pytest.mark.django_db
def test_modificar_alumno():
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    # Crear algunas sedes de ejemplo
    region = Region.objects.create(id_region=999, nombre_region="Región A")
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
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

    # Crear una instancia de Apoderado
    apoderado = Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="John",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="Dirección A",
        telefono_apoderado=123456789,
        correo_apoderado="john.doe@example.com",
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

    # Crear una instancia de Curso
    curso = Curso.objects.create(
        id_curso="C001", nombre_curso="Curso A", docente_curso=docente, sala_curso=sala
    )

    # Crear una instancia de Alumno
    alumno = Alumno.objects.create(
        rut_alumno="12345678-9",
        nombre_alumno="John",
        appaterno_alumno="Doe",
        apmaterno_alumno="Smith",
        correo_alumno="john.doe@example.com",
        password="password",
        sede_alumno=sede,
        apoderado_alumno=apoderado,
        curso_alumno=curso,
    )

    # Datos actualizados para el alumno
    datos_actualizados = {
        "rut_alumno": "98765432-1",
        "nombre_alumno": "Jane",
        "appaterno_alumno": "Doe",
        "apmaterno_alumno": "Smith",
        "correo_alumno": "jane.doe@example.com",
        "password": "new_password",
        "sede_alumno": sede,
        "apoderado_alumno": apoderado,
        "curso_alumno": curso
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Alumno
    alumno.rut_alumno = datos_actualizados["rut_alumno"]
    alumno.nombre_alumno = datos_actualizados["nombre_alumno"]
    alumno.appaterno_alumno = datos_actualizados["appaterno_alumno"]
    alumno.apmaterno_alumno = datos_actualizados["apmaterno_alumno"]
    alumno.correo_alumno = datos_actualizados["correo_alumno"]
    alumno.password = datos_actualizados["password"]
    alumno.sede_alumno = datos_actualizados["sede_alumno"]
    alumno.apoderado_alumno = datos_actualizados["apoderado_alumno"]
    alumno.curso_alumno = datos_actualizados["curso_alumno"]
    alumno.save()

    # Volver a obtener el alumno de la base de datos
    alumno_actualizado = Alumno.objects.get(rut_alumno=alumno.rut_alumno)

    # Verificar que los campos se hayan actualizado correctamente
    assert alumno_actualizado.rut_alumno == datos_actualizados["rut_alumno"]
    assert alumno_actualizado.nombre_alumno == datos_actualizados["nombre_alumno"]
    assert alumno_actualizado.appaterno_alumno == datos_actualizados["appaterno_alumno"]
    assert alumno_actualizado.apmaterno_alumno == datos_actualizados["apmaterno_alumno"]
    assert alumno_actualizado.correo_alumno == datos_actualizados["correo_alumno"]
    assert alumno_actualizado.password == datos_actualizados["password"]
    assert alumno_actualizado.sede_alumno == datos_actualizados["sede_alumno"]
    assert alumno_actualizado.apoderado_alumno == datos_actualizados["apoderado_alumno"]
    assert alumno_actualizado.curso_alumno == datos_actualizados["curso_alumno"]
    # Aquí puedes incluir las verificaciones para otros campos, si es necesario


# Modificar docente


@pytest.mark.django_db
def test_modificar_docente():
    imagen = SimpleUploadedFile(
        name="test_image.jpg", content=b"", content_type="image/jpeg"
    )
    # Crear algunas sedes de ejemplo
    region = Region.objects.create(id_region=999, nombre_region="Región A")
    comuna = Comuna.objects.create(
        id_comuna=999, nombre_comuna="Comuna A", region_comuna=region
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
        nombre_docente="Nombre A",
        appaterno_docente="Apellido Paterno A",
        apmaterno_docente="Apellido Materno A",
        direccion_docente="Dirección A",
        telefono_docente=123456789,
        correo_docente="correo@docente.com",
        password="password",
        sede_docente=sede,
    )

    # Datos actualizados para el docente
    datos_actualizados = {
        "rut_docente": "98765432-1",
        "nombre_docente": "Nombre B",
        "appaterno_docente": "Apellido Paterno B",
        "apmaterno_docente": "Apellido Materno B",
        "direccion_docente": "Dirección B",
        "telefono_docente": 987654321,
        "correo_docente": "correo_actualizado@docente.com",
        "password": "nueva_contraseña",
        "sede_docente": sede
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Docente
    docente.rut_docente = datos_actualizados["rut_docente"]
    docente.nombre_docente = datos_actualizados["nombre_docente"]
    docente.appaterno_docente = datos_actualizados["appaterno_docente"]
    docente.apmaterno_docente = datos_actualizados["apmaterno_docente"]
    docente.direccion_docente = datos_actualizados["direccion_docente"]
    docente.telefono_docente = datos_actualizados["telefono_docente"]
    docente.correo_docente = datos_actualizados["correo_docente"]
    docente.password = datos_actualizados["password"]
    docente.sede_docente = datos_actualizados["sede_docente"]
    docente.save()

    # Volver a obtener el docente de la base de datos
    docente_actualizado = Docente.objects.get(rut_docente=docente.rut_docente)

    # Verificar que los campos se hayan actualizado correctamente
    assert docente_actualizado.rut_docente == datos_actualizados["rut_docente"]
    assert docente_actualizado.nombre_docente == datos_actualizados["nombre_docente"]
    assert (
        docente_actualizado.appaterno_docente == datos_actualizados["appaterno_docente"]
    )
    assert (
        docente_actualizado.apmaterno_docente == datos_actualizados["apmaterno_docente"]
    )
    assert (
        docente_actualizado.direccion_docente == datos_actualizados["direccion_docente"]
    )
    assert (
        docente_actualizado.telefono_docente == datos_actualizados["telefono_docente"]
    )
    assert docente_actualizado.correo_docente == datos_actualizados["correo_docente"]
    assert docente_actualizado.password == datos_actualizados["password"]
    assert docente_actualizado.sede_docente == datos_actualizados["sede_docente"]
    # Aquí puedes incluir las verificaciones para otros campos, si es necesario


# Modificar apoderados


@pytest.mark.django_db
def test_modificar_apoderado():
    # Crear una instancia de Apoderado
    apoderado = Apoderado.objects.create(
        rut_apoderado="12345678-9",
        nombre_apoderado="John",
        appaterno_apoderado="Doe",
        apmaterno_apoderado="Smith",
        direccion_apoderado="Dirección A",
        telefono_apoderado=123456789,
        correo_apoderado="john.doe@example.com",
        password="password",
    )

    # Datos actualizados para el apoderado
    datos_actualizados = {
        "rut_apoderado": "98765432-1",
        "nombre_apoderado": "Jane",
        "appaterno_apoderado": "Doe",
        "apmaterno_apoderado": "Smith",
        "direccion_apoderado": "Dirección B",
        "telefono_apoderado": 987654321,
        "correo_apoderado": "jane.doe@example.com",
        "password": "new_password"
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Apoderado
    apoderado.rut_apoderado = datos_actualizados["rut_apoderado"]
    apoderado.nombre_apoderado = datos_actualizados["nombre_apoderado"]
    apoderado.appaterno_apoderado = datos_actualizados["appaterno_apoderado"]
    apoderado.apmaterno_apoderado = datos_actualizados["apmaterno_apoderado"]
    apoderado.direccion_apoderado = datos_actualizados["direccion_apoderado"]
    apoderado.telefono_apoderado = datos_actualizados["telefono_apoderado"]
    apoderado.correo_apoderado = datos_actualizados["correo_apoderado"]
    apoderado.password = datos_actualizados["password"]
    apoderado.save()

    # Volver a obtener el apoderado de la base de datos
    apoderado_actualizado = Apoderado.objects.get(rut_apoderado=apoderado.rut_apoderado)

    # Verificar que los campos se hayan actualizado correctamente
    assert apoderado_actualizado.rut_apoderado == datos_actualizados["rut_apoderado"]
    assert (
        apoderado_actualizado.nombre_apoderado == datos_actualizados["nombre_apoderado"]
    )
    assert (
        apoderado_actualizado.appaterno_apoderado
        == datos_actualizados["appaterno_apoderado"]
    )
    assert (
        apoderado_actualizado.apmaterno_apoderado
        == datos_actualizados["apmaterno_apoderado"]
    )
    assert (
        apoderado_actualizado.direccion_apoderado
        == datos_actualizados["direccion_apoderado"]
    )
    assert (
        apoderado_actualizado.telefono_apoderado
        == datos_actualizados["telefono_apoderado"]
    )
    assert (
        apoderado_actualizado.correo_apoderado == datos_actualizados["correo_apoderado"]
    )
    assert apoderado_actualizado.password == datos_actualizados["password"]
    # Aquí puedes incluir las verificaciones para otros campos, si es necesario


# Modificar postulaciones


@pytest.mark.django_db
def test_modificar_postulacion():
    # Crear una instancia de Postulaciones
    postulacion = Postulaciones.objects.create(
        nombres="John",
        apellidos="Doe",
        email="john.doe@example.com",
        telefono=123456789,
        sede="Sede Principal",
        mensaje="Hola, me gustaría postular para un trabajo.",
    )

    # Datos actualizados para la postulación
    datos_actualizados = {
        "nombres": "Jane",
        "apellidos": "Doe",
        "email": "jane.doe@example.com",
        "telefono": 987654321,
        "sede": "Sede Secundaria",
        "mensaje": "Hola, quiero modificar mi postulación."
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Postulaciones
    postulacion.nombres = datos_actualizados["nombres"]
    postulacion.apellidos = datos_actualizados["apellidos"]
    postulacion.email = datos_actualizados["email"]
    postulacion.telefono = datos_actualizados["telefono"]
    postulacion.sede = datos_actualizados["sede"]
    postulacion.mensaje = datos_actualizados["mensaje"]
    postulacion.save()

    # Volver a obtener la postulación de la base de datos
    postulacion_actualizada = Postulaciones.objects.get(id=postulacion.id)

    # Verificar que los campos se hayan actualizado correctamente
    assert postulacion_actualizada.nombres == datos_actualizados["nombres"]
    assert postulacion_actualizada.apellidos == datos_actualizados["apellidos"]
    assert postulacion_actualizada.email == datos_actualizados["email"]
    assert postulacion_actualizada.telefono == datos_actualizados["telefono"]
    assert postulacion_actualizada.sede == datos_actualizados["sede"]
    assert postulacion_actualizada.mensaje == datos_actualizados["mensaje"]


# Modificar noticias


@pytest.mark.django_db
def test_modificar_noticia():
    # Crear una instancia de Noticias
    noticia = Noticias.objects.create(
        titulo="Título original",
        descripcion="Descripción original",
        fecha_publi="2023-01-01",
        foto_noticia=None,
    )

    # Datos actualizados para la noticia
    datos_actualizados = {
        "titulo": "Título actualizado",
        "descripcion": "Descripción actualizada",
        "fecha_publi": "2023-02-01",
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Noticias
    noticia.titulo = datos_actualizados["titulo"]
    noticia.descripcion = datos_actualizados["descripcion"]
    noticia.fecha_publi = datos_actualizados["fecha_publi"]
    noticia.save()

    # Volver a obtener la noticia de la base de datos
    noticia_actualizada = Noticias.objects.get(id=noticia.id)

    # Verificar que los campos se hayan actualizado correctamente
    assert noticia_actualizada.titulo == datos_actualizados["titulo"]
    assert noticia_actualizada.descripcion == datos_actualizados["descripcion"]
    assert (
        noticia_actualizada.fecha_publi.strftime("%Y-%m-%d")
        == datos_actualizados["fecha_publi"]
    )


# Modificar sedes


@pytest.mark.django_db
def test_modificar_sede():
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

    # Datos actualizados para la sede
    datos_actualizados = {
        "nombre_sede": "Sede B",
        "direccion_sede": "Dirección B",
        "telefono_sede": 987654321,
        "region_sede": region,
        "comuna_sede": comuna,
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Sede
    sede.nombre_sede = datos_actualizados["nombre_sede"]
    sede.direccion_sede = datos_actualizados["direccion_sede"]
    sede.telefono_sede = datos_actualizados["telefono_sede"]
    sede.region_sede = datos_actualizados["region_sede"]
    sede.comuna_sede = datos_actualizados["comuna_sede"]
    sede.save()

    # Volver a obtener la sede de la base de datos
    sede_actualizada = Sede.objects.get(id=sede.id)

    # Verificar que los campos se hayan actualizado correctamente
    assert sede_actualizada.nombre_sede == datos_actualizados["nombre_sede"]
    assert sede_actualizada.direccion_sede == datos_actualizados["direccion_sede"]
    assert sede_actualizada.telefono_sede == datos_actualizados["telefono_sede"]
    assert sede_actualizada.region_sede == datos_actualizados["region_sede"]
    assert sede_actualizada.comuna_sede == datos_actualizados["comuna_sede"]


# Modificar sala


@pytest.mark.django_db
def test_modificar_sala():
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

    # Datos actualizados para la sala
    datos_actualizados = {
        "id_sala": 99,
        "nombre_sala": "Sala B",
        "sede_sala": sede,
        "tipo_sala": tipo_sala
        # Aquí puedes incluir los datos actualizados para otros campos, si es necesario
    }

    # Modificar la instancia de Sala
    sala.id_sala = datos_actualizados["id_sala"]
    sala.nombre_sala = datos_actualizados["nombre_sala"]
    sala.sede_sala = datos_actualizados["sede_sala"]
    sala.tipo_sala = datos_actualizados["tipo_sala"]
    sala.save()

    # Volver a obtener la sala de la base de datos
    sala_actualizada = Sala.objects.get(id_sala=sala.id_sala)

    # Verificar que los campos se hayan actualizado correctamente
    assert sala_actualizada.id_sala == datos_actualizados["id_sala"]
    assert sala_actualizada.nombre_sala == datos_actualizados["nombre_sala"]
    assert sala_actualizada.sede_sala == datos_actualizados["sede_sala"]
    assert sala_actualizada.tipo_sala == datos_actualizados["tipo_sala"]


# Modificar asignatura


@pytest.mark.django_db
def test_modificar_asignatura():
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

    # Modificar la instancia de Asignatura
    asignatura.id_asignatura = "ASG002"
    asignatura.nombre_asignatura = "Asignatura B"
    asignatura.profesor_asignatura = docente
    asignatura.save()

    # Volver a obtener la asignatura de la base de datos
    asignatura_actualizada = Asignatura.objects.get(
        id_asignatura=asignatura.id_asignatura
    )

    # Verificar que los campos se hayan actualizado correctamente
    assert asignatura_actualizada.id_asignatura == "ASG002"
    assert asignatura_actualizada.nombre_asignatura == "Asignatura B"
    assert asignatura_actualizada.profesor_asignatura == docente


# Modificar cursos


@pytest.mark.django_db
def test_modificar_curso():
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

    # Modificar la instancia de Curso
    curso.id_curso = "CUR002"
    curso.nombre_curso = "Curso B"
    curso.docente_curso = docente
    curso.sala_curso = sala
    curso.save()

    # Volver a obtener el curso de la base de datos
    curso_actualizado = Curso.objects.get(id_curso=curso.id_curso)

    # Verificar que los campos se hayan actualizado correctamente
    assert curso_actualizado.id_curso == "CUR002"
    assert curso_actualizado.nombre_curso == "Curso B"
    assert curso_actualizado.docente_curso == docente
    assert curso_actualizado.sala_curso == sala
