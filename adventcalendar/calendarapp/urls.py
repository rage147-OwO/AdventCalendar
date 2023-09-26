from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('calendar_list/', views.calendar_list, name='calendar_list'),
    path('', views.calendar, name='home'),
    path('login/', views.loginn),
    path('showlist/', views.showlist, name='showlist'),
    path('calendar_intro/', views.calendar_intro, name='calendar_intro'),
    path('calendar-entries/', views.calendar_entry_list, name='calendar_entry_list'),
    path('calendar-entry/<int:entry_id>/', views.calendar_entry_detail, name='calendar_entry_detail'),
    path('create-calendar-entry/', views.create_calendar_entry, name='create_calendar_entry'),
    path('update-calendar-entry/<int:entry_id>/', views.update_calendar_entry, name='update_calendar_entry'),
    path('delete-calendar-entry/<int:entry_id>/', views.delete_calendar_entry, name='delete_calendar_entry'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

