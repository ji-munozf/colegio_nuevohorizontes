from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):

    rut_alumno = forms.CharField(widget=forms.TextInput, max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Alumno
        fields = '__all__'

class DocenteForm(forms.ModelForm):

    rut_docente = forms.CharField(widget=forms.TextInput, max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Docente
        fields = '__all__'

class ApoderadoForm(forms.ModelForm):

    rut_apoderado = forms.CharField(widget=forms.TextInput, max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)

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

        # Cambiar el asterisco por dos puntos en los labels
        self.fields['id_sede'].label = 'ID de la sede'
        self.fields['nombre_sede'].label = 'Nombre de la sede'
        self.fields['direccion_sede'].label = 'Dirección de la sede'
        self.fields['telefono_sede'].label = 'Teléfono de la sede'
        self.fields['fotoSede'].label = 'Foto de la sede'
        self.fields['region_sede'].label = 'Región de la sede'
        self.fields['comuna_sede'].label = 'Comuna de la sede'

    class Meta:
        model = Sede
        fields = ['id_sede', 'nombre_sede', 'direccion_sede', 'telefono_sede', 'fotoSede', 'region_sede', 'comuna_sede']
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
            'fecha_publi': forms.DateInput(
        format=('%d-%m-%Y'),
        attrs={'class': 'form-control', 
               'placeholder': 'Select a date',
               'type': 'date'
              }),
        }

class SalaForm(forms.ModelForm):

    class Meta:
        model = Sala
        fields = '__all__'

class MateriaForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = '__all__'