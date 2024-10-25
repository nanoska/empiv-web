# # tickets/models.py
# from django.db import models
# from django.utils import timezone
# from users.models import User
# from django.utils.translation import gettext_lazy as _

# class Ticket(models.Model):
#     TICKET_TYPE_CHOICES = [
#         ('bug', 'Error'),
#         ('feature', 'Mejoras'),
#         ('other', 'Other'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
#     title = models.CharField(max_length=200, verbose_name=_('Título'))
#     description = models.TextField(verbose_name=_('Descripción'))
#     ticket_type = models.CharField(max_length=50, choices=TICKET_TYPE_CHOICES, verbose_name=_('Tipo de Ticket'))
#     is_resolved = models.BooleanField(default=False, verbose_name=_('Está Resuelto'))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de Creación'))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Fecha de Actualización'))
#     user_agent = models.CharField(max_length=255, blank=True, null=True)  # Para almacenar la información del navegador
#     page_url = models.URLField(blank=True, null=True)  # Para almacenar la URL de la página donde se generó el ticket

#     def __str__(self):
#         return f"{self.title} ({self.user.username})"

# class TicketChat(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='chats')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.TextField()
#     timestamp = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"Chat on {self.ticket.title} by {self.user.username}"

# class Message(models.Model):
#     chat = models.ForeignKey(TicketChat, on_delete=models.CASCADE, related_name='messages')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"Message by {self.user.username} at {self.timestamp}"
