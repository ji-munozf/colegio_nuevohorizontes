# Generated by Django 4.1 on 2024-01-11 18:19

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_admin', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellido_admin', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('correo_admin', models.CharField(max_length=50, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('rut_alumno', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre_alumno', models.CharField(max_length=50, verbose_name='Nombres')),
                ('appaterno_alumno', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apmaterno_alumno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('correo_alumno', models.CharField(max_length=50, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('rut_apoderado', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre_apoderado', models.CharField(max_length=50, verbose_name='Nombres')),
                ('appaterno_apoderado', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apmaterno_apoderado', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('direccion_apoderado', models.CharField(max_length=30, verbose_name='Dirección')),
                ('telefono_apoderado', models.IntegerField(verbose_name='Teléfono')),
                ('correo_apoderado', models.CharField(max_length=50, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id_asignatura', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='ID de la asignatura')),
                ('nombre_asignatura', models.CharField(max_length=30, verbose_name='Nombre de la asignatura')),
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
            name='Postulaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.CharField(max_length=50, verbose_name='Correo')),
                ('telefono', models.IntegerField(verbose_name='Teléfono')),
                ('sede', models.CharField(max_length=50, verbose_name='sede')),
                ('mensaje', models.TextField(verbose_name='mensaje')),
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
            name='Tipo_asis',
            fields=[
                ('id_tipo_asistencia', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_asistencia', models.CharField(max_length=20, verbose_name='Tipo asistencia')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_pago_colegio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipo_pago_colegio', models.CharField(max_length=20, verbose_name='tipo de valor')),
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
                ('nombre_sede', models.CharField(max_length=40, verbose_name='Nombre de la sede')),
                ('direccion_sede', models.CharField(max_length=40, verbose_name='Dirección de la sede')),
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
            name='Pagos_colegio',
            fields=[
                ('id_pago_colegio', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del valor')),
                ('nombre_pago_colegio', models.CharField(max_length=50, verbose_name='Nombre del pago colegio')),
                ('monto', models.IntegerField(verbose_name='Monto del valor')),
                ('fecha_vencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('pagado', models.BooleanField(default=False, verbose_name='Pagado')),
                ('tipo_pago_colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.tipo_pago_colegio', verbose_name='Tipo pago colegio')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('rut_docente', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='Rut del docente')),
                ('nombre_docente', models.CharField(max_length=50, verbose_name='Nombres del docente')),
                ('appaterno_docente', models.CharField(max_length=50, verbose_name='Apellido paterno del docente')),
                ('apmaterno_docente', models.CharField(max_length=50, verbose_name='Apellido materno del docente')),
                ('direccion_docente', models.CharField(max_length=30, verbose_name='Dirección del docente')),
                ('telefono_docente', models.IntegerField(verbose_name='Teléfono del docente')),
                ('correo_docente', models.CharField(max_length=50, verbose_name='Correo electrónico del docente')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
                ('sede_docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sede', verbose_name='Sede asignado')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='ID del curso')),
                ('nombre_curso', models.CharField(max_length=30, verbose_name='Nombre del curso')),
                ('docente_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.docente', verbose_name='Docente asignado')),
                ('sala_curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sala', verbose_name='Sala del curso')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region_comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.region', verbose_name='Región'),
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_nota', models.CharField(max_length=40, verbose_name='Nombre de la nota')),
                ('valor', models.FloatField(verbose_name='Nota')),
                ('fecha_nota', models.DateField(verbose_name='Fecha nota')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.alumno', verbose_name='Nombre el alumno')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.asignatura', verbose_name='Asignatura de la nota')),
            ],
        ),
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_bloque', models.CharField(max_length=3, null=True, verbose_name='Nombre del bloque')),
                ('asignatura_bloque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.asignatura', verbose_name='Asignatura del bloque')),
                ('curso_bloque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.curso', verbose_name='Curso del bloque')),
                ('docente_bloque', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.docente', verbose_name='Docente del bloque')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.AutoField(primary_key=True, serialize=False, verbose_name='ID asistencia')),
                ('fecha_asistencia', models.DateField(verbose_name='Fecha asistencia')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.alumno', verbose_name='Alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.curso', verbose_name='Curso')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.docente', verbose_name='Docente')),
                ('tipo_asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.tipo_asis', verbose_name='Tipo asistencia')),
            ],
        ),
        migrations.AddField(
            model_name='asignatura',
            name='profesor_asignatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.docente', verbose_name='profesor de la asignatura'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='apoderado_alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.apoderado', verbose_name='Apoderado asignado'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='curso_alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.curso', verbose_name='Curso del alumno'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='sede_alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nuevoshorizontes.sede', verbose_name='Sede del alumno'),
        ),
    ]
