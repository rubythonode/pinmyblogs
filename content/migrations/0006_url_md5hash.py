# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-17 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20170614_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='md5hash',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
