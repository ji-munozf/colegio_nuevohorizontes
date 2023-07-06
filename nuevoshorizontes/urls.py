from django.urls import path
from .views import *

urlpatterns = [
    #Home
    path('', home, name="home"),
    path('nosotros', nosotros, name="nosotros"),
    path('portales', portales, name="portales"),
    path('sedes', sedes, name="sedes"),
    path('noticias', noticias, name="noticias"),

    #Home admin
    path('portal_admin/home_admin', home_admin, name="home_admin"),
    path('portal_admin/home_agregar', home_agregar, name="home_agregar"),
    path('portal_admin/home_listado', home_listado, name="home_listado"),
    path('portal_admin/home_pagos', home_pagos, name="home_pagos"),

    #Registro contacto de postulación
    path('registro_contacto', registrar_contacto, name="registro_contacto"),

    #Api select comunas
    path('api/comunas/', obtener_comunas, name='api_comunas'),

    #Formularios de agregar
    path('portal_admin/formularios/agregar_admins', agregar_admins, name="agregar_admins"),
    path('portal_admin/formularios/agregar_alumnos', agregar_alumnos, name="agregar_alumnos"),
    path('portal_admin/formularios/agregar_docentes', agregar_docentes, name="agregar_docentes"),
    path('portal_admin/formularios/agregar_apoderados', agregar_apoderados, name="agregar_apoderados"),
    path('portal_admin/formularios/agregar_asignaturas', agregar_asignaturas, name="agregar_asignaturas"),
    path('portal_admin/formularios/agregar_cursos', agregar_cursos, name="agregar_cursos"),
    path('portal_admin/formularios/agregar_noticias', agregar_noticias, name="agregar_noticias"),
    path('portal_admin/formularios/agregar_salas', agregar_salas, name="agregar_salas"),
    path('portal_admin/formularios/agregar_sedes', agregar_sedes, name="agregar_sedes"),
    path('portal_admin/formularios/agregar_pagos_colegio', agregar_pagos_colegio, name="agregar_pagos_colegio"),
    path('portal_admin/formularios/agregar_horariocurso', agregar_horariocurso, name="agregar_horariocurso"),

    #Listado
    path('portal_admin/listados/listar_admins', listar_admins, name="listar_admins"),
    path('portal_admin/listados/listar_alumnos', listar_alumnos, name="listar_alumnos"),
    path('portal_admin/listados/listar_docentes', listar_docentes, name="listar_docentes"),
    path('portal_admin/listados/listar_apoderados', listar_apoderados, name="listar_apoderados"),
    path('portal_admin/listados/listar_noticias', listar_noticias, name="listar_noticias"),
    path('portal_admin/listados/listar_asignaturas', listar_asignaturas, name="listar_asignaturas"),
    path('portal_admin/listados/listar_cursos', listar_cursos, name="listar_cursos"),
    path('portal_admin/listados/listar_sedes', listar_sedes_admin, name="listar_sedes"),
    path('portal_admin/listados/listar_salas', listar_salas, name="listar_salas"),
    path('portal_admin/listados/listar_postulaciones', listar_postulaciones, name="listar_postulaciones"),
    path('portal_admin/listados/listar_asistencias', listar_asistencias, name="listar_asistencias"),
    path('portal_admin/listados/listar_pago_colegio', listar_pago_colegio, name="listar_pago_colegio"),
    path('portal_admin/listados/listar_horarios_cursos', listar_horarios_cursos, name="listar_horarios_cursos"),
    path('portal_admin/listados/listar_horarios_cursos/listar_horario/<str:id_curso>/', listar_horarios, name="listar_horarios"),

    #Cambiar contraseñas
    path('portal_admin/listados/listar_docentes/cambiar_pass_docente/<id>/', cambiar_pass_docente, name="cambiar_pass_docente"),
    path('portal_admin/listados/listar_alumnos/cambiar_pass_alumno/<id>/', cambiar_pass_alumno, name="cambiar_pass_alumno"),
    path('portal_admin/listados/listar_apoderado/cambiar_pass_apoderado/<id>/', cambiar_pass_apoderado, name="cambiar_pass_apoderado"),
    path('portal_admin/listados/listar_admins/cambiar_pass_admin/<id>/', cambiar_pass_admin, name="cambiar_pass_admin"),

    #Modificar
    path('portal_admin/listados/listar_alumnos/modificar_alumno/<id>/', modificar_alumnos, name="modificar_alumno"),
    path('portal_admin/listados/listar_docentes/modificar_docente/<id>/', modificar_docentes, name="modificar_docente"),
    path('portal_admin/listados/listar_apoderados/modificar_apoderado/<id>/', modificar_apoderados, name="modificar_apoderado"),
    path('portal_admin/listados/listar_admins/modificar_admin/<id>/', modificar_admins, name="modificar_admins"),
    path('portal_admin/listados/listar_noticias/modificar_noticia/<id>/', modificar_noticias, name="modificar_noticias"),
    path('portal_admin/listados/listar_asignaturas/modificar_asignatura/<id>/', modificar_asignaturas, name="modificar_asignaturas"),
    path('portal_admin/listados/listar_cursos/modificar_curso/<id>/', modificar_cursos, name="modificar_cursos"),
    path('portal_admin/listados/listar_sedes/modificar_sede/<id>/', modificar_sedes, name="modificar_sedes"),
    path('portal_admin/listados/listar_salas/modificar_salas/<id>/', modificar_salas, name="modificar_salas"),
    path('portal_admin/listados/listar_salas/modificar_pago_colegio/<id>/', modificar_pago_colegio, name="modificar_pago_colegio"),

    #Eliminar
    path('eliminar_alumno/<id>/', eliminar_alumno, name="eliminar_alumno"),
    path('eliminar_docente/<id>/', eliminar_docentes, name="eliminar_docente"),
    path('eliminar_apoderado/<id>/', eliminar_apoderado, name="eliminar_apoderado"),
    path('eliminar_admin/<id>/', eliminar_admin, name="eliminar_admin"),
    path('eliminar_noticias/<id>/', eliminar_noticias, name="eliminar_noticias"),
    path('eliminar_asignatura/<id>/', eliminar_asignatura, name="eliminar_asignatura"),
    path('eliminar_curso/<id>/', eliminar_curso, name="eliminar_curso"),
    path('eliminar_sede/<id>/', eliminar_sedes, name="eliminar_sedes"),
    path('eliminar_sala/<id>/', eliminar_salas, name="eliminar_salas"),
    path('eliminar_postulacion/<id>/', eliminar_postulacion, name="eliminar_postulacion"),
    path('eliminar_pago/<id>/', eliminar_pagos, name="eliminar_pagos"),
    path('eliminar_pagos_colegio/<id>/', eliminar_pagos_colegio, name="eliminar_pagos_colegio"),
    path('eliminar_horario/<str:id_curso>/', eliminar_horario, name="eliminar_horario"),
    path('eliminar-asistencias/', eliminar_asistencias, name='eliminar_asistencias'),
    
    #Home alumno
    path('portal_alumno/home_alumno', home_alumno, name="home_alumno"),
    path('portal_alumno/mi_perfil', miperfil_alumno, name="miperfil_alumno"),
    path('portal_alumno/notas_alumno', notas_alumno, name="notas_alumno"),
    path('portal_alumno/horario_alumno', horario_alumno, name="horario_alumno"),
    path('portal_alumno/asistencia_alumno', asistencia_alumno, name="asistencia_alumno"),

    #Home apoderado
    path('portal_apoderado/home_apoderado', home_apoderado, name="home_apoderado"),
    path('portal_apoderado/mi_perfil', miperfil_apoderado, name="miperfil_apoderado"),
    path('portal_apoderado/lista_hijos', lista_hijos, name="lista_hijos"),
    path('portal_apoderado/horarios', horarios_apoderado, name="horarios_apoderado"),
    path('portal_apoderado/horarios/ver_horario_hijo/<str:rut_alumno>/', ver_horario_hijo, name="ver_horario_hijo"),
    path('portal_apoderado/asistencias', asistencias_apoderado, name="asistencias_apoderado"),
    path('portal_apoderado/notas_apoderado', notas_apoderado, name="notas_apoderado"),
    path('portal_apoderado/pagos_apoderado', pagos_apoderado, name="pagos_apoderado"),
    path('portal_apoderado/pagos_apoderado/listar_pagos_apoderado/<str:rut_alumno>/', listar_pagos_apoderado, name="listar_pagos_apoderado"),
    path("realizar_pago/", realizar_pago, name="realizar_pago"),

    #Home docente
    path('portal_docente/home_docente', home_docente, name="home_docente"),
    path('portal_docente/mi_perfil', miperfil_docente, name="miperfil_docente"),
    path('portal_docente/curso_docente', curso_docente, name="curso_docente"),
    path('portal_docente/asignaturas_docente', asignaturas_docente, name="asignaturas_docente"),
    path('portal_docente/asistencia_docente', asistencia_docente, name="asistencia_docente"),
    path('portal_docente/asistencia_docente/agregar_asistencia', agregar_asistencia, name="agregar_asistencia"),
    path('portal_docente/asistencia_docente/buscar_asistencia', buscar_asistencia, name="buscar_asistencia"),
    path('portal_docente/asistencia_docente/modificar_asistencia/<str:rut_alumno>/', modificar_asistencia, name="modificar_asistencia"),

    #Inicio de sesión
    path('portales/login_alumno', login_alumno, name="login_alumno"),
    path('portales/login_docente', login_docente, name="login_docente"),
    path('portales/login_apoderado', login_apoderado, name="login_apoderado"),
    path('portales/login_administrativo', login_administrativo, name="login_administrativo"),

    #Cerrar sesión
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]