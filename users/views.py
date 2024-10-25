from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import CustomPasswordResetForm, CustomUserCreationForm
from django.contrib.auth.views import PasswordResetView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .models import *
from .forms import UserEditForm
from django.views.generic.edit import UpdateView


class RegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Asegúrate de definir esta URL en tus urls.py

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # Opcionalmente puedes manejar la lógica para un formulario inválido aquí
        return super().form_invalid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = 'registration/password_reset_done.html'

    def get(self, request, *args, **kwargs):
        form = CustomPasswordResetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name=self.email_template_name,
                subject_template_name=self.subject_template_name,
                from_email=self.from_email,
                html_email_template_name=self.html_email_template_name,
                extra_email_context=self.extra_email_context,
            )
            return render(request, self.success_url)
        return render(request, self.template_name, {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('home')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class ProfileDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/user_edit.html'
    success_url = reverse_lazy('profile_dashboard')

    def get_object(self):
        return self.request.user
    

