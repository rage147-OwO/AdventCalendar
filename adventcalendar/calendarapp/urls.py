from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.calendar, name='home'),
    path('create-gallery/', views.create_gallery, name='create_gallery'),
    path('create-calendar-entry/', views.create_calendar_entry, name='create_calendar_entry'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
