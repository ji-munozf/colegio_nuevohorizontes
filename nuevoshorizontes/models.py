from django.db import models

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, verbose_name="ID región")
    nombre_region = models.CharField(max_length=15, verbose_name="Nombre")

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, verbose_name="ID comuna")
    nombre_comuna = models.CharField(max_length=15, verbose_name="Nombre")
    region_comuna = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región")

    def __str__(self):
        return self.nombre_comuna

class Sede(models.Model):
    id_sede = models.IntegerField(primary_key=True, verbose_name="ID sede")
    nombre_sede = models.CharField(max_length=15, verbose_name="Nombre")
    direccion_sede = models.CharField(max_length=25, verbose_name="Dirección")
    telefono_sede = models.IntegerField(verbose_name="Teléfono")
    fotoSede = models.ImageField(upload_to="sedes", null=True,verbose_name="Imagen de la sede")
    comuna_sede = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna")

    def __str__(self):
        return self.nombre_sede

class Tipo_Sala(models.Model):
    id_tipo_sala = models.IntegerField(primary_key=True, verbose_name="ID tipo sala")
    nombre_tipo_sala = models.CharField(max_length=12, verbose_name="Nombre")

    def __str__(self):
        return self.nombre_tipo_sala

class Sala(models.Model): 
    id_sala = models.IntegerField(primary_key=True, verbose_name="ID de la sala")
    nombre_sala = models.CharField(max_length=10, verbose_name="Nombre")
    sede_sala = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede asignado")
    tipo_sala = models.ForeignKey(Tipo_Sala, on_delete=models.CASCADE, verbose_name="Tipo sala")

    def __str__(self):
        return self.nombre_sala

class Docente(models.Model):
    rut_docente = models.CharField(primary_key=True, max_length=12, verbose_name="Rut")
    nombre_docente = models.CharField(max_length=15, verbose_name="Nombres")
    appaterno_docente = models.CharField(max_length=30, verbose_name="Apellido paterno")
    apmaterno_docente = models.CharField(max_length=30, verbose_name="Apellido materno")
    direccion_docente = models.CharField(max_length=30, verbose_name="Dirección")
    telefono_docente = models.IntegerField(verbose_name="Teléfono")
    correo_docente = models.CharField(max_length=30, verbose_name="Correo electrónico")
    password = models.CharField(max_length=125, verbose_name="Contraseña")
    sede_docente = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede asignado")
    
    def __str__(self):
        return self.nombre_docente + " " + self.appaterno_docente + " " + self.apmaterno_docente + " RUT: " + self.rut_docente

class Curso(models.Model):
    id_curso = models.IntegerField(primary_key=True, verbose_name="ID del curso")
    nombre_curso = models.CharField(max_length=30, verbose_name="Nombre del curso")
    docente_curso = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name="Docente asignado")

    def __str__(self):
        return self.nombre_curso

class Asignatura(models.Model):
    id_asignatura = models.CharField(max_length=6, primary_key=True, verbose_name="ID de la asignatura")
    nombre_asignatura = models.CharField(max_length=12, verbose_name="Nombre")
    curso_asignatura = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso asignado")
    docente_asignatura = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name="Docente asignado")

    def __str__(self):
        return self.nombre_asignatura

class Horario(models.Model):
    id_horario = models.IntegerField(primary_key=True, verbose_name="ID del horario")
    dia_horario = models.CharField(max_length=9, verbose_name="Días")
    curso_horario = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso asignado")

    def __str__(self):
        return self.dia_horario

class Bloque(models.Model):
    id_bloque = models.IntegerField(primary_key=True, verbose_name="ID del bloque")
    horario_bloque = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name="Horario bloque")
    asignatura_bloque = models.ForeignKey(Asignatura, on_delete=models.CASCADE, verbose_name="Bloque de la asignatura")
    sala_bloque = models.ForeignKey(Sala, on_delete=models.CASCADE, verbose_name="Bloque de la sala")

    def __str__(self):
        return self.id_bloque

class Apoderado(models.Model):
    rut_apoderado = models.CharField(primary_key=True, max_length=12, verbose_name="Rut")
    nombre_apoderado = models.CharField(max_length=15, verbose_name="Nombres")
    appaterno_apoderado = models.CharField(max_length=30, verbose_name="Apellido paterno")
    apmaterno_apoderado = models.CharField(max_length=30, verbose_name="Apellido materno")
    direccion_apoderado = models.CharField(max_length=30, verbose_name="Dirección")
    telefono_apoderado = models.IntegerField(verbose_name="Teléfono")
    correo_apoderado = models.CharField(max_length=30, verbose_name="Correo electrónico")
    password = models.CharField(max_length=125, verbose_name="Contraseña")

    def __str__(self):
        return self.nombre_apoderado + " " + self.appaterno_apoderado + " " + self.apmaterno_apoderado

class Alumno(models.Model):
    rut_alumno = models.CharField(primary_key=True, max_length=12, verbose_name="Rut")
    nombre_alumno = models.CharField(max_length=15, verbose_name="Nombres")
    appaterno_alumno = models.CharField(max_length=30, verbose_name="Apellido paterno")
    apmaterno_alumno = models.CharField(max_length=30, verbose_name="Apellido materno")
    direccion_alumno = models.CharField(max_length=30, verbose_name="Dirección")
    telefono_alumno = models.IntegerField(verbose_name="Teléfono")
    correo_alumno = models.CharField(max_length=30, verbose_name="Correo electrónico")
    password = models.CharField(max_length=125, verbose_name="Contraseña")
    sede_alumno = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede del alumno")
    apoderado_alumno = models.ForeignKey(Apoderado, on_delete=models.CASCADE, verbose_name="Apoderado asignado")
    curso_alumno = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso del alumno")

    def __str__(self):
        return self.nombre_alumno + " " + self.appaterno_alumno + " " + self.apmaterno_alumno + " RUT: " + self.rut_alumno

class Boleta(models.Model):
    id_boleta = models.IntegerField(primary_key=True, verbose_name="ID de la boleta")
    apoderado_boleta = models.ForeignKey(Apoderado, on_delete=models.CASCADE, verbose_name="Boleta del apoderado")
   
    def __str__(self):
        return self.id_boleta

class Tipo_Pago(models.Model):
    id_tipo_pago = models.IntegerField(primary_key=True, verbose_name="ID tipo de pago")
    nombre_tipo_pago = models.CharField(max_length=10, verbose_name="Nombre del tipo de pago")

    def __str__(self):
        return self.nombre_tipo_pago

class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True, verbose_name="ID del pago")
    fecha_pago = models.DateTimeField(verbose_name="Fecha")
    monto_pago = models.IntegerField(verbose_name="Monto")
    boleta_pago = models.ForeignKey(Boleta, on_delete=models.CASCADE, verbose_name="Boleta pago")
    tipo_pago_pago = models.ForeignKey(Tipo_Pago, on_delete=models.CASCADE, verbose_name="Tipo pago")

    def __str__(self):
        return self.id_pago
    
class Noticias(models.Model):
    id_noticia = models.IntegerField(primary_key=True, verbose_name="ID de la noticia")
    titulo = models.CharField(max_length=20, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_publi = models.DateTimeField(verbose_name="Fecha de publicación")
    foto_noticia = models.ImageField(upload_to="noticias", null=True, verbose_name="Imagen de la noticia")

    def __str__(self):
        return self.titulo
    
class Administrador(models.Model):
    rut_admin = models.CharField(primary_key=True, max_length=12, verbose_name="Rut")
    nombre_admin = models.CharField(max_length=30, verbose_name="Nombres")
    apellido_admin = models.CharField(max_length=30, verbose_name="Apellidos")
    correo_admin = models.CharField(max_length=30, verbose_name="Correo electrónico")
    password = models.CharField(max_length=125, verbose_name="Contraseña")

    def __str__(self):
        return "RUT: " + self.rut_admin + " " + "Nombres: " + self.nombre_admin + " " + self.apellido_admin