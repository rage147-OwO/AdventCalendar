from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GalleryForm, GalleryImageFormSet, CalendarEntryForm
from .models import Gallery, GalleryImage, CalendarEntry


def calendar(request):
    days = [{'day': i, 'person_name': None, 'person_image_url': None, 'link': None} for i in range(1, 32)]

    calendar_entries = CalendarEntry.objects.all()

    for entry in calendar_entries:
        if 0 < entry.day <= 31:
            days[entry.day - 1].update({
                'person_name': entry.username,
                'person_image_url': entry.user_image.url if entry.user_image else None,
                'link': entry.link
            })

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
        form = CalendarEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry, created = CalendarEntry.objects.update_or_create(
                username=form.cleaned_data['username'],
                defaults={
                    'day': form.cleaned_data['day'],
                    'link': form.cleaned_data['link'],
                    'user_image': form.cleaned_data['user_image']
                }
            )
            return redirect('calendar_entry_list')
    else:
        form = CalendarEntryForm()

    return render(request, 'create_calendar_entry.html', {'form': form})



