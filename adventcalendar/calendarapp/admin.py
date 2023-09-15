from django.contrib import admin
from .models import Gallery, GalleryImage, CalendarEntry
# Register your models here.

admin.site.register(Gallery)
admin.site.register(GalleryImage)
admin.site.register(CalendarEntry)
