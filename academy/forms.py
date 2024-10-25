from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class SingleClassForm(forms.ModelForm):
    class Meta:
        model = SingleClass
        fields = [
            'title', 
            'short_description', 
            'long_description', 
            'price', 
            'duration', 
            'teacher', 
            'student', 
            'type', 
            'modality'
        ]
        widgets = {
            'type': forms.RadioSelect,  # Puedes usar RadioSelect para mostrar opciones de tipo
            'modality': forms.RadioSelect,  # También puedes usarlo para la modalidad si lo prefieres
            'duration': forms.TextInput(attrs={'placeholder': 'Ingrese la duración en horas y minutos'}),
        }

    def __init__(self, *args, **kwargs):
        super(SingleClassForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = [
            'name',
            'description',
            'day',
            'init_time',
            'end_time',
            'price',
            'location',
            'image',
            'max_participants',
            'teachers'
        ]
        widgets = {
            'day': forms.Select,  # Usa un select para escoger el día
            'init_time': forms.TimeInput(format='%H:%M'),
            'end_time': forms.TimeInput(format='%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(WorkshopForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))


# class RepertoireForm(forms.ModelForm):
#     class Meta:
#         model = Repertoire
#         fields = ['name', 'description']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Repertorio'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
#         }