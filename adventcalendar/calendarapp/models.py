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
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='entries')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    day = models.PositiveIntegerField()
    link = models.URLField()
    user_image = models.ImageField(upload_to='user_images/', null=True)

    class Meta:
        unique_together = ['calendar', 'day']

    @property
    def username(self):
        return self.user.username if self.user else None

    def __str__(self):
        return f"Entry for {self.username} on {self.day} of {self.calendar.name}"
