from django import forms
from .models import  CalendarEntry



class CalendarEntryForm(forms.ModelForm):
    class Meta:
        model = CalendarEntry
        fields = ['username', 'day', 'link', 'user_image']

