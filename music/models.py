from django.db import models

# # Create your models here.
# class Instrument(models.Model):
#     TYPE_CHOICES = [
#         ('brass', 'Brass'),
#         ('woodwind', 'Woodwind'),
#     ]

#     TONE_CHOICES = [
#         ('C', 'C'),
#         ('Bb', 'Bb'),
#         ('Eb', 'Eb'),
#     ]

#     name = models.CharField(max_length=255, null=True, blank=True)
#     type = models.CharField(max_length=255, choices=TYPE_CHOICES)
#     image = models.ImageField(upload_to='instruments', null=True, blank=True)
#     tone = models.CharField(max_length=255, choices=TONE_CHOICES)

#     def __str__(self):
#         return f"{self.name} | {self.tone}"
    

# class Rithm(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     time = models.IntegerField()
#     image = models.ImageField(upload_to='rithms')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name 


# class Genre(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     image = models.ImageField(upload_to='genres')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name  
    

# class Note(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     image = models.ImageField(upload_to='notes')
#     absolute_name = models.CharField(max_length=255, null=True, blank=True)
#     sound = models.FileField(upload_to='sounds')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    
# class Chord(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     notes = models.ManyToManyField(Note)
#     intervals = models.ManyToManyField('Interval')
#     image = models.ImageField(upload_to='chords', null=True, blank=True)
#     sound = models.FileField(upload_to='sounds', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    

# class Mode(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     image = models.ImageField(upload_to='modes')
#     sound = models.FileField(upload_to='sounds')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


# class Scale(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     mode = models.ForeignKey(Mode, on_delete=models.CASCADE)
#     notes = models.ManyToManyField(Note)
#     chords = models.ManyToManyField(Chord)
#     image = models.ImageField(upload_to='scales')
#     sound = models.FileField(upload_to='sounds')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.name} | {self.mode}"
    

# class Interval(models.Model):
#     notes = models.ManyToManyField(Note)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     distance = models.IntegerField() # in semitones
#     image = models.ImageField(upload_to='intervals', null=True, blank=True)
#     sound = models.FileField(upload_to='sounds', null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    


# from django.db import models

# class Nota(models.Model):
#     TIPO_NOTA_CHOICES = [
#         ('negra', 'Negra'),
#         ('blanca', 'Blanca'),
#         ('corchea', 'Corchea'),
#         ('semicorchea', 'Semicorchea'),
#         ('redonda', 'Redonda'),
#         ('semifusa', 'Semifusa'),
#     ]

#     POSICION_PENTAGRAMA_CHOICES = [
#         ('C4', 'Do4'),
#         ('D4', 'Re4'),
#         ('E4', 'Mi4'),
#         ('F4', 'Fa4'),
#         ('G4', 'Sol4'),
#         ('A4', 'La4'),
#         ('B4', 'Si4'),
#         # Añadir más posiciones según sea necesario
#     ]

#     tipo = models.CharField(max_length=20, choices=TIPO_NOTA_CHOICES, help_text="Tipo de nota")
#     posicion = models.CharField(max_length=20, choices=POSICION_PENTAGRAMA_CHOICES, help_text="Posición en el pentagrama")

#     def __str__(self):
#         return f"{self.get_tipo_display()} en {self.get_posicion_display()}"

# class Compas(models.Model):
#     numero = models.PositiveIntegerField(help_text="Número del compás")
#     notas = models.ManyToManyField(Nota, related_name="compases")

#     def __str__(self):
#         return f"Compás {self.numero}"

# class ClaveRitmo(models.Model):
#     TIEMPOS_CHOICES = [
#         ('4/4', '4/4'),
#         ('3/4', '3/4'),
#         ('2/4', '2/4'),
#         ('6/8', '6/8'),
#         # Añadir más claves de ritmo según sea necesario
#     ]

#     tiempos = models.CharField(max_length=10, choices=TIEMPOS_CHOICES, help_text="Clave de ritmo")

#     def __str__(self):
#         return self.get_tiempos_display()
    
# class Melodia(models.Model):
#     titulo = models.CharField(max_length=100, help_text="Título de la melodía")
#     compases = models.ManyToManyField(Compas, related_name="melodias")
#     clave_ritmo = models.ForeignKey(ClaveRitmo, on_delete=models.CASCADE, related_name="melodias")
#     notas = models.ManyToManyField(Nota, related_name="melodias")
#     def __str__(self):
#         return self.titulo
    


# class Sound(models.Model):
#     FREQUENCY_CHOICES = [(i, f"{i} Hz") for i in range(20, 20001, 20)]  # Frecuencias típicas del rango audible humano

#     name = models.CharField(max_length=100, help_text="Nombre del sonido")
#     frequency = models.IntegerField(choices=FREQUENCY_CHOICES, help_text="Frecuencia del sonido en Hz")
#     amplitude = models.FloatField(help_text="Amplitud del sonido en dB")
#     duration = models.FloatField(help_text="Duración del sonido en segundos")
#     timbre = models.CharField(max_length=100, help_text="Timbre o calidad del sonido")
#     speed = models.FloatField(default=343.0, help_text="Velocidad del sonido en m/s")
#     wavelength = models.FloatField(help_text="Longitud de onda del sonido en metros")

#     def __str__(self):
#         return self.name

#     def save(self, *args, **kwargs):
#         # Calcular longitud de onda basándose en la frecuencia y la velocidad
#         if self.frequency > 0:
#             self.wavelength = self.speed / self.frequency
#         super(Sound, self).save(*args, **kwargs)
        

# class Tone(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)
#     frequency = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
