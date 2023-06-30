from django.db import models

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True, verbose_name="ID de la región")
    nombre_region = models.CharField(max_length=50, verbose_name="Nombre de la región")

    def __str__(self):
        return self.nombre_region

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True, verbose_name="ID de la comuna")
    nombre_comuna = models.CharField(max_length=50, verbose_name="Nombre")
    region_comuna = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región")

    def __str__(self):
        return self.nombre_comuna

class Sede(models.Model):
    nombre_sede = models.CharField(max_length=40, verbose_name="Nombre de la sede")
    direccion_sede = models.CharField(max_length=40, verbose_name="Dirección de la sede")
    telefono_sede = models.IntegerField(verbose_name="Teléfono de la sede")
    fotoSede = models.ImageField(upload_to="sedes", null=True,verbose_name="Imagen de la sede")
    region_sede = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Región de la sede")
    comuna_sede = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name="Comuna de la sede")

    def __str__(self):
        return self.nombre_sede

class Tipo_Sala(models.Model):
    id_tipo_sala = models.IntegerField(primary_key=True, verbose_name="ID del tipo sala")
    nombre_tipo_sala = models.CharField(max_length=12, verbose_name="Nombre del tipo de sala")

    def __str__(self):
        return self.nombre_tipo_sala

class Sala(models.Model): 
    id_sala = models.IntegerField(primary_key=True, verbose_name="ID de la sala")
    nombre_sala = models.CharField(max_length=10, verbose_name="Nombre de la sala")
    sede_sala = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede asignada")
    tipo_sala = models.ForeignKey(Tipo_Sala, on_delete=models.CASCADE, verbose_name="Tipo de la sala")

    def __str__(self):
        return self.nombre_sala

class Docente(models.Model):
    rut_docente = models.CharField(primary_key=True, max_length=12, verbose_name="Rut del docente")
    nombre_docente = models.CharField(max_length=50, verbose_name="Nombres del docente")
    appaterno_docente = models.CharField(max_length=50, verbose_name="Apellido paterno del docente")
    apmaterno_docente = models.CharField(max_length=50, verbose_name="Apellido materno del docente")
    direccion_docente = models.CharField(max_length=30, verbose_name="Dirección del docente")
    telefono_docente = models.IntegerField(verbose_name="Teléfono del docente")
    correo_docente = models.CharField(max_length=50, verbose_name="Correo electrónico del docente")
    password = models.CharField(max_length=128, verbose_name="Contraseña")
    sede_docente = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede asignado")

    def __str__(self):
        return "RUT: " + self.rut_docente + " " + "Nombre: " + self.nombre_docente + " " + self.appaterno_docente
    
    def nombre_completo(self):
        return self.nombre_docente + " " + self.appaterno_docente

class Asignatura(models.Model):
    id_asignatura = models.CharField(max_length=9, primary_key=True, verbose_name="ID de la asignatura")
    nombre_asignatura = models.CharField(max_length=30, verbose_name="Nombre de la asignatura")
    profesor_asignatura = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name="profesor de la asignatura" )

    def __str__(self):
        return self.nombre_asignatura

class Curso(models.Model):
    id_curso = models.CharField(primary_key=True,max_length=10, verbose_name="ID del curso")
    nombre_curso = models.CharField(max_length=30, verbose_name="Nombre del curso")
    docente_curso = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name="Docente asignado")
    sala_curso = models.ForeignKey(Sala,on_delete=models.CASCADE, verbose_name="Sala del curso", null=True)

    def __str__(self):
        return self.nombre_curso

class Horario(models.Model):
    id_horario = models.IntegerField(primary_key=True, verbose_name="ID del horario")
    curso_horario = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso asignado")

    def __str__(self):
        return self.dia_horario

class Bloque(models.Model):
    id_bloque = models.IntegerField(primary_key=True, verbose_name="ID del bloque")
    nombre_bloque = models.CharField(max_length=3, verbose_name="Nombre del bloque", null=True)
    horario_bloque = models.ForeignKey(Horario, on_delete=models.CASCADE, verbose_name="Horario del bloque")
    asignatura_bloque = models.ForeignKey(Asignatura, on_delete=models.CASCADE, verbose_name="Bloque de la asignatura")

    def __str__(self):
        return self.id_bloque

class Apoderado(models.Model):
    rut_apoderado = models.CharField(primary_key=True, max_length=12, verbose_name="Rut")
    nombre_apoderado = models.CharField(max_length=50, verbose_name="Nombres")
    appaterno_apoderado = models.CharField(max_length=50, verbose_name="Apellido paterno")
    apmaterno_apoderado = models.CharField(max_length=50, verbose_name="Apellido materno")
    direccion_apoderado = models.CharField(max_length=30, verbose_name="Dirección")
    telefono_apoderado = models.IntegerField(verbose_name="Teléfono")
    correo_apoderado = models.CharField(max_length=50, verbose_name="Correo electrónico")
    password = models.CharField(max_length=128, verbose_name="Contraseña")

    def __str__(self):
        return "RUT: " + self.rut_apoderado + " " + "Nombre completo: " + self.nombre_apoderado + " " + self.appaterno_apoderado

class Alumno(models.Model):
    rut_alumno = models.CharField(primary_key=True, max_length=12, verbose_name="Rut")
    nombre_alumno = models.CharField(max_length=50, verbose_name="Nombres")
    appaterno_alumno = models.CharField(max_length=50, verbose_name="Apellido paterno")
    apmaterno_alumno = models.CharField(max_length=50, verbose_name="Apellido materno")
    correo_alumno = models.CharField(max_length=50, verbose_name="Correo electrónico")
    password = models.CharField(max_length=128, verbose_name="Contraseña")
    sede_alumno = models.ForeignKey(Sede, on_delete=models.CASCADE, verbose_name="Sede del alumno")
    apoderado_alumno = models.ForeignKey(Apoderado, on_delete=models.CASCADE, verbose_name="Apoderado asignado")
    curso_alumno = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso del alumno")

    def __str__(self):
        return "RUT: " + self.rut_alumno + " " + "Nombres: " + self.nombre_alumno + " " + self.appaterno_alumno
    
class Tipo_asis(models.Model):
    id_tipo_asistencia = models.AutoField(primary_key=True)
    tipo_asistencia = models.CharField(max_length=20, verbose_name="Tipo asistencia") #Presente, ausente y justificado

    def __str__(self):
        return self.nombre_estado_asistencia
    
class Asistencia(models.Model):
    tipo_asistencia = models.ForeignKey(Tipo_asis, on_delete=models.CASCADE, verbose_name="Tipo asistencia")
    fecha_asistencia = models.DateField(verbose_name="Fecha asistencia")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso")
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, verbose_name="Docente")

    def __str__(self):
        return self.tipo_asistencia
    
class Tipo_pago_colegio(models.Model):
    nombre_tipo_pago_colegio = models.CharField(max_length=20, verbose_name="tipo de valor")

    def __str__(self):
        return self.nombre_tipo_pago_colegio
    
class Pagos_colegio(models.Model):
    id_pago_colegio = models.AutoField(primary_key=True, verbose_name="ID del valor")
    nombre_pago_colegio = models.CharField(max_length=50, verbose_name="Nombre del pago colegio")
    monto = models.IntegerField(verbose_name="Monto del valor")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    tipo_pago_colegio = models.ForeignKey(Tipo_pago_colegio, on_delete=models.CASCADE, verbose_name="Tipo pago colegio")

    def __str__(self):
        return self.nombre_pago_colegio
    
class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True, verbose_name="ID del pago")
    fecha_pago = models.DateField(verbose_name="Fecha")
    monto_pago = models.IntegerField(verbose_name="Monto")
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE, verbose_name="Apoderado que pagó")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, verbose_name="Alumno")
    nombre_pago_colegio = models.ForeignKey(Pagos_colegio, on_delete=models.CASCADE, verbose_name="Nombre pago colegio")

    def __str__(self):
        return str(self.id_pago)
    
class Boletas(models.Model):
    id_boleta = models.AutoField(primary_key=True, verbose_name="ID de la boleta")
    pago = models.ForeignKey(Pagos, on_delete=models.CASCADE, verbose_name="Pago realizado")

    def __str__(self):
        return str(self.id_boleta)
    
class Noticias(models.Model):
    titulo = models.CharField(max_length=20, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_publi = models.DateField(verbose_name="Fecha de publicación")
    foto_noticia = models.ImageField(upload_to="noticias", null=True, verbose_name="Imagen de la noticia")

    def __str__(self):
        return self.titulo

class Administrador(models.Model):
    nombre_admin = models.CharField(max_length=50, verbose_name="Nombres")
    apellido_admin = models.CharField(max_length=50, verbose_name="Apellidos")
    correo_admin = models.CharField(max_length=50, verbose_name="Correo electrónico")
    password = models.CharField(max_length=128, verbose_name="Contraseña")
    
    def __str__(self):
        return "Nombres: " + self.nombre_admin + " " + self.apellido_admin
    
class Postulaciones(models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Nombre")
    apellidos = models.CharField(max_length=50, verbose_name="Apellido")
    email = models.CharField(max_length=50, verbose_name="Correo")
    telefono = models.IntegerField(verbose_name="Teléfono")
    sede = models.CharField(max_length=50, verbose_name="sede")
    mensaje = models.TextField(verbose_name="mensaje")