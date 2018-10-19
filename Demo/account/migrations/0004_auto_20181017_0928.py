# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-17 01:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20181012_0008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='RealName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='Schoolid',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='college',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='update_time',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='HeadImage',
            field=models.ImageField(blank=True, upload_to='Image/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='WeCheat',
            field=models.ImageField(blank=True, upload_to='WeCheat/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='motto',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='College',
        ),
    ]
