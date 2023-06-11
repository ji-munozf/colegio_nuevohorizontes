from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('nosotros', nosotros, name="nosotros"),
    path('portales', portales, name="portales"),
    path('sedes', sedes, name="sedes"),
    path('noticias', noticias, name="noticias"),

    path('portal_admin/home_admin', home_admin, name="home_admin"),
    path('portal_admin/home_agregar', home_agregar, name="home_agregar"),
    path('portal_admin/home_listado', home_listado, name="home_listado"),
    path('portal_admin/home_pagos', home_pagos, name="home_pagos"),

    path('api/comunas/', obtener_comunas, name='api_comunas'),

    path('portal_admin/formularios/agregar_admins', agregar_admins, name="agregar_admins"),
    path('portal_admin/formularios/agregar_alumnos', agregar_alumnos, name="agregar_alumnos"),
    path('portal_admin/formularios/agregar_docentes', agregar_docentes, name="agregar_docentes"),
    path('portal_admin/formularios/agregar_apoderados', agregar_apoderados, name="agregar_apoderados"),
    path('portal_admin/formularios/agregar_asignaturas', agregar_asignaturas, name="agregar_asignaturas"),
    path('portal_admin/formularios/agregar_cursos', agregar_cursos, name="agregar_cursos"),
    path('portal_admin/formularios/agregar_noticias', agregar_noticias, name="agregar_noticias"),
    path('portal_admin/formularios/agregar_salas', agregar_salas, name="agregar_salas"),
    path('portal_admin/formularios/agregar_sedes', agregar_sedes, name="agregar_sedes"),

    path('portal_admin/listados/listar_admins', listar_admins, name="listar_admins"),
    path('portal_admin/listados/listar_alumnos', listar_alumnos, name="listar_alumnos"),
    path('portal_admin/listados/listar_docentes', listar_docentes, name="listar_docentes"),
    path('portal_admin/listados/listar_noticias', listar_noticias, name="listar_noticias"),

    path('portal_admin/listados/listar_docentes/cambiar_pass_docente/<id>/', cambiar_pass_docente, name="cambiar_pass_docente"),

    path('portal_admin/listados/listar_docentes/modificar_docente/<id>/', modificar_docentes, name="modificar_docente"),
    path('portal_admin/listados/listar_noticias/modificar_noticia/<id>/', modificar_noticias, name="modificar_noticias"),

    path('eliminar_docente/<id>/', eliminar_docentes, name="eliminar_docente"),
    path('eliminar_noticias/<id>/', eliminar_noticias, name="eliminar_noticias"),
    
    path('portal_alumno/home_alumno', home_alumno, name="home_alumno"),
    path('portal_alumno/mi_perfil', miperfil_alumno, name="miperfil_alumno"),
    path('portal_alumno/guardar_perfil_alumno', guardar_perfil_alumno, name="guardar_perfil_alumno"),
    path('portal_alumno/notas_alumno', notas_alumno, name="notas_alumno"),
    path('portal_alumno/horario_alumno', horario_alumno, name="horario_alumno"),

    path('portal_apoderado/home_apoderado', home_apoderado, name="home_apoderado"),
    path('portal_apoderado/mi_perfil', miperfil_apoderado, name="miperfil_apoderado"),
    path('portal_apoderado/guardar_perfil_apoderado/', guardar_perfil_apoderado, name='guardar_perfil_apoderado'),
    path('portal_apoderado/lista_hijos', lista_hijos, name="lista_hijos"),
    path('portal_apoderado/horarios', horarios_apoderado, name="horarios_apoderado"),
    path('portal_apoderado/asistencias', asistencias_apoderado, name="asistencias_apoderado"),
    path('portal_apoderado/notas_apoderado', notas_apoderado, name="notas_apoderado"),
    path('portal_apoderado/pagos_apoderado', pagos_apoderado, name="pagos_apoderado"),

    path('portal_docente/home_docente', home_docente, name="home_docente"),
    path('portal_docente/mi_perfil', miperfil_docente, name="miperfil_docente"),
    path('portal_apoderado/guardar_perfil_docente/', guardar_perfil_docente, name='guardar_perfil_docente'),
    path('portal_docente/curso_docente', curso_docente, name="curso_docente"),
    path('portal_docente/asignaturas_docente', asignaturas_docente, name="asignaturas_docente"),

    path('portales/login_alumno', login_alumno, name="login_alumno"),
    path('portales/login_docente', login_docente, name="login_docente"),
    path('portales/login_apoderado', login_apoderado, name="login_apoderado"),
    path('portales/login_administrativo', login_administrativo, name="login_administrativo"),

    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]