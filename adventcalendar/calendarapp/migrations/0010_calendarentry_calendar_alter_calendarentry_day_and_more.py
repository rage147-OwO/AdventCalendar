# Generated by Django 4.2.5 on 2023-09-27 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0009_calendar_remove_galleryimage_gallery_delete_gallery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarentry',
            name='calendar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='calendarapp.calendar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendarentry',
            name='day',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='calendarentry',
            unique_together={('calendar', 'day')},
        ),
    ]