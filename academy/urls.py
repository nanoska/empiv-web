
from django.urls import path
from .views import *

urlpatterns = [
    path('talleres/list/', WorkshopListView.as_view(), name='workshop_list'),
    # path('mis-talleres/', MyWorkshopListView.as_view(), name='my_workshop_list'),
    path('taller/create/', WorkshopCreateView.as_view(), name='workshop_create'),
    path('taller/<int:pk>/', WorkshopDetailView.as_view(), name='workshop_detail'),
    path('taller/update/<int:pk>/', WorkshopUpdateView.as_view(), name='workshop_update'),
    path('taller/delete/<int:pk>/', WorkshopDeleteView.as_view(), name='workshop_delete'),
]

urlpatterns += [
    path('clases-particulares/', SingleLessonsListView.as_view(), name='single_lesson_list'),
    path('clases-particulares/create/', SingleLessonCreateView.as_view(), name='single_lesson_create'),
    path('clases-particulares/<int:pk>/', SingleLessonDetailView.as_view(), name='single_lesson_detail'),
    path('clases-particulares/update/<int:pk>/', SingleLessonUpdateView.as_view(), name='single_lesson_update'),
    path('clases-particulares/delete/<int:pk>/', SingleLessonDeleteView.as_view(), name='single_lesson_delete'),
]

# urlpatterns += [
#     # path('taller/<int:pk>/inscripciones/', EnrollmentView.as_view(), name='enrollment'),
#     # path('talleres/disponibles/', AvailableWorkshopsListView.as_view(), name='available_workshops'),
# ]


# urlpatterns += [
#     path('repertorios/', RepertoireListView.as_view(), name='repertoire_list'),
#     path('repertorios/create/', RepertoireCreateView.as_view(), name='repertoire_create'),
#     path('repertorios/<int:pk>/update/', RepertoireUpdateView.as_view(), name='repertoire_update'),
#     path('repertorios/<int:pk>/delete/', RepertoireDeleteView.as_view(), name='repertoire_delete'),
# ]

