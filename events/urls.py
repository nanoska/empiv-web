# events/urls.py

from .views import *
from django.urls import path


urlpatterns = [    
    path('list/', EventListView.as_view(), name='events'),
    path('evento/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('evento/create/', EventCreateView.as_view(), name='event_create'),
    path('evento/update/<int:pk>/', EventUpdateView.as_view(), name='event_update'),
    path('evento/delete/<int:pk>/', EventDeleteView.as_view(), name='event_delete'),
    # path('evento/<int:pk>/reservar-lugar/', EventReservationView.as_view(), name='event_reservation'),
    
    path('locaciones/', LocationListView.as_view(), name='location_list'),
    path('locacion/<int:pk>/', LocationDetailView.as_view(), name='location_detail'),
    path('locacion/create/', LocationCreateView.as_view(), name='location_create'),

]
