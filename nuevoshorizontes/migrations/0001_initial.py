# Generated by Django 4.2 on 2023-06-12 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('rut_admin', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre_admin', models.CharField(max_length=30, verbose_name='Nombres')),
                ('apellido_admin', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('correo_admin', models.CharField(max_length=30, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=125, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('rut_apoderado', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre_apoderado', models.CharField(max_length=15, verbose_name='Nombres')),
                ('appaterno_apoderado', models.CharField(max_length=30, verbose_name='Apellido paterno')),
                ('apmaterno_apoderado', models.CharField(max_length=30, verbose_name='Apellido materno')),
                ('direccion_apoderado', models.CharField(max_length=30, verbose_name='Dirección')),
                ('telefono_apoderado', models.IntegerField(verbose_name='Teléfono')),
                ('correo_apoderado', models.CharField(max_length=30, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=125, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id_asignatura', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='ID de la asignatura')),
                ('nombre_asignatura', models.CharField(max_length=30, verbose_name='Nombre de la asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de la boleta')),
                ('apoderado_boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.apoderado', verbose_name='Boleta del apoderado')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de la comuna')),
                ('nombre_comuna', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del curso')),
                ('nombre_curso', models.CharField(max_length=30, verbose_name='Nombre del curso')),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20, verbose_name='Título')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('fecha_publi', models.DateField(verbose_name='Fecha de publicación')),
                ('foto_noticia', models.ImageField(null=True, upload_to='noticias', verbose_name='Imagen de la noticia')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de la región')),
                ('nombre_region', models.CharField(max_length=50, verbose_name='Nombre de la región')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Pago',
            fields=[
                ('id_tipo_pago', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID tipo de pago')),
                ('nombre_tipo_pago', models.CharField(max_length=10, verbose_name='Nombre del tipo de pago')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Sala',
            fields=[
                ('id_tipo_sala', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del tipo sala')),
                ('nombre_tipo_sala', models.CharField(max_length=12, verbose_name='Nombre del tipo de sala')),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=15, verbose_name='Nombre de la sede')),
                ('direccion_sede', models.CharField(max_length=25, verbose_name='Dirección de la sede')),
                ('telefono_sede', models.IntegerField(verbose_name='Teléfono de la sede')),
                ('fotoSede', models.ImageField(null=True, upload_to='sedes', verbose_name='Imagen de la sede')),
                ('comuna_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.comuna', verbose_name='Comuna de la sede')),
                ('region_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.region', verbose_name='Región de la sede')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id_sala', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de la sala')),
                ('nombre_sala', models.CharField(max_length=10, verbose_name='Nombre de la sala')),
                ('sede_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sede', verbose_name='Sede asignada')),
                ('tipo_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.tipo_sala', verbose_name='Tipo de la sala')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del pago')),
                ('fecha_pago', models.DateTimeField(verbose_name='Fecha')),
                ('monto_pago', models.IntegerField(verbose_name='Monto')),
                ('boleta_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.boleta', verbose_name='Boleta pago')),
                ('tipo_pago_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.tipo_pago', verbose_name='Tipo pago')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id_horario', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del horario')),
                ('dia_horario', models.CharField(max_length=9, verbose_name='Días')),
                ('curso_horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.curso', verbose_name='Curso asignado')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('rut_docente', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut del docente')),
                ('nombre_docente', models.CharField(max_length=15, verbose_name='Nombres del docente')),
                ('appaterno_docente', models.CharField(max_length=30, verbose_name='Apellido paterno del docente')),
                ('apmaterno_docente', models.CharField(max_length=30, verbose_name='Apellido materno del docente')),
                ('direccion_docente', models.CharField(max_length=30, verbose_name='Dirección del docente')),
                ('telefono_docente', models.IntegerField(verbose_name='Teléfono del docente')),
                ('correo_docente', models.CharField(max_length=30, verbose_name='Correo electrónico del docente')),
                ('password', models.CharField(max_length=125, verbose_name='Contraseña')),
                ('asignaturas_docente', models.ManyToManyField(to='nuevoshorizontes.asignatura', verbose_name='Asignaturas asignadas')),
                ('sede_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sede', verbose_name='Sede asignado')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='docente_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.docente', verbose_name='Docente asignado'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region_comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.region', verbose_name='Región'),
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id_bloque', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del bloque')),
                ('asignatura_bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.asignatura', verbose_name='Bloque de la asignatura')),
                ('horario_bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.horario', verbose_name='Horario del bloque')),
                ('sala_bloque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sala', verbose_name='Bloque de la sala')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut_alumno', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre_alumno', models.CharField(max_length=15, verbose_name='Nombres')),
                ('appaterno_alumno', models.CharField(max_length=30, verbose_name='Apellido paterno')),
                ('apmaterno_alumno', models.CharField(max_length=30, verbose_name='Apellido materno')),
                ('direccion_alumno', models.CharField(max_length=30, verbose_name='Dirección')),
                ('telefono_alumno', models.IntegerField(blank=True, null=True, verbose_name='Teléfono')),
                ('correo_alumno', models.CharField(max_length=30, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=125, verbose_name='Contraseña')),
                ('apoderado_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.apoderado', verbose_name='Apoderado asignado')),
                ('curso_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.curso', verbose_name='Curso del alumno')),
                ('sede_alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sede', verbose_name='Sede del alumno')),
            ],
        ),
    ]
