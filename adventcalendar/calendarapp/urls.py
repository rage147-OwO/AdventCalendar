from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='home'),
     path('create-gallery/', views.create_gallery, name='create_gallery'),
    path('create-calendar-entry/', views.create_calendar_entry, name='create_calendar_entry'),
]
