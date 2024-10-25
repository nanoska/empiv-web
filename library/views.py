# from django.shortcuts import render
# from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
# from django.views.generic.base import TemplateView
# from django.urls import reverse_lazy
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# from .serializers import *
# from .forms import *
# from .models import *


# # Create your views here.

# class LibraryMainView(TemplateView):
#     template_name = 'library/library_main.html'


# # %% Score
    
# class ScoreListView(ListView):
#     model = Score
#     template_name = 'library/score_list.html'
#     context_object_name = 'scores'


# class ScoreCreateView(CreateView):
#     model = Score
#     form_class = ScoreForm
#     template_name = 'library/score_create.html'
#     success_url = reverse_lazy('score_list')


# class ScoreDeleteView(DeleteView):
#     model = Score
#     template_name = 'library/score_delete_confirm.html'
#     success_url = reverse_lazy('score_list')


# class ScoreUpdateView(UpdateView):
#     model = Score
#     form_class = ScoreForm
#     template_name = 'library/score_update.html'
#     success_url = reverse_lazy('score_list')


# class ScoreDetailView(DetailView):
#     model = Score
#     template_name = 'library/score_detail.html'
#     context_object_name = 'score'


# # %% Sheet

# class SheetListView(ListView):
#     model = Sheet

#     template_name = 'library/sheet_list.html'
#     context_object_name = 'sheets'


# class SheetDeleteView(DeleteView):
#     model = Sheet
#     template_name = 'library/sheet_delete_confirm.html'
#     success_url = reverse_lazy('sheet_list')


# class SheetUpdateView(UpdateView):
#     model = Sheet
#     form_class = SheetForm
#     template_name = 'library/sheet_update.html'
#     success_url = reverse_lazy('sheet_list')


# class SheetDetailView(DetailView):
#     model = Sheet
#     template_name = 'library/sheet_detail.html'
#     context_object_name = 'sheet'


# class SheetCreateView(CreateView):
#     model = Sheet
#     form_class = SheetForm
#     template_name = 'library/sheet_create.html'
#     success_url = reverse_lazy('sheet_list')


# class ScoreSheetListView(ListView):
#     model = Score

#     def get_queryset(self):
#         return Sheet.objects.filter(pk=self.kwargs['pk'])

#     template_name = 'library/score_sheet_list.html'
#     context_object_name = 'sheets'


# # %% Theme

# class ThemeListView(ListView):
#     model = Theme
#     template_name = 'library/theme_list.html'
#     context_object_name = 'themes'


# class ThemeCreateView(CreateView):
#     model = Theme
#     form_class = ThemeForm
#     template_name = 'library/theme_create.html'
#     success_url = reverse_lazy('theme_list')


# class ThemeDetailView(DetailView):
#     model = Theme
#     template_name = 'library/theme_detail.html'
#     context_object_name = 'theme'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['versions'] = Version.objects.filter(theme=self.object)
#         return context
    

# class ThemeDeleteView(DeleteView):
#     model = Theme
#     template_name = 'library/theme_delete_confirm.html'
#     success_url = reverse_lazy('theme_list')


# class ThemeUpdateView(UpdateView):
#     model = Theme
#     form_class = ThemeForm
#     template_name = 'library/theme_update.html'
#     success_url = reverse_lazy('theme_list')

    

# # %% Version


# class VersionListView(ListView):
#     model = Version
#     template_name = 'library/version_list.html'
#     context_object_name = 'versions'


# class VersionCreateView(CreateView):
#     model = Version
#     form_class = VersionForm
#     template_name = 'library/version_create.html'
#     success_url = reverse_lazy('version_list')


# class VersionDetailView(DetailView):
#     model = Version
#     template_name = 'library/version_detail.html'
#     context_object_name = 'version'


# class VersionDeleteView(DeleteView):
#     model = Version
#     template_name = 'library/version_confirm_delete.html'
#     success_url = reverse_lazy('version_list')


# class VersionUpdateView(UpdateView):
#     model = Version
#     form_class = VersionForm
#     template_name = 'library/version_create.html'
#     success_url = reverse_lazy('version_list')


# # %% Exercise

# class ExerciseListView(ListView):
#     model = Exercise
#     template_name = 'library/exercise_list.html'
#     context_object_name = 'exercises'


# class ExerciseCreateView(CreateView):
#         model = Exercise
#         form_class = ExerciseForm
#         template_name = 'library/exercise_create.html'
#         success_url = reverse_lazy('exercise_list')


# class ExerciseDetailView(DetailView):
#     model = Exercise
#     template_name = 'library/exercise_detail.html'
#     context_object_name = 'exercise'


# class ExerciseDeleteView(DeleteView):
#     model = Exercise
#     template_name = 'library/exercise_confirm_delete.html'
#     success_url = reverse_lazy('exercise_list')


# class ExerciseUpdateView(UpdateView):
#     model = Exercise
#     form_class = ExerciseForm
#     template_name = 'library/exercise_create.html'
#     success_url = reverse_lazy('exercise_list')


# # %% Lesson



# class LessonListView(ListView):
#     model = Lesson
#     template_name = 'library/lesson_list.html'
#     context_object_name = 'lessons'


# class LessonCreateView(CreateView):

#     model = Lesson
#     form_class = LessonForm
#     template_name = 'library/lesson_create.html'
#     success_url = reverse_lazy('lesson_list')


# class LessonDetailView(DetailView):
#     model = Lesson
#     template_name = 'library/lesson_detail.html'
#     context_object_name = 'lesson'


# class LessonDeleteView(DeleteView):
#     model = Lesson
#     template_name = 'library/lesson_confirm_delete.html'
#     success_url = reverse_lazy('lesson_list')


# class LessonUpdateView(UpdateView):
#     model = Lesson
#     form_class = LessonForm
#     template_name = 'library/lesson_create.html'
#     success_url = reverse_lazy('lesson_list')



# #%% Book

# class BookListView(ListView):
#     model = Book
#     template_name = 'library/book_list.html'
#     context_object_name = 'books'


# class BookCreateView(CreateView):
#     model = Book
#     form_class = BookForm
#     template_name = 'library/book_create.html'
#     success_url = reverse_lazy('book_list')


# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'library/book_detail.html'
#     context_object_name = 'book'


# class BookDeleteView(DeleteView):
#     model = Book
#     template_name = 'library/book_confirm_delete.html'
#     success_url = reverse_lazy('book_list')


# class BookUpdateView(UpdateView):
#     model = Book
#     form_class = BookForm
#     template_name = 'library/book_create.html'
#     success_url = reverse_lazy('book_list')


    