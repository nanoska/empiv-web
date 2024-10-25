# from django import forms
# from .models import Theme, Sheet, Score, Version, Exercise, Lesson, Book

# class ThemeForm(forms.ModelForm):
#     class Meta:
#         model = Theme
#         fields = ['name', 'author', 'description', 'image']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del tema'}),
#             'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Autor (opcional)'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del tema'}),
#             'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

# class SheetForm(forms.ModelForm):
#     class Meta:
#         model = Sheet
#         fields = ['score', 'instrument', 'line', 'level', 'pdf', 'audio']
#         widgets = {
#             'score': forms.Select(attrs={'class': 'form-control'}),
#             'instrument': forms.Select(attrs={'class': 'form-control'}),
#             'line': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Línea (1-5)'}),
#             'level': forms.Select(attrs={'class': 'form-control'}),
#             'pdf': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'audio': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

# class ScoreForm(forms.ModelForm):
#     class Meta:
#         model = Score
#         fields = ['theme', 'arranger', 'concert_pitch', 'mode', 'pdf', 'audio']
#         widgets = {
#             'theme': forms.Select(attrs={'class': 'form-control'}),
#             'arranger': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Arreglista'}),
#             'concert_pitch': forms.Select(attrs={'class': 'form-control'}),
#             'mode': forms.Select(attrs={'class': 'form-control'}),
#             'pdf': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'audio': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }

# class VersionForm(forms.ModelForm):
#     class Meta:
#         model = Version
#         fields = ['theme', 'score', 'sheets', 'tone', 'mode', 'scale', 'level', 'genre', 'description']
#         widgets = {
#             'theme': forms.Select(attrs={'class': 'form-control'}),
#             'score': forms.Select(attrs={'class': 'form-control'}),
#             'sheets': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'tone': forms.Select(attrs={'class': 'form-control'}),
#             'mode': forms.Select(attrs={'class': 'form-control'}),
#             'scale': forms.Select(attrs={'class': 'form-control'}),
#             'level': forms.Select(attrs={'class': 'form-control'}),
#             'genre': forms.Select(attrs={'class': 'form-control'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción de la versión'}),
#         }


# class ExerciseForm(forms.ModelForm):
#     class Meta:
#         model = Exercise
#         fields = ['title', 'description', 'pdf', 'audio']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del ejercicio'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del ejercicio'}),
#             'pdf': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'audio': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }


# class LessonForm(forms.ModelForm):
#     class Meta:
#         model = Lesson
#         fields = ['title', 'description', 'pdf', 'audio']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la lección'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción de la lección'}),
#             'pdf': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#             'audio': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'description', 'pdf']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del libro'}),
#             'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del libro'}),
#             'pdf': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
#         }


        