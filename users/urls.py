
from django.urls import path
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from .views import *
from .students_views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register-done/', RegisterDoneView.as_view(), name='register-done'),
    path('reset-password', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# urlpatterns += [
#     path('students/list/', StudentListView.as_view(), name='student_list'),
#     path('student/detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
#     path('student/add/', StudentAddView.as_view(), name='student_add'),
#     path('student/update/<int:pk>/', StudentUpdateView.as_view(), name='student_update'),
#     path('student/delete/<int:pk>/', StudentDeleteView.as_view(), name='student_delete'),
# ]


urlpatterns += [
    path('profile/', ProfileDashboardView.as_view(), name='profile_dashboard'),
    path('profile/edit/', UserEditView.as_view(), name='user_edit'),
    # path('profile/password/', ProfilePasswordUpdateView.as_view(), name='profile_password'),

    # path('dashboard/', DashboardView.as_view(), name='dashboard'),

]

