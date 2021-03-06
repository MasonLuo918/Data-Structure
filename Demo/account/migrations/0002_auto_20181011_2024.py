# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-10-11 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('send_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Schoolid',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
