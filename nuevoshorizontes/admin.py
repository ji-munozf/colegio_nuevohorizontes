from django.contrib import admin
from .models import Region, Comuna, Sede, Tipo_Sala, Sala, Docente, Curso, Asignatura, Horario, Bloque, Apoderado, Alumno, Boleta, Tipo_Pago, Pago
# Register your models here.

admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Sede)