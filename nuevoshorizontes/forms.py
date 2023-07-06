from django import forms
from .models import *
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


class AlumnoForm(forms.ModelForm):
    rut_alumno = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required", "placeholder": "Ej: 12.345.678-9"}),
        max_length=14,
        error_messages={
            "unique": "El RUT del alumno ya existe.",
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

    def clean_rut_alumno(self):
        rut_alumno = self.cleaned_data.get("rut_alumno")
        rut_pattern = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9K]$'

        if not re.match(rut_pattern, rut_alumno):
            raise ValidationError("El rut del alumno debe tener el formato correcto (Ej: 12.345.678-9 o 12.345.678-K en mayúscula).")

        return rut_alumno

    def clean_correo_alumno(self):
        correo_alumno = self.cleaned_data.get("correo_alumno")
        instance = self.instance

        if instance is None:  # Agregar nuevo apoderado
            if Alumno.objects.filter(correo_alumno=correo_alumno).exists():
                raise ValidationError("El correo del docente ya existe.")
        else:  # Modificar apoderado existente
            if Alumno.objects.filter(correo_alumno=correo_alumno).exclude(rut_docente=instance.rut_docente).exists():
                raise ValidationError("El correo del docente ya existe para otro docente.")
        
        return correo_alumno

    class Meta:
        model = Alumno
        fields = "__all__"


class DocenteForm(forms.ModelForm):
    rut_docente = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required", "placeholder": "Ej: 12.345.678-9"}),
        max_length=14,
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

    def clean_rut_docente(self):
        rut_docente = self.cleaned_data.get("rut_docente")
        rut_pattern = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9K]$'

        if not re.match(rut_pattern, rut_docente):
            raise ValidationError("El rut del docente debe tener el formato correcto (Ej: 12.345.678-9 o 12.345.678-K en mayúscula).")

        return rut_docente

    def clean_correo_docente(self):
        correo_docente = self.cleaned_data.get("correo_docente")
        instance = self.instance

        if instance is None:  # Agregar nuevo apoderado
            if Docente.objects.filter(correo_docente=correo_docente).exists():
                raise ValidationError("El correo del docente ya existe.")
        else:  # Modificar apoderado existente
            if Docente.objects.filter(correo_docente=correo_docente).exclude(rut_docente=instance.rut_docente).exists():
                raise ValidationError("El correo del docente ya existe para otro docente.")
        
        return correo_docente

    class Meta:
        model = Docente
        fields = "__all__"


class ApoderadoForm(forms.ModelForm):
    rut_apoderado = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "required": "required", "placeholder": "Ej: 12.345.678-9"}),
        max_length=14,
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

    def clean_rut_apoderado(self):
        rut_apoderado = self.cleaned_data.get("rut_apoderado")
        rut_pattern = r'^\d{1,2}\.\d{3}\.\d{3}-[0-9K]$'

        if not re.match(rut_pattern, rut_apoderado):
            raise ValidationError("El rut del apoderado debe tener el formato correcto (Ej: 12.345.678-9 o 12.345.678-K en mayúscula).")

        return rut_apoderado

    def clean_correo_apoderado(self):
        correo_apoderado = self.cleaned_data.get("correo_apoderado")
        instance = self.instance

        if instance is None:  # Agregar nuevo apoderado
            if Apoderado.objects.filter(correo_apoderado=correo_apoderado).exists():
                raise ValidationError("El correo del apoderado ya existe.")
        else:  # Modificar apoderado existente
            if Apoderado.objects.filter(correo_apoderado=correo_apoderado).exclude(rut_apoderado=instance.rut_apoderado).exists():
                raise ValidationError("El correo del apoderado ya existe para otro apoderado.")
        
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
        correo_admin = self.cleaned_data.get("correo_admin")
        instance = self.instance

        if instance is None:  # Agregar nuevo administrador
            if Administrador.objects.filter(correo_admin=correo_admin).exists():
                raise ValidationError("El correo del admin ya existe.")
        else:  # Modificar administrador existente
            if Administrador.objects.filter(correo_admin=correo_admin).exclude(id=instance.id).exists():
                raise ValidationError("El correo del admin ya existe para otro administrador.")

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
        nombre_asignatura = self.cleaned_data.get("nombre_asignatura")
        instance = self.instance

        if instance is None:  # Agregar nueva asignatura
            if Asignatura.objects.filter(nombre_asignatura=nombre_asignatura).exists():
                raise ValidationError("El nombre de la asignatura ya existe.")
        else:  # Modificar asignatura existente
            if Asignatura.objects.filter(nombre_asignatura=nombre_asignatura).exclude(id_asignatura=instance.id_asignatura).exists():
                raise ValidationError("El nombre de la asignatura ya existe para otra asignatura.")
        
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
        nombre_curso = self.cleaned_data.get("nombre_curso")
        instance = self.instance

        if instance is None:  # Agregar nuevo curso
            if Curso.objects.filter(nombre_curso=nombre_curso).exists():
                raise ValidationError("El nombre del curso ya existe.")
        else:  # Modificar curso existente
            if Curso.objects.filter(nombre_curso=nombre_curso).exclude(id_curso=instance.id_curso).exists():
                raise ValidationError("El nombre del curso ya existe para otro curso.")
        
        return nombre_curso

    def clean_docente_curso(self):
        docente_curso = self.cleaned_data.get("docente_curso")
        instance = self.instance

        if instance is None:  # Agregar nuevo curso
            if Curso.objects.filter(docente_curso=docente_curso).exists():
                raise ValidationError("El docente seleccionado ya fue asignado a otro curso.")
        else:  # Modificar curso existente
            if Curso.objects.filter(docente_curso=docente_curso).exclude(id_curso=instance.id_curso).exists():
                raise ValidationError("El docente seleccionado ya fue asignado a otro curso.")
        
        return docente_curso

    def clean_sala_curso(self):
        sala_curso = self.cleaned_data.get("sala_curso")
        instance = self.instance

        if instance is None:  # Agregar nuevo curso
            if Curso.objects.filter(sala_curso=sala_curso).exists():
                raise ValidationError("La sala seleccionada ya fue asignada a otro curso.")
        else:  # Modificar curso existente
            if Curso.objects.filter(sala_curso=sala_curso).exclude(id_curso=instance.id_curso).exists():
                raise ValidationError("La sala seleccionada ya fue asignada a otro curso.")
        
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


class PagosColegioForm(forms.ModelForm):
    nombre_pago_colegio = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "required": "required"}
        ),
    )
    monto = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", "required": "required"})
    )
    tipo_pago_colegio = forms.ModelChoiceField(
        queryset=Tipo_pago_colegio.objects.all(),
        empty_label="Seleccione el tipo pago colegio",
        widget=forms.Select(attrs={"class": "form-control", "required": "required"})
    )

    def clean_nombre_pago_colegio(self):
        nombre_pago_colegio = self.cleaned_data.get("nombre_pago_colegio")
        instance = self.instance

        if instance is None:  # Agregar nueva sala
            if Pagos_colegio.objects.filter(nombre_pago_colegio=nombre_pago_colegio).exists():
                raise ValidationError("El nombre del pago colegio ya existe.")
        else:  # Modificar sala existente
            if Pagos_colegio.objects.filter(nombre_pago_colegio=nombre_pago_colegio).exclude(id_pago_colegio=instance.id_pago_colegio).exists():
                raise ValidationError("El nombre del pago colegio ya existe para otro pago colegio.")
            
        return nombre_pago_colegio

    class Meta:
        model = Pagos_colegio
        fields = "__all__"
        widgets = {
            "fecha_vencimiento": forms.SelectDateWidget(
                attrs={
                    "class": "form-control",
                    "style": "width:auto; display:inline-block;",
                },
                years=range(
                    date.today().year, date.today().year + 20
                ),  # Cambia el rango de años aquí
            )
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

    def clean_nombre_sala(self):
        nombre_sala = self.cleaned_data.get("nombre_sala")
        instance = self.instance

        if instance is None:  # Agregar nueva sala
            if Sala.objects.filter(nombre_sala=nombre_sala).exists():
                raise ValidationError("El nombre de la sala ya existe.")
        else:  # Modificar sala existente
            if Sala.objects.filter(nombre_sala=nombre_sala).exclude(id_sala=instance.id_sala).exists():
                raise ValidationError("El nombre de la sala ya existe para otra sala.")
            
        return nombre_sala

    class Meta:
        model = Sala
        fields = "__all__"
