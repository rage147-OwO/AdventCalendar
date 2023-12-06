from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from .forms import  CalendarEntryForm, CalendarForm
from .models import CalendarEntry, Calendar
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse

def index(request):
    if 'show_mine' in request.GET and request.user.is_authenticated:
        calendars = Calendar.objects.filter(creator=request.user)
    else:
        calendars = Calendar.objects.all()
    return render(request, 'index.html', {'calendars': calendars})



def calendar_list(request):
    calendars = Calendar.objects.all()
    return render(request, 'calendar_list.html', {'calendars': calendars})


@login_required
def create_calendar(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST)
        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.creator = request.user
            calendar.save()
            return redirect(index)
    else:
        form = CalendarForm()

    return render(request, 'create_calendar.html', {'form': form})

@login_required
def calendar_detail(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)
    return render(request, 'calendar_detail.html', {'calendar': calendar})

@login_required
def update_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id, creator=request.user)

    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = CalendarForm(instance=calendar)

    return render(request, 'update_calendar.html', {'form': form, 'calendar': calendar})

@login_required
def delete_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id, creator=request.user)

    if request.method == 'POST':
        calendar.delete()
        return redirect(index)

    return render(request, 'delete_calendar.html', {'calendar': calendar})















def calendar(request, calendar_id):
    # 해당 ID의 Calendar를 가져옴
    calendar_obj = get_object_or_404(Calendar, id=calendar_id)
    
    days = [{'day': i, 'person_name': None, 'person_image_url': None, 'link': None} for i in range(1, 26)]
    entries = CalendarEntry.objects.filter(calendar=calendar_id).order_by('day')  
    
    # 해당 Calendar와 연결된 CalendarEntry 항목만 가져옴
    calendar_entries = CalendarEntry.objects.filter(calendar=calendar_obj)

    for entry in calendar_entries:
        if 0 < entry.day <= 31:
            days[entry.day - 1].update({
                'person_name': entry.user,
                'person_image_url': entry.user_image.url if entry.user_image else None,
                'link': entry.link
            })

    return render(request, 'calendar.html', {
        'entries' : entries,
        'days': days, 
        'calendar': calendar_obj, 
        'calendar_id': calendar_id  # 여기에 calendar_id 추가
    }) 



def loginn(request):
    return render(request, 'login.html')

def calendar_intro(request):
    return render(request, 'calendar_intro.html')



@login_required
def create_calendar_entry(request, calendar_id): 
    calendar = Calendar.objects.get(pk=calendar_id)
    if request.method == 'POST':
        form = CalendarEntryForm(request.POST, request.FILES)
        if form.is_valid():
            day = form.cleaned_data['day']
            if CalendarEntry.objects.filter(calendar=calendar, day=day).exists():
                form.add_error('day', 'An entry for this day already exists for this calendar.')
            else:
                entry = form.save(commit=False)
                entry.user = request.user  
                entry.calendar = calendar
                entry.save()
                request.session['recent_calendar_id'] = calendar.id 
                return redirect('calendar_detail', calendar_id=calendar_id)
    else:
        form = CalendarEntryForm()

    return render(request, 'create_calendar_entry.html', {'form': form, 'calendar_id': calendar_id})






@login_required
def calendar_entry_list(request, calendar_id):  
    entries = CalendarEntry.objects.filter(user=request.user, calendar=calendar_id).order_by('day')  
    return render(request, 'calendar_entry_list.html', {'entries': entries, 'calendar_id': calendar_id}) 



@login_required
def calendar_entry_detail(request, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id, user=request.user)
    return render(request, 'calendar_entry_detail.html', {'entry': entry})

@login_required
def update_calendar_entry(request, calendar_id, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        form = CalendarEntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('calendar_entry_detail', calendar_id=calendar_id, entry_id=entry_id)
    else:
        form = CalendarEntryForm(instance=entry)

    return render(request, 'update_calendar_entry.html', {'form': form, 'entry': entry})

@login_required
def delete_calendar_entry(request,calendar_id, entry_id):
    entry = get_object_or_404(CalendarEntry, id=entry_id, user=request.user)

    if request.method == 'POST':
        entry.delete()
        return redirect('calendar_entry_detail', calendar_id=calendar_id, entry_id=entry_id)
    return render(request, 'delete_calendar_entry.html', {'entry': entry, 'calendar_id': entry.calendar.id})


