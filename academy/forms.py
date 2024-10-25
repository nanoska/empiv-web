

# from django import forms
# from .models import *


# class SingleClassForm(forms.ModelForm):
#     class Meta:
#         model = SingleClass
#         fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'short_description': forms.TextInput(attrs={'class': 'form-control'}),
#             'long_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
#             'price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'duration': forms.TextInput(attrs={'class': 'form-control'}),
#             'teacher': forms.Select(attrs={'class': 'form-control'}),
#             'student': forms.Select(attrs={'class': 'form-control'}),
#             'type': forms.Select(attrs={'class': 'form-control'}),
#             'modality': forms.Select(attrs={'class': 'form-control'}),
#         }


# class RepertoireForm(forms.ModelForm):
#     class Meta:
#         model = Repertoire
#         fields = ['name', 'description']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Repertorio'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
#         }