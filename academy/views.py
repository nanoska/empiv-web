# from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.mixins import UserPassesTestMixin
# from django.urls import reverse_lazy

# from .models import *
# from .forms import *



# # Create your views here.

# # %% WORKSHOPS VIEWS

# class WorkshopListView(ListView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_list.html'
#     context_object_name = 'talleres'

#     def get_queryset(self):
#         return Workshop.objects.all().order_by('created_at')
    

# class MyWorkshopListView(ListView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_list.html'
#     context_object_name = 'talleres'

#     # obtener los workshops del usuario logueado que estan relacionados en Enrollment
#     def get_queryset(self):
#         return Workshop.objects.all()


# class WorkshopDetailView(DetailView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_detail.html'
#     context_object_name = 'workshop'


# class WorkshopCreateView(CreateView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_form.html'
#     fields = ['name', 'description', 'image']
#     success_url = '/talleres/'


# class WorkshopUpdateView(UpdateView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_update_form.html'
#     fields = '__all__'
#     success_url = '/talleres/'


# class WorkshopDeleteView(DeleteView):
#     model = Workshop
#     template_name = 'academy/workshops/workshop_confirm_delete.html'
#     success_url = '/talleres/'





# # %% SINGLE LESSONS VIEWS

# class SingleLessonsListView(ListView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lessons_list.html'
#     context_object_name = 'clases'


# class SingleLessonDetailView(DetailView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_detail.html'
#     context_object_name = 'clase'


# class SingleLessonCreateView(CreateView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_form.html'
#     fields = '__all__'
#     success_url = '/clases-particulares/'


# class SingleLessonUpdateView(UpdateView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_update_form.html'
#     fields = '__all__'
#     success_url = '/clases-particulares/'


# class SingleLessonDeleteView(DeleteView):
#     model = SingleClass
#     template_name = 'academy/single_lessons/single_lesson_confirm_delete.html'
#     success_url = '/clases-particulares/'
    

# # %% Repertoire

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