# Generated by Django 4.2.3 on 2023-07-19 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_plog_alter_about_abouts1_alter_about_abouts2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plog',
            name='plogImg',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 17, 26, 56, 605807)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 17, 26, 56, 605807)),
        ),
    ]