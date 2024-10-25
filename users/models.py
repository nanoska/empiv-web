from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from music.models import Instrument

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)  # Asegura que el email sea único

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_normal = models.BooleanField(default=False)

    image = models.ImageField(upload_to='users/', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.id} - {self.username}"
    

# %%

class Normal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', unique=True)
    instruments = models.ManyToManyField(Instrument, related_name='student_instruments', blank=True)
    primary_instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return f"Alumnx: {self.user.username} | {self.primary_instrument}"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instruments = models.ManyToManyField(Instrument, related_name='teacher_instruments')
    primary_instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, default=None, blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return f"{self.user.username}"
    

    