from django import forms
from .models import *
from datetime import date
from django.core.exceptions import ValidationError


class AlumnoForm(forms.ModelForm):
    rut_alumno = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        max_length=10,
        error_messages={
            "unique": "El rut del alumno ya existe.",
        },
    )
    nombre_alumno = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    appaterno_alumno = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    apmaterno_alumno = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    direccion_alumno = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    telefono_alumno = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"}), required=False
    )
    correo_alumno = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El correo del alumno ya existe.",
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "required": "required"}
        )
    )
    sede_alumno = forms.ModelChoiceField(
        queryset=Sede.objects.all(),
        empty_label="Seleccione una sede",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )
    apoderado_alumno = forms.ModelChoiceField(
        queryset=Apoderado.objects.all(),
        empty_label="Seleccione un apoderado",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )
    curso_alumno = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        empty_label="Seleccione el curso",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )

    def clean_correo_alumno(self):
        correo_alumno = self.cleaned_data['correo_alumno']
        if not self.instance.pk and Alumno.objects.filter(correo_alumno=correo_alumno).exists():
            raise forms.ValidationError("El correo del alumno ya existe.")
        return correo_alumno

    class Meta:
        model = Alumno
        fields = "__all__"


class DocenteForm(forms.ModelForm):
    rut_docente = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        max_length=10,
        error_messages={
            "unique": "El rut del docente ya existe.",
        },
    )
    nombre_docente = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    appaterno_docente = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    apmaterno_docente = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    direccion_docente = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    telefono_docente = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "required": "required"}
        )
    )
    correo_docente = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El correo del docente ya existe.",
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "required": "required"}
        )
    )
    sede_docente = forms.ModelChoiceField(
        queryset=Sede.objects.all(),
        empty_label="Seleccione una sede",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )

    def clean_correo_docente(self):
        correo_docente = self.cleaned_data['correo_docente']
        if not self.instance.pk and Docente.objects.filter(correo_docente=correo_docente).exists():
            raise forms.ValidationError("El correo del docente ya existe.")
        return correo_docente

    class Meta:
        model = Docente
        fields = "__all__"


class ApoderadoForm(forms.ModelForm):
    rut_apoderado = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        max_length=10,
        error_messages={
            "unique": "El rut del apoderado ya existe.",
        },
    )
    nombre_apoderado = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    appaterno_apoderado = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    apmaterno_apoderado = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    direccion_apoderado = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )
    telefono_apoderado = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "required": "required"}
        )
    )
    correo_apoderado = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El correo del apoderado ya existe.",
        },
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "required": "required"}
        )
    )

    def clean_correo_apoderado(self):
        correo_apoderado = self.cleaned_data['correo_apoderado']
        if not self.instance.pk and Apoderado.objects.filter(correo_apoderado=correo_apoderado).exists():
            raise forms.ValidationError("El correo del apoderado ya existe.")
        return correo_apoderado

    class Meta:
        model = Apoderado
        fields = "__all__"


class AdminForm(forms.ModelForm):
    nombre_admin = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )

    apellido_admin = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"})
    )

    correo_admin = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El correo del admin ya existe.",
        },
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "required": "required"}
        )
    )

    def clean_correo_admin(self):
        correo_admin = self.cleaned_data['correo_admin']
        if not self.instance.pk and Administrador.objects.filter(correo_admin=correo_admin).exists():
            raise forms.ValidationError("El correo del admin ya existe.")
        return correo_admin

    class Meta:
        model = Administrador
        fields = "__all__"


class SedeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["region_sede"].empty_label = "Seleccione una región"
        self.fields["comuna_sede"].empty_label = "Seleccione una comuna"

    class Meta:
        model = Sede
        fields = "__all__"
        widgets = {
            "region_sede": forms.Select(
                attrs={
                    "id": "region-select",
                    "class": "form-control",
                    "required": "required",
                }
            ),
            "comuna_sede": forms.Select(
                attrs={
                    "id": "comuna-select",
                    "class": "form-control",
                    "required": "required",
                }
            ),
            "nombre_sede": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "direccion_sede": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "telefono_sede": forms.NumberInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "fotoSede": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class AsignaturaForm(forms.ModelForm):
    id_asignatura = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        max_length=9,
        error_messages={
            "unique": "El ID de la asignatura ya existe.",
        },
    )
    nombre_asignatura = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        max_length=30,
        error_messages={
            "unique": "El nombre de la asignatura ya existe.",
        },
    )
    profesor_asignatura = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        empty_label="Seleccione al docente",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )

    def clean_nombre_asignatura(self):
        nombre_asignatura = self.cleaned_data['nombre_asignatura']
        if self.instance.pk is None and Asignatura.objects.filter(nombre_asignatura=nombre_asignatura).exists():
            raise forms.ValidationError("El nombre de la asignatura ya existe.")
        return nombre_asignatura


    class Meta:
        model = Asignatura
        fields = "__all__"


class CursoForm(forms.ModelForm):
    id_curso = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "required": "required"}
        ),
        max_length=10,
        error_messages={
            "unique": "El ID del curso ya existe.",
        }
    )
    nombre_curso = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        max_length=30,
        error_messages={
            "unique": "El nombre del curso ya existe.",
        },
    )
    docente_curso = forms.ModelChoiceField(
        queryset=Docente.objects.all(),
        empty_label="Seleccione a un docente",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El docente seleccionado ya fue asignado a otro curso.",
        },
    )
    sala_curso = forms.ModelChoiceField(
        queryset=Sala.objects.all(),
        empty_label="Seleccione la sala",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "La sala seleccionada ya fue asignada a otro curso.",
        },
    )

    def clean_nombre_curso(self):
        nombre_curso = self.cleaned_data['nombre_curso']
        if self.instance.pk is None and Curso.objects.filter(nombre_curso=nombre_curso).exists():
            raise forms.ValidationError("El nombre del curso ya existe.")
        return nombre_curso

    def clean_docente_curso(self):
        docente_curso = self.cleaned_data['docente_curso']
        if self.instance.pk is None and Curso.objects.filter(docente_curso=docente_curso).exists():
            raise forms.ValidationError("El docente seleccionado ya fue asignado a otro curso.")
        return docente_curso

    def clean_sala_curso(self):
        sala_curso = self.cleaned_data['sala_curso']
        if self.instance.pk is None and Curso.objects.filter(sala_curso=sala_curso).exists():
            raise forms.ValidationError("La sala seleccionada ya fue asignada a otro curso.")
        return sala_curso

    class Meta:
        model = Curso
        fields = "__all__"


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = "__all__"
        widgets = {
            "fecha_publi": forms.SelectDateWidget(
                attrs={
                    "class": "form-control",
                    "style": "width:auto; display:inline-block;",
                },
                years=range(
                    date.today().year, date.today().year + 20
                ),  # Cambia el rango de años aquí
            ),
            "titulo": forms.TextInput(
                attrs={"class": "form-control", "required": "required"}
            ),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "required": "required"}
            ),
            "foto_noticia": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class SalaForm(forms.ModelForm):
    id_sala = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "required": "required"}
        ),
        error_messages={
            "unique": "El ID de la sala ya existe.",
        },
    )
    nombre_sala = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El nombre de la sala ya existe.",
        },
    )
    sede_sala = forms.ModelChoiceField(
        queryset=Sede.objects.all(),
        empty_label="Seleccione la sede",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )
    tipo_sala = forms.ModelChoiceField(
        queryset=Tipo_Sala.objects.all(),
        empty_label="Seleccione el tipo de sala",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"}),
    )

    class Meta:
        model = Sala
        fields = "__all__"
