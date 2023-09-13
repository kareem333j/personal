# Generated by Django 4.2.3 on 2023-07-15 12:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_usermsg_alter_comment_time_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermsg',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserMsg', to='data.profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 15, 47, 49, 795127)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 15, 15, 47, 49, 795127)),
        ),
    ]