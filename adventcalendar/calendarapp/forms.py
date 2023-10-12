from django import forms
from .models import  CalendarEntry, Calendar



class CalendarEntryForm(forms.ModelForm):
    class Meta:
        model = CalendarEntry
        fields = ['day', 'link', 'user_image']



class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name', 'description']
