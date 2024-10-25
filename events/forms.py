from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'location', 'description', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


class EventReservationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    guests = forms.IntegerField(min_value=1, max_value=10)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 15}))
    

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'name', 'address', 'city', 'state', 'phone', 
            'email', 'website', 'image', 'iframe'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la Ubicación'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Localidad'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Sitio Web'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'iframe': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Iframe del Mapa'}),
        }




class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['event', 'name', 'email', 'phone']
        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }


class EventReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['event', 'name', 'email', 'phone']

        widgets = {
            'event': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 11 1234-5678'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['event'].widget.attrs['readonly'] = True
        self.fields['event'].disabled = True