from __future__ import unicode_literals

from django.db import models

from content.models import Category


class CategoryList(models.Model):
    name=models.CharField(max_length=300, null=False, blank=True)

    is_blocked=models.IntegerField(default=0, null=False)

# def create_entry_in_category(sender, **kwargs):
#     if (kwargs.has_key("created")):
#         email=request.settings['email']
#         print (kwargs['instance'])
#         Category.objects.create(created_by=email, is_blocked=0, category_name=kwargs['instance'])
#
#
# post_save.connect(create_entry_in_category, sender=CategoryList)
