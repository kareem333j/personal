# Generated by Django 4.2.3 on 2023-08-12 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0026_project_boots_project_bostg_project_css_project_dj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 19, 29, 57, 52257)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 12, 19, 29, 57, 53257)),
        ),
    ]