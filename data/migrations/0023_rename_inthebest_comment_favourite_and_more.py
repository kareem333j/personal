# Generated by Django 4.2.3 on 2023-08-09 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_comment_inthebest_alter_comment_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='inTheBest',
            new_name='favourite',
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 15, 57, 27, 159846)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 9, 15, 57, 27, 159846)),
        ),
    ]