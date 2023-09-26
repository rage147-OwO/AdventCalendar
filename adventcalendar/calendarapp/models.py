from django.db import models
from django.conf import settings



class CalendarEntry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    day = models.PositiveIntegerField(unique=True)
    link = models.URLField()
    user_image = models.ImageField(upload_to='user_images/',null=True)

    def __str__(self):
        return f"Entry for {self.username} on {self.day}"

class Calendar(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name