# Generated by Django 4.2.5 on 2023-09-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0005_alter_calendarentry_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarentry',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]