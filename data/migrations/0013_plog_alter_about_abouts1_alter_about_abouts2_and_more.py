# Generated by Django 4.2.3 on 2023-07-19 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_about_aboutskills_alter_about_abouts1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(blank=True, default='Logo', max_length=100, null=True)),
                ('plogName', models.CharField(blank=True, default='Plog_Name', max_length=100, null=True)),
                ('plogImg', models.ImageField(upload_to='', verbose_name=models.ImageField(blank=True, default='default/user3.png', null=True, upload_to='images/PlogImg/%y/%m/%d'))),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutS1',
            field=models.TextField(blank=True, default='Section_1', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutS2',
            field=models.TextField(blank=True, default='Section_2', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutS3',
            field=models.TextField(blank=True, default='Section_3', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutS4',
            field=models.TextField(blank=True, default='Section_4', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='aboutSkills',
            field=models.TextField(blank=True, default='Skills', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 17, 18, 35, 176641)),
        ),
        migrations.AlterField(
            model_name='usermsg',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 19, 17, 18, 35, 176641)),
        ),
    ]