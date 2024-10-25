# from django.db import models
# from music.models import *

# class Theme(models.Model):
#     name = models.CharField(max_length=255)
#     author = models.CharField(max_length=255, null=True, blank=True)
#     description = models.TextField()
#     image = models.ImageField(upload_to='themes', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    

# class Sheet(models.Model):

#     LEVEL_CHOICES = [
#         ('beginner', 'Inicial'),
#         ('intermediate', 'Intermedio'),
#         ('advanced', 'Avanzado'),
#     ]

#     score = models.ForeignKey('Score', on_delete=models.CASCADE, related_name='sheets', null=True, blank=True)
#     instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, related_name='sheets')
#     line = models.IntegerField() # 1, 2, 3, 4, 5
#     level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
#     pdf = models.FileField(upload_to='sheets', null=True, blank=True)
#     audio = models.FileField(upload_to='audios', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.score} | {self.instrument}"
    

# class Score(models.Model):
#     theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True, blank=True)
#     arranger = models.CharField(max_length=255)
#     concert_pitch = models.ForeignKey(Tone, on_delete=models.CASCADE, null=True, blank=True)
#     mode = models.ForeignKey(Scale, on_delete=models.CASCADE, null=True, blank=True)
#     pdf = models.FileField(upload_to='scores')
#     audio = models.FileField(upload_to='audios', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.title} para [{len(self.sheets.all())}] instrumentos de viento"
    

# class Version(models.Model):

#     MODE_CHOICES = [
#         ('major', 'Mayor'),
#         ('minor', 'Menor'),
#     ]

#     LEVEL_CHOICES = [
#         ('beginner', 'Inicial'),
#         ('intermediate', 'Intermedio'),
#         ('advanced', 'Avanzado'),
#     ]

#     title = models.CharField(max_length=255)
#     theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='versions', null=True, blank=True)
#     description = models.TextField()
#     level = models.CharField(max_length=255, choices=LEVEL_CHOICES)
#     score = models.ForeignKey(Score, on_delete=models.CASCADE, null=True, blank=True)
#     sheets = models.ManyToManyField(Sheet, blank=True)
#     tone = models.ForeignKey(Tone, on_delete=models.CASCADE, null=True, blank=True, related_name='versions')
#     mode = models.CharField(max_length=255, choices=MODE_CHOICES, null=True, blank=True)
#     scale = models.ForeignKey(Scale, on_delete=models.CASCADE, null=True, blank=True, related_name='versions')
#     genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True, related_name='versions')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    

# class Exercise(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, null=True, blank=True)
#     pdf = models.FileField(upload_to='exercises', null=True, blank=True)
#     audio = models.FileField(upload_to='audios', null=True, blank=True)
#     video = models.FileField(upload_to='videos', null=True, blank=True)
#     tone = models.ForeignKey(Tone, on_delete=models.CASCADE, null=True, blank=True)
#     scale = models.ForeignKey(Scale, on_delete=models.CASCADE, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    

# class Lesson(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     pdf = models.FileField(upload_to='lessons', null=True, blank=True)
#     audio = models.FileField(upload_to='audios', null=True, blank=True)
#     video = models.FileField(upload_to='videos', null=True, blank=True)
#     tone = models.ForeignKey(Tone, on_delete=models.CASCADE)
#     scale = models.ForeignKey(Scale, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    

# class Book(models.Model):

#     TYPE_CHOICES = [
#         ('theory', 'Teoría'),
#         ('practice', 'Práctica'),
#         ('real_book', 'Real Book'),
#     ]

#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     description = models.TextField()
#     type = models.CharField(max_length=255, choices=TYPE_CHOICES, null=True, blank=True)
#     instruments = models.ManyToManyField(Instrument, related_name='books')
#     instrument_type = models.CharField(max_length=255, choices=Instrument.TYPE_CHOICES, null=True, blank=True)
#     pdf = models.FileField(upload_to='books', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
    