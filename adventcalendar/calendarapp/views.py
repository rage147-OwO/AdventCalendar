from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .forms import GalleryForm, GalleryImageFormSet, CalendarEntryForm
from .models import Gallery, GalleryImage, CalendarEntry
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


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


        
@login_required
def create_calendar_entry(request):
    if request.method == 'POST':
        form = CalendarEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user  # 현재 로그인한 사용자를 항목의 작성자로 설정합니다.
            entry.save()
            return redirect('home')
    else:   
        form = CalendarEntryForm()

    return render(request, 'create_calendar_entry.html', {'form': form})

@login_required
def update_calendar_entry(request, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id)

    # 현재 사용자가 항목의 작성자가 아니면 접근을 차단합니다.
    if entry.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this entry.")

    if request.method == 'POST':
        form = CalendarEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CalendarEntryForm(instance=entry)

    return render(request, 'update_calendar_entry.html', {'form': form})



