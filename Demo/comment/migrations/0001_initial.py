# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-23 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogPost', '0008_auto_20181023_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('Comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='BlogPost.Post')),
                ('Comment_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_comment', to='comment.Comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
