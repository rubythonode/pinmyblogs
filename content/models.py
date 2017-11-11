from __future__ import unicode_literals

from django.db import models


class Url(models.Model):
    user_hash=models.CharField(max_length=50, unique=True, null=False, )
    md5hash=models.CharField(max_length=50, null=True, )
    url=models.TextField(null=False)
    user_email=models.CharField(max_length=50, null=False, )

    ##########################################################################
    date_created=models.DateTimeField(auto_now=True)
    date_modified=models.DateTimeField(auto_now_add=True)
    ####################url- meta - data - and settings############################
    is_blocked=models.IntegerField(default=0, null=False, )
    is_trashed=models.IntegerField(default=0, null=False, )
    is_delete_parmently=models.IntegerField(default=0, null=False, )
    ####################### another meta data ########################
    is_static=models.IntegerField(default=0, null=False, )
    is_favorite=models.IntegerField(default=0, null=False, )
    is_arhived=models.IntegerField(default=0, null=False, )
    category_name=models.CharField(max_length=300, null=False, default="not_defined")
    domain_name=models.CharField(max_length=300, null=False, default="not_defined")
    title=models.CharField(max_length=300, null=False, default="not_defined")
    request_status=models.IntegerField(default=200, null=False)
    summaryp=models.TextField(null=True, default="Not_Defined")


class Category(models.Model):
    category_name=models.CharField(max_length=300, null=False, blank=True)
    created_by=models.CharField(max_length=300, null=False, blank=False)
    is_blocked=models.IntegerField(default=0, null=False)
    category_date_created=models.DateField(auto_now=True)
