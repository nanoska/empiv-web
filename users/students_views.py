# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.shortcuts import get_object_or_404, redirect
# from django.urls import reverse_lazy
# from django.contrib import messages
# from django.db import IntegrityError, transaction
# from django.utils.html import format_html
# from .models import Student
# from .forms import StudentForm

# class StudentListView(ListView):
#     model = Student
#     template_name = 'students/student_list.html'
#     context_object_name = 'students'


# class StudentDetailView(DetailView):
#     model = Student
#     template_name = 'students/student_detail.html'
#     context_object_name = 'student'

# class StudentAddView(CreateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'students/student_add.html'
#     success_url = reverse_lazy('student_list')

#     def form_valid(self, form):
#         student = form.save(commit=False)
#         student.save()
#         user = student.user
#         user.is_student = True
#         user.is_normal = False
#         user.save()
#         messages.success(self.request, f'Estudiante {user.username} agregado con éxito.')
#         return super().form_valid(form)

# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = 'students/student_update.html'
#     context_object_name = 'student'
#     success_url = reverse_lazy('student_list')

#     def form_valid(self, form):
#         student = form.save(commit=False)
#         try:
#             with transaction.atomic():
#                 student.save()
#                 form.save_m2m()  # Guarda las relaciones ManyToMany
#                 user = student.user
#                 success_message = format_html(
#                     'Estudiante {} actualizado exitosamente. <a href="{}">Volver a la lista de alumnos</a>',
#                     user.username,
#                     reverse_lazy('student_list')
#                 )
#                 messages.success(self.request, success_message)
#         except IntegrityError as e:
#             form.add_error(None, f'Error al guardar los datos: {e}')
#             return self.form_invalid(form)
#         return super().form_valid(form)

# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name = 'staffUser/students/student_delete_confirm.html'
#     context_object_name = 'student'
#     success_url = reverse_lazy('student_list')

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         user = self.object.user
#         user.is_student = False
#         user.is_normal = True
#         user.save()
#         messages.success(request, f'Estudiante {user.username} eliminado con éxito.')
#         return super().delete(request, *args, **kwargs)
