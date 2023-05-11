from django.urls import path
from .views import home, login, nosotros, sedes, noticias, home_admin, asignaturas_admin, cursos_admin, noticias_admin, salas_admin, sedes_admin, usuarios_admin

urlpatterns = [
    path('', home, name="home"),
    path('nosotros', nosotros, name="nosotros"),
    path('sedes', sedes, name="sedes"),
    path('noticias', noticias, name="noticias"),
    path('login', login, name="login"),
    path('home_admin', home_admin, name="home_admin"),
    path('asignaturas_admin', asignaturas_admin, name="asignaturas_admin"),
    path('cursos_admin', cursos_admin, name="cursos_admin"),
    path('noticias_admin', noticias_admin, name="noticias_admin"),
    path('salas_admin', salas_admin, name="salas_admin"),
    path('sedes_admin', sedes_admin, name="sedes_admin"),
    path('usuarios_admin', usuarios_admin, name="usuarios_admin"),
]