# Generated by Django 4.2.4 on 2023-08-19 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_comment_time_alter_usermsg_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 18, 36, 52, 515113)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 19, 18, 36, 52, 515113)),
        ),
    ]