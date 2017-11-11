# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

from randomize.generate import send_hash


class SettingManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main=super(SettingManager, self).all(*args, **kwargs)
        qs=qs_main.filter(act=True)
        return qs


class Settings(models.Model):
    user=models.OneToOneField(User, unique=True)
    user_hash=models.CharField(max_length=10, blank=False, null=False)
    active=models.BooleanField(default=True)
    pagination=models.IntegerField(default=10)
    date_time_format=models.CharField(max_length=10, default="relative")


    # objects=SettingManager()


def created_profile(sender, **kwargs):
    if (kwargs['created']):
        q=Settings
        hashForUuser=send_hash(q)
        user_profile=Settings(user=kwargs['instance'], user_hash=hashForUuser)
        user_profile.save()


post_save.connect(created_profile, sender=User)
