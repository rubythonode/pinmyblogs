# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20170619_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='date_modified',
            field=models.DateField(),
        ),
    ]
