from django.conf import settings
from django.db import models

class Calendar(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CalendarEntry(models.Model):
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='entries') # 이 부분을 추가합니다.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    day = models.PositiveIntegerField()  # unique 제약 조건을 일단 제거합니다.
    link = models.URLField()
    user_image = models.ImageField(upload_to='user_images/',null=True)

    class Meta:
        unique_together = ['calendar', 'day']  # 한 캘린더 내에서는 동일한 날짜가 중복되지 않도록 설정

    def __str__(self):
        return f"Entry for {self.username} on {self.day} of {self.calendar.name}"
