from django import forms
from .models import *

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