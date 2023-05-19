from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('nosotros', nosotros, name="nosotros"),
    path('sedes', sedes, name="sedes"),
    path('noticias', noticias, name="noticias"),
    path('home_admin', home_admin, name="home_admin"),
    path('asignaturas_admin', asignaturas_admin, name="asignaturas_admin"),
    path('cursos_admin', cursos_admin, name="cursos_admin"),
    path('noticias_admin', noticias_admin, name="noticias_admin"),
    path('salas_admin', salas_admin, name="salas_admin"),
    path('sedes_admin', sedes_admin, name="sedes_admin"),
    path('usuarios_admin', usuarios_admin, name="usuarios_admin"),
    path('agregar_asignaturas', agregar_asignaturas, name="agregar_asignaturas"),
    path('agregar_cursos', agregar_cursos, name="agregar_cursos"),
    path('agregar_noticias', agregar_noticias, name="agregar_noticias"),
    path('agregar_salas', agregar_salas, name="agregar_salas"),
    path('agregar_sedes', agregar_sedes, name="agregar_sedes")
]