# Generated by Django 4.2.2 on 2023-06-23 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeTable', '0007_timetable_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='week',
            field=models.IntegerField(),
        ),
    ]
