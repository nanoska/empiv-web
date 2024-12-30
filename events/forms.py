from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'short_description', 'description', 'date', 'time', 'location', 'image']

        # Personalizar los widgets para los campos
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del evento'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descripción corta'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción completa'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ubicación'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Imagen'}),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'name', 'address', 'city', 'state', 'phone', 'email', 'website', 'image', 'capacity', 'iframe'
        ]

        # Personalizar los widgets para los campos
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la ubicación'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Sitio web'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capacidad'}),
            'iframe': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Iframe del mapa'}),
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))

