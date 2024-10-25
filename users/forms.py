
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Student
from music.models import Instrument

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_normal = True  # Ajustar al valor por defecto para nuevos usuarios
        if commit:
            user.save()
        return user


class CustomPasswordResetForm(PasswordResetForm):
    def send_mail(self, subject_template_name, email_template_name,
                context, from_email, to_email, html_email_template_name=None):

            subject = "Restablecer contraseña"
            body = render_to_string(email_template_name, context)
            email = EmailMessage(subject, body, from_email, [to_email])
            email.content_subtype = "html"
            email.send()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']
        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),

            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

            'image': forms.FileInput(attrs={'class': 'form-control'}),

        }



# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['user', 'instruments', 'primary_instrument']
#         widgets = {
#             'user': forms.Select(attrs={'class': 'form-control'}, choices=User.objects.filter(is_student=False)),
#             'instruments': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}, choices=Instrument.objects.all()),
#             'primary_instrument': forms.Select(attrs={'class': 'form-control'}, choices=Instrument.objects.all()),
#         }

#     def __init__(self, *args, **kwargs):
#         super(StudentForm, self).__init__(*args, **kwargs)
#         self.fields['user'].queryset = User.objects.filter(is_student=False)