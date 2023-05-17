from django.db import models

class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=15)

    def __str__(self):
        return self.id_region

class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=15)
    region_comuna = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_comuna

class Sede(models.Model):
    id_sede = models.IntegerField(primary_key=True)
    nombre_sede = models.CharField(max_length=15)
    direccion_sede = models.CharField(max_length=25)
    telefono_sede = models.IntegerField()
    comuna_sede = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    region_sede = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_sede

class Tipo_Sala(models.Model):
    id_tipo_sala = models.IntegerField(primary_key=True)
    nombre_tipo_sala = models.CharField(max_length=12)

    def __str__(self):
        return self.id_tipo_sala

class Sala(models.Model): 
    id_sala = models.IntegerField(primary_key=True)
    nombre_sala = models.CharField(max_length=6)
    sede_sala = models.ForeignKey(Sede, on_delete=models.CASCADE)
    tipo_sala = models.ForeignKey(Tipo_Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_sala

class Docente(models.Model):
    rut_docente = models.CharField(primary_key=True, max_length=12)
    id_docente = models.CharField(max_length=15)
    nombre_docente = models.CharField(max_length=15)
    appaterno_docente = models.CharField(max_length=15)
    apmaterno_docente = models.CharField(max_length=15)
    direccion_docente = models.CharField(max_length=30)
    telefono_docente = models.IntegerField()
    correo_docente = models.CharField(max_length=25)
    sede_docente = models.ForeignKey(Sede, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut_docente

class Curso(models.Model):
    id_curso = models.CharField(max_length=5, primary_key=True)
    anno_curso = models.IntegerField()
    docente_curso = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_curso

class Asignatura(models.Model):
    id_asignatura = models.CharField(max_length=6, primary_key=True)
    nombre_asignatura = models.CharField(max_length=12)
    curso_asignatura = models.ForeignKey(Curso, on_delete=models.CASCADE)
    docente_asignatura = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_asignatura

class Horario(models.Model):
    id_horario = models.IntegerField(primary_key=True)
    dia_horario = models.CharField(max_length=9)
    curso_horario = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_horario

class Bloque(models.Model):
    id_bloque = models.IntegerField(primary_key=True)
    horario_bloque = models.ForeignKey(Horario, on_delete=models.CASCADE)
    asignatura_bloque = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    sala_bloque = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_bloque

class Apoderado(models.Model):
    rut_apoderado = models.CharField(primary_key=True, max_length=12)
    id_apoderado = models.CharField(max_length=15)    
    nombre_apoderado = models.CharField(max_length=15)
    appaterno_apoderado = models.CharField(max_length=15)
    apmaterno_apoderado = models.CharField(max_length=15)
    direccion_apoderado = models.CharField(max_length=30)
    telefono_apoderado = models.IntegerField()
    correo_apoderado = models.CharField(max_length=25) 

    def __str__(self):
        return self.rut_apoderado  

class Alumno(models.Model):
    rut_alumno = models.CharField(primary_key=True, max_length=12)
    id_alumno = models.CharField(max_length=15)
    nombre_alumno = models.CharField(max_length=15)
    appaterno_alumno = models.CharField(max_length=15)
    apmaterno_alumno = models.CharField(max_length=15)
    direccion_alumno = models.CharField(max_length=30)
    telefono_alumno = models.IntegerField()
    correo_alumno = models.CharField(max_length=25)
    sede_alumno = models.ForeignKey(Sede, on_delete=models.CASCADE)
    apoderado_alumno = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
    curso_alumno = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut_alumno

class Boleta(models.Model):
    id_boleta = models.IntegerField(primary_key=True)
    apoderado_boleta = models.ForeignKey(Apoderado, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.id_boleta

class Tipo_Pago(models.Model):
    id_tipo_pago = models.IntegerField(primary_key=True)
    nombre_tipo_pago = models.CharField(max_length=10)
    def __str__(self):
        return self.id_tipo_pago

class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    fecha_pago = models.DateTimeField()
    monto_pago = models.IntegerField()
    boleta_pago = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    tipo_pago_pago = models.ForeignKey(Tipo_Pago, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_pago