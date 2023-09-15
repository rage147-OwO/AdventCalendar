from django.shortcuts import render
from .models import Post
from django.template import loader





def calendar(request):
    days = [{'day': i} for i in range(1, 32)]

    days[0].update({'person_name': 'rage147', 'person_image_url': 'static/rage147.webp', 'post_link': 'Hi, I am Alice!'})
    # ... (다른 날짜에 대한 데이터 할당)
    return render(request, 'calendar.html', {'days': days})

