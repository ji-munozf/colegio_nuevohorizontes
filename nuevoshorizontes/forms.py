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

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Alumno.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Alumno.DoesNotExist:
            return field_value
        
    def clean_rut_alumno(self):
        return self.clean_field("rut_alumno")
    
    def clean_correo_alumno(self):
        return self.clean_field("correo_alumno")

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
    asignaturas_docente = forms.ModelMultipleChoiceField(
        queryset=Asignatura.objects.all(),
        widget=forms.SelectMultiple(
            attrs={"class": "form-control", "required": "required"}
        ),
    )

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Docente.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Docente.DoesNotExist:
            return field_value
        
    def clean_rut_docente(self):
        return self.clean_field("rut_docente")
    
    def clean_correo_docente(self):
        return self.clean_field("correo_docente")

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

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Apoderado.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Apoderado.DoesNotExist:
            return field_value
        
    def clean_rut_apoderado(self):
        return self.clean_field("rut_apoderado")
    
    def clean_correo_apoderado(self):
        return self.clean_field("correo_apoderado")

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

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Administrador.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Administrador.DoesNotExist:
            return field_value
        
    def clean_correo_admin(self):
        return self.clean_field("correo_admin")

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
        max_length=6,
        error_messages={
            "unique": "El ID de la asignatura ya existe.",
        },
    )
    nombre_asignatura = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
        error_messages={
            "unique": "El nombre de la asignatura ya existe.",
        },
    )

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Asignatura.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Asignatura.DoesNotExist:
            return field_value

    def clean_id_asignatura(self):
        return self.clean_field("id_asignatura")

    def clean_nombre_asignatura(self):
        return self.clean_field("nombre_asignatura")

    class Meta:
        model = Asignatura
        fields = "__all__"


class CursoForm(forms.ModelForm):
    id_curso = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "required": "required"}
        ),
        error_messages={
            "unique": "El ID del curso ya existe.",
        }
    )
    nombre_curso = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}),
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

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Curso.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Curso.DoesNotExist:
            return field_value

    def clean_id_curso(self):
        return self.clean_field("id_curso")

    def clean_nombre_curso(self):
        return self.clean_field("nombre_curso")
    
    def clean_docente_curso(self):
        return self.clean_field("docente_curso")

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

    def clean_field(self, field_name):
        field_value = self.cleaned_data[field_name]
        try:
            Sala.objects.get(**{field_name: field_value})
            raise ValidationError(self.fields[field_name].error_messages["unique"])
        except Sala.DoesNotExist:
            return field_value

    def clean_id_sala(self):
        return self.clean_field("id_sala")

    def clean_nombre_sala(self):
        return self.clean_field("nombre_sala")

    class Meta:
        model = Sala
        fields = "__all__"
