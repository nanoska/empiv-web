from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from core.mixins import StaffRequiredMixin
from django.contrib import messages

from .models import *
from .forms import *

from django.shortcuts import get_object_or_404
from django.utils import timezone

import os
from dotenv import load_dotenv

load_dotenv()

WP_PHONE_NUMBER = os.getenv('WP_PHONE_NUMBER')


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

class EventDetailView(DetailView, FormView):
    model = Event
    template_name = 'events/event_detail.html'
    form_class = EventReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['today'] = timezone.now().date()
        return context

    def get_form(self, form_class=None):
        event = self.get_object()
        form = super().get_form(form_class)
        form.fields['event'].initial = event
        form.fields['event'].widget.attrs['readonly'] = True
        return form

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Reserva realizada con éxito.')
        return redirect(reverse('event_detail', args=[self.get_object().id]))


class EventUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_update_form.html'
    success_url = reverse_lazy('events')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['event'] = self.get_object()
        return context

    def form_valid(self, form):
        return super().form_valid(form)


class EventDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = 'events/event_confirm_delete.html'


class EventCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_create_form.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        return super().form_valid(form)
    


# class EventReservationCreateView(FormView):
#     form_class = EventReservationForm
#     template_name = 'events/event_reservation.html'
#     success_url = reverse_lazy('events')

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, 'Reserva realizada con éxito.')
#         return super().form_valid(form)

# %% Locations

class LocationDetailView(DetailView):
    model = Location
    template_name = 'events/location_detail.html'
    context_object_name = 'location'


class LocationCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'events/location_form.html'
    success_url = reverse_lazy('under_construction')


class LocationUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Location
    form_class = LocationForm
    template_name = 'events/location_form.html'
    success_url = reverse_lazy('under_construction')


class LocationListView(ListView):
    model = Location
    template_name = 'events/location_list.html'
    context_object_name = 'locations'


# %% Reservation

# class EventReservationView(CreateView):
#     model = Reservation
#     form_class = ReservationForm
#     template_name = 'events/event_reservation.html'

#     def get_success_url(self):
#         return reverse('event_detail', args=[self.object.event.id])

#     def form_valid(self, form):
#         form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
#         messages.success(self.request, 'Reservación exitosa.')
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['event'] = get_object_or_404(Event, pk=self.kwargs['pk'])
#         context['wp_phone_number'] = WP_PHONE_NUMBER
#         return context
    