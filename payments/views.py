# # payments/views.py

# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.views.generic.base import TemplateView
# from django.contrib import messages

# from .models import *
# from .forms import *

# from django.utils.timezone import now
# from django.contrib.auth.mixins import LoginRequiredMixin


# class PaymentListView(ListView):
#     model = Payment
#     template_name = 'payments/payment_list.html'

# class PaymentCreateView(CreateView):
#     model = Payment
#     form_class = PaymentForm
#     template_name = 'payments/payment_form.html'
#     success_url = reverse_lazy('payment_list')

#     def form_valid(self, form):
#         messages.success(self.request, 'Pago registrado con éxito.')
#         return super().form_valid(form)

# class ExpenseListView(ListView):
#     model = Expense
#     template_name = 'payments/expense_list.html'

# class ExpenseCreateView(CreateView):
#     model = Expense
#     form_class = ExpenseForm
#     template_name = 'payments/expense_form.html'
#     success_url = reverse_lazy('expense_list')

#     def form_valid(self, form):
#         messages.success(self.request, 'Gasto registrado con éxito.')
#         return super().form_valid(form)

# class SubscriptionListView(ListView):
#     model = Subscription
#     template_name = 'payments/subscription_list.html'

# class SubscriptionCreateView(CreateView):
#     model = Subscription
#     form_class = SubscriptionForm
#     template_name = 'payments/subscription_form.html'
#     success_url = reverse_lazy('subscription_list')

#     def form_valid(self, form):
#         messages.success(self.request, 'Suscripción registrada con éxito.')
#         return super().form_valid(form)


# class FinancialDashboardView(LoginRequiredMixin, TemplateView):
#     template_name = 'payments/financial_dashboard.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['wallet_transactions'] = Transaction.objects.filter(user=self.request.user).order_by('-date')
#         context['subscriptions'] = Subscription.objects.filter(user=self.request.user).order_by('-end_date')
#         context['payments'] = Payment.objects.all().order_by('-date')
#         context['expenses'] = Expense.objects.all().order_by('-date')
#         return context
    

# class PaymentsDashboardView(LoginRequiredMixin, TemplateView):
#     template_name = 'payments/payments_dashboard.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['payments'] = Payment.objects.filter(user=self.request.user).order_by('-date')
#         context['subscriptions'] = Subscription.objects.filter(user=self.request.user).order_by('-end_date')
#         return context
    

# class PaymentWorkshopView(CreateView):
#     model = Payment
#     form_class = PaymentForm
#     template_name = 'payments/payment_form.html'
#     success_url = reverse_lazy('payments_dashboard')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.payment_type = 'event'  # Asumiendo que 'Aporte para Talleres' se categoriza como 'event'
#         form.instance.details = 'Aporte para Talleres'
#         return super().form_valid(form)

# class PaymentHatView(CreateView):
#     model = Payment
#     form_class = PaymentForm
#     template_name = 'payments/payment_form.html'
#     success_url = reverse_lazy('payments_dashboard')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.payment_type = 'donation'  # Asumiendo que 'Gorra' se categoriza como 'donation'
#         form.instance.details = 'Gorra'
#         return super().form_valid(form)