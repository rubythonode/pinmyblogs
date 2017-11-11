from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from account.views import (loginuser, register)
from content.views import (dashboard, saveinline, send,
                           index, favicon, delete, trashedbin, trashedbin_delete, trashed_empty)
from editing.views import edit, achiveShow
from search.views import search
from start.views import start

urlpatterns=[
    ##########################
    url(r'^start/$', start, name="start"),
    ########################
    # url(r'^__debug__/', include(debug_toolbar.urls)),
    #################

    url(r'^remove/((?P<user_hash>[\w]+){1,8})\b$', delete, name="delete"),
    url(r'^sp_user/', admin.site.urls),
    url(r'^search/$', search, name="search"),

    url(r'^send/$', send, name="send"),
    url(r'bootstrap.min.css.map$', favicon, name="favicon"),

    url(r'^favicon.ico$', favicon, name="favicon"),
    url(r'favicon.ico', favicon, name="favicon"),
    url(r'^favicon.ico/$', favicon, name="favicon"),
    url(r'^edit/((?P<user_hash>[\w]+){1,8})\b$', edit, name="edit"),

    url(r'^category/', include("category.urls", ), name="category"),
    url(r'^setting/', include("settings.urls", ), name="setting"),

    url(r'^login/$', loginuser, name="login", ),
    url(r'^logout$', logout, {'next_page': 'start'}, name="logout", ),
    url(r'^register/$', register, name="register", ),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^archive/$', achiveShow, name="archiveshow"),

    url(r'^trashedbin/$', trashedbin, name="trashedbin"),

    url(r'^restore/((?P<user_hash>[\w]+){1,8})\b$', trashedbin, name="trashedbin_command"),
    url(r'^deleteparam/((?P<user_hash>[\w]+){1,8})', trashedbin_delete, name="trashedbin_delete"),
    url(r'^emptytrash/$', trashed_empty, name="trashedbin_empty"),

    ###############  Base URL for saving the URL ################
    url(r'^$', index, name="index"),

    url(r'^.+$', saveinline, name="saveinline"),
]

handler404=favicon
# handler400 = loginuser
# handler403 = loginuser
# handler500 = loginuser#
