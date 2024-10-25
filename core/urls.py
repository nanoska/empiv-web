# core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', include('web.urls')),
    path('users/', include('users.urls')),
    # path('eventos/', include('events.urls')),
    # path('talleres/', include('workshops.urls')),
    # path('biblioteca/', include('library.urls')),
    # path('musica/', include('music.urls')),
    # path('tareas/', include('tasks.urls')),
    # path('academia/', include('academy.urls')),
    # path('pagos/', include('payments.urls')),
    # path('tickets/', include('tickets.urls')),
    # path('inbox/', include('inbox.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)