# web/urls.py

from .views import *
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    
    # path('contacto/', ContactView.as_view(), name='contact'),
    path('under-construction/', UnderConstructionView.as_view(), name='under_construction'),
    # path('clases-particulares/', SingleLessonsView.as_view(), name='single_lessons'),
    path('sobre-nosotros/', AboutUsView.as_view(), name='about_us'),
]
