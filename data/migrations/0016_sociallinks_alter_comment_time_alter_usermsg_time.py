# Generated by Django 4.2.3 on 2023-07-29 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_project_alter_comment_time_alter_usermsg_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, max_length=1000, null=True)),
                ('github', models.CharField(blank=True, max_length=1000, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=1000, null=True)),
                ('watsapp', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 29, 18, 36, 2, 656287)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 29, 18, 36, 2, 656287)),
        ),
    ]