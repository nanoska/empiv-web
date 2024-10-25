# # payments/models.py

# from django.db import models
# # from django.contrib.auth.models import User
# from users.models import User
# from django.utils.timezone import now
# from django.urls import reverse

# class Payment(models.Model):
#     PAYMENT_CHOICES = [
#         ('subscription', 'Subscripción'),
#         ('donation', 'Donación'),
#         ('event', 'Evento (gorra)'),
#         ('other', 'Otro')
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(default=now)
#     payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
#     details = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.amount} - {self.payment_type}"

# class Expense(models.Model):

#     PAYMENT_TYPES = [
#         ('payment', 'Pago'),
#         ('expense', 'Gasto'),
#     ]

#     description = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(default=now)
#     payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPES)

#     def __str__(self):
#         return f"{self.description} - {self.amount} - {self.payment_type}"

# class Subscription(models.Model):
#     SUBSCRIPTION_CHOICES = [
#         ('student', 'Estudiante'),
#         ('normal', 'Clasica'),
#         ('music_learning', 'Aprendizaje Musical'),
#         ('premium', 'Premium'),
#         ('other', 'Otro')
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     subscription_type = models.CharField(max_length=50, choices=SUBSCRIPTION_CHOICES)
#     start_date = models.DateField(default=now)
#     end_date = models.DateField()
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.subscription_type} - {self.active}"

#     def get_absolute_url(self):
#         return reverse('subscription_detail', kwargs={'pk': self.pk})


# class Wallet(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     balance = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"{self.user.username} - {self.balance}"
    

# class Transaction(models.Model):
#     PAYMENT_CHOICES = [
#         ('subscription', 'Subscripción'),
#         ('donation', 'Donación'),
#         ('event', 'Evento (gorra)'),
#         ('other', 'Otro'),
#         ('payment', 'Pago'),
#         ('expense', 'Gasto'),
#     ]

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(default=now)
#     transaction_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
#     details = models.TextField(blank=True, null=True)
#     inout = models.BooleanField(default=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.amount} - {self.transaction_type}"
    