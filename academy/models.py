from django.db import models
from users.models import *
from events.models import *
# from library.models import *


# class SingleClass(models.Model):

#     TYPE_CHOICES = [
#         ('1', 'Instrumento'),
#         ('2', 'Teoria'),
#         ('3', 'Otro')
#     ]

#     MODALITY_CHOICES = [
#         ('1', 'Presencial'),
#         ('2', 'Online'),
#         ('3', 'Híbrido'),
#         ('4', 'A domicilio'),
#         ('5', 'Asincrónico')
#     ]

#     title = models.CharField(max_length=100)
#     short_description = models.CharField(max_length=255)
#     long_description = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
#     duration = models.DurationField()
#     type = models.CharField(max_length=1, choices=TYPE_CHOICES)
#     modality = models.CharField(max_length=1, choices=MODALITY_CHOICES)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='single_lessons', null=True, blank=True)

#     def __str__(self):
#         return self.title
    

class Workshop(models.Model):

    DAY_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo')
    ]

    TYPE_CHOICES = [
        ('1', 'Instrumento'),
        ('2', 'Teoria'),
        ('3', 'Taller'),
        ('4', 'Otro')
    ]

    MODALITY_CHOICES = [
        ('1', 'Presencial'),
        ('2', 'Online'),
        ('3', 'Híbrido'),
        ('4', 'A domicilio'),
        ('5', 'Asincrónico')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    day = models.CharField(max_length=15, choices=DAY_CHOICES)
    init_time = models.TimeField()
    end_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='workshops')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    max_participants = models.PositiveIntegerField()
    # teachers = models.ManyToManyField(Teacher, related_name='workshops', blank=True)

    def __str__(self):
        return self.name
    

# class GroupClass(models.Model):

#     TYPE_CHOICES = [
#         ('1', 'Instrumento'),
#         ('2', 'Teoria'),
#         ('3', 'Taller'),
#         ('4', 'Otro')
#     ]

#     MODALITY_CHOICES = [
#         ('1', 'Presencial'),
#         ('2', 'Online'),
#         ('3', 'Híbrido'),
#         ('4', 'A domicilio'),
#         ('5', 'Asincrónico')
#     ]

#     title = models.CharField(max_length=100)
#     short_description = models.CharField(max_length=255)
#     long_description = models.TextField()
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     duration = models.DurationField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='group_lessons')
#     students = models.ManyToManyField(Student, related_name='group_lessons')
#     type = models.CharField(max_length=1, choices=TYPE_CHOICES)
#     modality = models.CharField(max_length=1, choices=MODALITY_CHOICES)
#     max_students = models.PositiveIntegerField()

#     def __str__(self):
#         return self.title


# # class Enrollment(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.workshop.name}"


# class Repertoire(models.Model):
#     name = models.CharField(max_length=255)
#     versions = models.ManyToManyField(Version, related_name='repertoires', blank=True)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='repertoires', null=True, blank=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


    

    