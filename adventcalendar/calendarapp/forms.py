from django import forms
from .models import Gallery, GalleryImage, CalendarEntry

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['username']

GalleryImageFormSet = forms.inlineformset_factory(Gallery, GalleryImage, fields=('image',), extra=1, max_num=5,can_delete=False)


class CalendarEntryForm(forms.ModelForm):
    class Meta:
        model = CalendarEntry
        fields = ['username', 'day', 'link', 'user_image']

