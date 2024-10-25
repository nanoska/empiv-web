from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):

    SUBJECT_CHOICES = (
        ('', 'Seleccione un asunto'),
        ('eventos', 'Eventos'),
        ('talleres_grupales', 'Talleres Grupales'),
        ('aprendizaje_musical', 'Aprendizaje Musical'),
        ('clases_particulares', 'Clases Particulares'),
        ('sugerencia', 'Sugerencia'),
        ('felicitación', 'Felicitación'),
        ('otros', 'Otros'),
    )

    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label='Asunto', required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=100, label='Nombre', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, label='Teléfono', required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 11 1234 5678'}))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 15}), label='Mensaje', required=True)


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))


