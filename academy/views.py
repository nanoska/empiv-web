from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import StaffRequiredMixin
from django.urls import reverse_lazy

from .models import *
from .forms import *

# cargar variables de entorno wp_number
import os
from dotenv import load_dotenv  
load_dotenv()

WP_PHONE_NUMBER = os.getenv('WP_PHONE_NUMBER')

# %% WORKSHOPS VIEWS

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'academy/workshops/workshop_list.html'
    context_object_name = 'talleres'

    def get_queryset(self):
        return Workshop.objects.all().order_by('created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wp_phone_number'] = WP_PHONE_NUMBER
        return context
    

class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'academy/workshops/workshop_detail.html'
    context_object_name = 'workshop'


class WorkshopCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
    model = Workshop
    template_name = 'academy/workshops/workshop_form.html'
    fields = '__all__'
    success_url = reverse_lazy('workshop_list')


class WorkshopUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    model = Workshop
    template_name = 'academy/workshops/workshop_update_form.html'
    fields = '__all__'
    success_url = reverse_lazy('workshop_list')


class WorkshopDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
    model = Workshop
    template_name = 'academy/workshops/workshop_confirm_delete.html'
    success_url = reverse_lazy('workshop_list')


# class MyWorkshopListView(ListView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_list.html'
#     context_object_name = 'talleres'

#     def get_queryset(self):
#         return Workshop.objects.all()


# %% SINGLE LESSONS VIEWS

# class SingleLessonsListView(ListView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lessons_list.html'
#     context_object_name = 'clases'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['wp_phone_number'] = WP_PHONE_NUMBER
#         return context


# class SingleLessonDetailView(DetailView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_detail.html'
#     context_object_name = 'clase'


# class SingleLessonCreateView(LoginRequiredMixin, StaffRequiredMixin, CreateView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_form.html'
#     fields = '__all__'
#     success_url = '/academia/clases-particulares/'


# class SingleLessonUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_update_form.html'
#     fields = '__all__'
#     success_url = '/academia/clases-particulares/'


# class SingleLessonDeleteView(LoginRequiredMixin, StaffRequiredMixin, DeleteView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_confirm_delete.html'
#     success_url = '/academia/clases-particulares/'
    

# %% Repertoire

# class RepertoireListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
#     model = Repertoire
#     template_name = 'events/repertoire_list.html'
#     context_object_name = 'repertoires'

#     def test_func(self):
#         return self.request.user.is_staff

# class RepertoireCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
#     model = Repertoire
#     form_class = RepertoireForm
#     template_name = 'events/repertoire_form.html'
#     success_url = reverse_lazy('repertoire_list')

#     def test_func(self):
#         return self.request.user.is_staff

# class RepertoireUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Repertoire
#     form_class = RepertoireForm
#     template_name = 'events/repertoire_form.html'
#     success_url = reverse_lazy('repertoire_list')

#     def test_func(self):
#         return self.request.user.is_staff

# class RepertoireDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Repertoire
#     template_name = 'events/repertoire_confirm_delete.html'
#     success_url = reverse_lazy('repertoire_list')

#     def test_func(self):
#         return self.request.user.is_staff