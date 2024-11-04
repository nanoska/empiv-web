# web/views.py

from academy.models import Workshop
from events.models import Event
from users.models import User #, Teacher
from .forms import ContactForm

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from typing import Any
import os
from dotenv import load_dotenv

load_dotenv()

WP_PHONE_NUMBER = os.getenv("WP_PHONE_NUMBER")

class LoginView(LoginView):

    def get_success_url(self):
        # Puedes definir aquí tus urls de redirección personalizadas
        if self.request.user.is_superuser:
            return resolve_url('home')
        elif self.request.user.is_staff:
            return resolve_url('student_list')
        elif hasattr(self.request.user, 'is_teacher') and self.request.user.is_teacher:
            return resolve_url('home')
        elif hasattr(self.request.user, 'is_student') and self.request.user.is_student:
            return resolve_url('home')
        else:
            return resolve_url('home')  # Un fallback por si acaso


class HomeView(TemplateView):
    template_name = 'main/home.html'

    def get_proximo_evento_id(self):
        events = Event.objects.all().order_by('date')
        today = timezone.now().date()
        if events:
            for event in events:
                if event.date >= today:
                    return event.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('-date')[:3]
        context['today'] = timezone.now().date()
        context['proximo_evento_id'] = self.get_proximo_evento_id()  
        context['message'] = self.request.GET.get('message', '')
        context['wp_phone_number'] = WP_PHONE_NUMBER
        return context
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        print()
        return self.render_to_response(context={'form': form, 
                                                'events': Event.objects.order_by('-date')[:3],
                                                'today': timezone.now().date(),
                                                'message': self.request.GET.get('message', ''),
                                                'wp_phone_number': WP_PHONE_NUMBER})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí puedes manejar el envío del formulario
            messages.success(request, 'Formulario enviado con éxito.')
            return self.render_to_response({'form': form, 
                                            'events': Event.objects.order_by('-date')[:3],
                                            'today': timezone.now().date(),
                                            'message': self.request.GET.get('message', ''),
                                            'wp_phone_number': WP_PHONE_NUMBER})
        return self.render_to_response({'form': form, 
                                        'events': Event.objects.order_by('-date')[:3],
                                        'today': timezone.now().date(),
                                        'message': self.request.GET.get('message', ''),
                                        'wp_phone_number': WP_PHONE_NUMBER})


    
class ContactView(TemplateView):
    template_name = 'main/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        context['message'] = self.request.GET.get('message', '')
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            # Procesar los datos del formulario
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']

            phone = form.cleaned_data['phone'].strip().replace(' ', '').replace('-', '')
            if phone.startswith('0'):
                phone = '549' + phone[1:]

            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Crear el contexto para el correo
            context = {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
                'subject': subject,
                'whatsapp_url': f"https://wa.me/+{phone}?text=Hola, {name}.",
            }


            # Enviar el correo
            send_mail(
                f'Nuevo mensaje de {name} - {subject}',
                render_to_string('emails/contact_email.html', context),
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Enviar el correo al usuario
            send_mail(
                f'¡Gracias por tu mensaje, {name}! Nos pondremos en contacto contigo pronto.',
                render_to_string('emails/contact_email_user.html', context),
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )


            # Redirigir o mostrar un mensaje de éxito
            return render(request, 'main/contact.html', {'form': form, 'message': 'Mensaje enviado con éxito.'})

        # Si el formulario no es válido, renderizar la página con los errores
        return render(request, 'main/contact.html', {'form': form})



class UnderConstructionView(TemplateView):
    template_name = 'main/under_construction.html'


# class SingleLessonsView(TemplateView):
#     template_name = 'main/single_lessons.html'


class AboutUsView(ListView):
    template_name = 'main/about_us.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_staff=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MEDIA_URL'] = settings.MEDIA_URL  # Añade MEDIA_URL al contexto
        context['talleres'] = Workshop.objects.all()
        return context
    
    
    

