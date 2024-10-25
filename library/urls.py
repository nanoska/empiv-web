# from django.urls import path
# from .views import *


# urlpatterns = [
#     path('', LibraryMainView.as_view(), name='library_main'),
# ]

# urlpatterns += [
#     path('libros/', BookListView.as_view(), name='book_list'),
#     path('libros/create/', BookCreateView.as_view(), name='book_create'),
#     path('libros/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
#     path('libros/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
#     path('libros/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
# ]


# urlpatterns += [
#     path('versiones/', VersionListView.as_view(), name='version_list'),
#     path('versiones/create/', VersionCreateView.as_view(), name='version_create'),
#     path('versiones/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
#     path('versiones/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
#     path('versiones/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
# ]


# urlpatterns += [
#     path('lecciones/', LessonListView.as_view(), name='lesson_list'),
#     path('lecciones/create/', LessonCreateView.as_view(), name='lesson_create'),
#     path('lecciones/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
#     path('lecciones/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
#     path('lecciones/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson_update'),
# ]


# urlpatterns += [
#     path('ejercicios/', ExerciseListView.as_view(), name='exercise_list'),
#     path('ejercicios/create/', ExerciseCreateView.as_view(), name='exercise_create'),
#     path('ejercicios/<int:pk>/', ExerciseDetailView.as_view(), name='exercise_detail'),
#     path('ejercicios/<int:pk>/delete/', ExerciseDeleteView.as_view(), name='exercise_delete'),
#     path('ejercicios/<int:pk>/update/', ExerciseUpdateView.as_view(), name='exercise_update'),
# ]

# urlpatterns += [
#     path('temas/', ThemeListView.as_view(), name='theme_list'),
#     path('temas/create/', ThemeCreateView.as_view(), name='theme_create'),
#     path('temas/<int:pk>/', ThemeDetailView.as_view(), name='theme_detail'),
#     path('temas/<int:pk>/delete/', ThemeDeleteView.as_view(), name='theme_delete'),
#     path('temas/<int:pk>/update/', ThemeUpdateView.as_view(), name='theme_update'),
# ]



# urlpatterns += [
#     path('partituras/scores/', ScoreListView.as_view(), name='score_list'),
#     path('partituras/scores/create/', ScoreCreateView.as_view(), name='score_create'),
#     path('partituras/scores/<int:pk>/', ScoreDetailView.as_view(), name='score_detail'),
#     path('partituras/scores/<int:pk>/delete/', ScoreDeleteView.as_view(), name='score_delete'),
#     path('partituras/scores/<int:pk>/update/', ScoreUpdateView.as_view(), name='score_update'),
#     path('partituras/score/<int:pk>/sheets/', ScoreSheetListView.as_view(), name='score_sheet_list'),
# ]

# urlpatterns += [
#     path('partituras/sheets/', SheetListView.as_view(), name='sheet_list'),
#     path('partituras/sheets/create/', SheetCreateView.as_view(), name='sheet_create'),
#     path('partituras/sheets/<int:pk>/', SheetDetailView.as_view(), name='sheet_detail'),
#     path('partituras/sheets/<int:pk>/delete/', SheetDeleteView.as_view(), name='sheet_delete'),
#     path('partituras/sheets/<int:pk>/update/', SheetUpdateView.as_view(), name='sheet_update'),
# ]
