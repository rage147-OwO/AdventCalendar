from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GalleryForm, GalleryImageFormSet, CalendarEntryForm
from .models import Gallery, GalleryImage, CalendarEntry

def calendar(request):
    days = [{'day': i} for i in range(1, 32)]

    days[0].update({'person_name': 'rage147', 'person_image_url': 'static/rage147.webp', 'post_link': 'Hi, I am Alice!'})
    # ... (다른 날짜에 대한 데이터 할당)
    return render(request, 'calendar.html', {'days': days})


def create_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        formset = GalleryImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            gallery = form.save()
            formset.instance = gallery
            formset.save()
            return redirect('gallery_detail', gallery.id)
    else:
        form = GalleryForm()
        formset = GalleryImageFormSet(queryset=GalleryImage.objects.none())

    return render(request, 'create_gallery.html', {'form': form, 'formset': formset})

def create_calendar_entry(request):
    if request.method == 'POST':
        form = CalendarEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_entry_list')
    else:
        form = CalendarEntryForm()
    
    return render(request, 'create_calendar_entry.html', {'form': form})
