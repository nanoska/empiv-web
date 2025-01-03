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

    
    def get_proximo_evento_id(self):
        events = Event.objects.all().order_by('date')
        today = timezone.now().date()
        if events:
            for event in events:
                if event.date >= today:
                    return event.id

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        context['proximo_evento_id'] = self.get_proximo_evento_id() 
        context['page_title'] = 'Eventos'
        return context
    

class EventDetailView(DetailView, FormView):
    model = Event
    template_name = 'events/event_detail.html'
    form_class = EventForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['today'] = timezone.now().date()
        return context


class EventUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events')


class EventDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('events')
    template_name = 'events/event_confirm_delete.html'


class EventCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        return super().form_valid(form)
    

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


class LocationDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Location
    success_url = reverse_lazy('location_list')
    template_name = 'events/location_confirm_delete.html'

