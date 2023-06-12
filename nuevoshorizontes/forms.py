from django import forms
from .models import *
from datetime import date

class AlumnoForm(forms.ModelForm):

    rut_alumno = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}), max_length=10)
    nombre_alumno = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    appaterno_alumno = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    apmaterno_alumno = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    direccion_alumno = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    telefono_alumno = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}), required=False)
    correo_alumno = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "required": "required"}))
    sede_alumno = forms.ModelChoiceField(queryset=Sede.objects.all(), empty_label="Seleccione una sede", widget=forms.Select(attrs={"class": "form-control", "required": "required"}))
    apoderado_alumno = forms.ModelChoiceField(queryset=Apoderado.objects.all(), empty_label="Seleccione un apoderado", widget=forms.Select(attrs={"class": "form-control", "required": "required"}))
    curso_alumno = forms.ModelChoiceField(queryset=Curso.objects.all(), empty_label="Seleccione el curso", widget=forms.Select(attrs={"class": "form-control", "required": "required"}))

    class Meta:
        model = Alumno
        fields = '__all__'

class DocenteForm(forms.ModelForm):

    rut_docente = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}), max_length=10)
    nombre_docente = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    appaterno_docente = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    apmaterno_docente = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    direccion_docente = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    telefono_docente = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "required": "required"}))
    correo_docente = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "required": "required"}))
    sede_docente = forms.ModelChoiceField(queryset=Sede.objects.all(), empty_label="Seleccione una sede", widget=forms.Select(attrs={"class": "form-control", "required": "required"}))
    asignaturas_docente = forms.ModelMultipleChoiceField(queryset=Asignatura.objects.all(), widget=forms.SelectMultiple(attrs={"class": "form-control", "required": "required"}))

    class Meta:
        model = Docente
        fields = '__all__'

class ApoderadoForm(forms.ModelForm):

    rut_apoderado = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}), max_length=10)
    nombre_apoderado = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    appaterno_apoderado = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    apmaterno_apoderado = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    direccion_apoderado = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    telefono_apoderado = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control", "required": "required"}))
    correo_apoderado = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "required": "required"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "required": "required"}))

    class Meta:
        model = Apoderado
        fields = '__all__'

class AdminForm(forms.ModelForm):

    rut_admin = forms.CharField(widget=forms.TextInput, max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Administrador
        fields = '__all__'

class SedeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region_sede'].empty_label = 'Seleccione una región'
        self.fields['comuna_sede'].empty_label = 'Seleccione una comuna'

    class Meta:
        model = Sede
        fields = ['nombre_sede', 'direccion_sede', 'telefono_sede', 'fotoSede', 'region_sede', 'comuna_sede']
        widgets = {
            'region_sede': forms.Select(attrs={'id': 'region-select'}),
            'comuna_sede': forms.Select(attrs={'id': 'comuna-select'})
        }


class AsignaturaForm(forms.ModelForm):

    class Meta:
        model = Asignatura
        fields = '__all__'

class CursoForm(forms.ModelForm):

    class Meta:
        model = Curso
        fields = '__all__'

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticias
        fields = '__all__'
        widgets = {
            "fecha_publi": forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'style': 'width:auto; display:inline-block;'
                },
                years=range(date.today().year, date.today().year + 20)  # Cambia el rango de años aquí
            ),
            "titulo": forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required'
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': 'required'
                }
            ),
            "foto_noticia": forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'required': 'required'
                }
            )
        }

class SalaForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = '__all__'