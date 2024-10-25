# # payments/forms.py

# from django import forms
# from .models import Payment, Expense, Subscription

# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['user', 'amount', 'payment_type', 'details']
#         widgets = {
#             'user': forms.Select(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'payment_type': forms.Select(attrs={'class': 'form-control'}),
#             'details': forms.Textarea(attrs={'class': 'form-control'}),
#         }

# class ExpenseForm(forms.ModelForm):
#     class Meta:
#         model = Expense
#         fields = ['description', 'amount']
#         widgets = {
#             'description': forms.TextInput(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#             'payment_type': forms.Select(attrs={'class': 'form-control'}),
#         }

# class SubscriptionForm(forms.ModelForm):
#     class Meta:
#         model = Subscription
#         fields = ['user', 'subscription_type', 'start_date', 'end_date', 'active']
#         widgets = {
#             'user': forms.Select(attrs={'class': 'form-control'}),
#             'subscription_type': forms.Select(attrs={'class': 'form-control'}),
#             'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         }
