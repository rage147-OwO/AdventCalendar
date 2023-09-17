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
            entry.user = request.user
            entry.save()
            return redirect('calendar_entry_list')
    else:
        form = CalendarEntryForm()

    return render(request, 'create_calendar_entry.html', {'form': form})

@login_required
def calendar_entry_list(request):
    # 사용자와 관련된 CalendarEntry 항목만 필터링하고 Day 순으로 정렬
    entries = CalendarEntry.objects.filter(user=request.user).order_by('day')
    return render(request, 'calendar_entry_list.html', {'entries': entries})

@login_required
def calendar_entry_detail(request, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id, user=request.user)
    return render(request, 'calendar_entry_detail.html', {'entry': entry})

@login_required
def update_calendar_entry(request, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        form = CalendarEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('calendar_entry_list')
    else:
        form = CalendarEntryForm(instance=entry)

    return render(request, 'update_calendar_entry.html', {'form': form, 'entry': entry})  # 'entry' 객체를 템플릿에 전달


@login_required
def delete_calendar_entry(request, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        entry.delete()
        return redirect('calendar_entry_list')

    return render(request, 'delete_calendar_entry.html', {'entry': entry})


@login_required
def showlist(request):
    days = [{'day': i, 'person_name': None, 'person_image_url': None, 'link': None} for i in range(1, 32)]
    calendar_entries = CalendarEntry.objects.all()
    for entry in calendar_entries:
        if 0 < entry.day <= 31:
            days[entry.day - 1].update({
                'person_name': entry.username,
                'person_image_url': entry.user_image.url if entry.user_image else None,
                'link': entry.link
            })

    return render(request, 'showlist.html', {'days': days})