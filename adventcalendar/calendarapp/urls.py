from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('calendar_list/', views.calendar_list, name='calendar_list'),
    path('', views.index, name='home'),
    path('login/', views.loginn),
    path('calendar_intro/', views.calendar_intro, name='calendar_intro'),

    # calendar_entry patterns nested under calendar
    path('calendar/<int:calendar_id>/entries/', views.calendar_entry_list, name='calendar_entry_list'),
    path('calendar/<int:calendar_id>/entry/<int:day>/', views.calendar_entry_detail, name='calendar_entry_detail'),
    path('calendar/<int:calendar_id>/create-entry/', views.create_calendar_entry, name='create_calendar_entry'),
    path('calendar/<int:calendar_id>/entry/<int:day>/edit/', views.update_calendar_entry, name='update_calendar_entry'),
    path('calendar/<int:calendar_id>/entry/<int:day>/delete/', views.delete_calendar_entry, name='delete_calendar_entry'),

    # calendar patterns
    path('create_calendar/', views.create_calendar, name='create_calendar'),
    path('calendar/<int:calendar_id>/', views.calendar, name='calendar_detail'),
    path('calendar/<int:calendar_id>/edit/', views.update_calendar, name='update_calendar'),
    path('calendar/<int:calendar_id>/delete/', views.delete_calendar, name='delete_calendar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

