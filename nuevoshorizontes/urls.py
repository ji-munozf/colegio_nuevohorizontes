from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('nosotros', nosotros, name="nosotros"),
    path('portales', portales, name="portales"),
    path('sedes', sedes, name="sedes"),
    path('noticias', noticias, name="noticias"),
    path('home_admin', home_admin, name="home_admin"),
    path('asignaturas_admin', asignaturas_admin, name="asignaturas_admin"),
    path('cursos_admin', cursos_admin, name="cursos_admin"),
    path('noticias_admin', noticias_admin, name="noticias_admin"),
    path('salas_admin', salas_admin, name="salas_admin"),
    path('sedes_admin', sedes_admin, name="sedes_admin"),
    path('usuarios_admin', usuarios_admin, name="usuarios_admin"),
    path('portal_admin/formularios/agregar_asignaturas', agregar_asignaturas, name="agregar_asignaturas"),
    path('portal_admin/formularios/agregar_cursos', agregar_cursos, name="agregar_cursos"),
    path('portal_admin/formularios/agregar_noticias', agregar_noticias, name="agregar_noticias"),
    path('portal_admin/formularios/agregar_salas', agregar_salas, name="agregar_salas"),
    path('portal_admin/formularios/agregar_sedes', agregar_sedes, name="agregar_sedes"),
    
    path('home_alumno', home_alumno, name="home_alumno"),
    path('notas_alumno', notas_alumno, name="notas_alumno"),
    path('horario_alumno', horario_alumno, name="horario_alumno"),

    path('home_apoderado', home_apoderado, name="home_apoderado"),
    path('notas_apoderado', notas_apoderado, name="notas_apoderado"),
    path('perfil_asistencia_apoderado', perfil_asistencia_apoderado, name="perfil_asistencia_apoderado"),
    path('pagos_apoderado', pagos_apoderado, name="pagos_apoderado"),

    path('home_docente', home_docente, name="home_docente"),
    path('curso_docente', curso_docente, name="curso_docente"),
    path('asignaturas_docente', asignaturas_docente, name="asignaturas_docente"),

    path('portales/login_alumno', login_alumno, name="login_alumno"),
    path('portales/login_docente', login_docente, name="login_docente"),
    path('portales/login_apoderado', login_apoderado, name="login_apoderado"),
    path('portales/login_administrativo', login_administrativo, name="login_administrativo"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion")
]