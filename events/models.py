from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, default="Buenos Aires") # Cuidad (Buenos Aires)
    state = models.CharField(max_length=255, null=True, blank=True) # Localidad
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='locations')
    capacity = models.IntegerField(null=True, blank=True)
    iframe = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Event(models.Model):

    STATE_CHOICES = (
        ('vigente', 'vigente'),
        ('pasado', 'pasado'),
       ('proximo', 'proximo'),
    )

    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='events')
    state = models.CharField(max_length=255, choices=STATE_CHOICES, default='proximo') # Ver cambio automatico de state con serializers?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EventReservation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reservations', verbose_name='Evento')
    name = models.CharField(max_length=255, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=255, verbose_name='Teléfono')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

# class Galery(models.Model):
#     name = models.CharField(max_length=255)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='galeries')
#     image = models.ImageField(upload_to='galery')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
    

# class Photo(models.Model):
#     galery = models.ForeignKey(Galery, on_delete=models.CASCADE, related_name='photos')
#     image = models.ImageField(upload_to='photos')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.galery.name
    
