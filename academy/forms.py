from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *

# class SingleClassForm(forms.ModelForm):
#     class Meta:
#         model = SingleClass
#         fields = ['title', 'short_description', 'long_description', 'price', 'duration', 'teacher', 'type', 'modality']

#         # Personalizar los widgets para algunos campos
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la clase'}),
#             'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción corta'}),
#             'long_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción larga'}),
#             'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
#             'duration': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
#             'type': forms.Select(attrs={'class': 'form-control'}),
#             'modality': forms.Select(attrs={'class': 'form-control'}),
#             'teacher': forms.Select(attrs={'class': 'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(SingleClassForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Guardar'))

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['name', 'description', 'day', 'init_time', 'end_time', 'price', 'location', 'image', 'max_participants'] #, 'teachers']

        # Personalizar los widgets para algunos campos
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del taller'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del taller'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'init_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'max_participants': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Máximo de participantes'}),
            #'teachers': forms.SelectMultiple(attrs={'class': 'form-control'}),
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