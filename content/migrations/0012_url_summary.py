# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-25 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20170622_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]