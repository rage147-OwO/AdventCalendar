from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.calendar, name='home'),
    path('create-gallery/', views.create_gallery, name='create_gallery'),
    path('showlist/', views.showlist, name='showlist'),

    path('calendar-entries/', views.calendar_entry_list, name='calendar_entry_list'),
    path('calendar-entry/<int:entry_id>/', views.calendar_entry_detail, name='calendar_entry_detail'),
    path('create-calendar-entry/', views.create_calendar_entry, name='create_calendar_entry'),
    path('update-calendar-entry/<int:entry_id>/', views.update_calendar_entry, name='update_calendar_entry'),
    path('delete-calendar-entry/<int:entry_id>/', views.delete_calendar_entry, name='delete_calendar_entry'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

