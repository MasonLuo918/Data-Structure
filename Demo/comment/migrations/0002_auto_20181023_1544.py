# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-23 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='Comment_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comment', to='comment.Comments'),
        ),
    ]