from django import forms
from .models import Alumno, Apoderado, Asignatura, Curso, Docente, Materia, Noticias, Sala, Sede

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
        model = Apoderado
        fields = '__all__'


class SedeForm(forms.ModelForm):

    class Meta:
        model = Sede
        fields = '__all__'

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