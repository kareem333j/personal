# Generated by Django 4.2.3 on 2023-07-15 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_rename_name_profile_name_f_profile_name_l_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermsg',
            name='name',
        ),
        migrations.AddField(
            model_name='usermsg',
            name='name_f',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='usermsg',
            name='name_l',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 16, 43, 59, 379652)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 16, 43, 59, 380652)),
        ),
    ]
