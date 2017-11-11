from django.conf.urls import url

from settings.views import home, paginations, remove_category, download, format_date

base64_pattern=r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?'

urlpatterns=[

    url(r'^home/$', home, name="setting_home"),
    url(r'^pagination/((?P<page>[\d]+))/$', paginations, name="setting_pagination"),
    url(r'^category/remove/' + '(?P<base64string>{})/$'.format(base64_pattern), remove_category,
        name="setting_category_remove"),

    url(r'^download/' + '(?P<base64string>{})/$'.format(base64_pattern), download,
        name="setting_download"),
    url(r'^format/' + '(?P<base64string>{})/$'.format(base64_pattern), format_date,
        name="setting_format"),

]
