# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-22 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20181017_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='School',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
