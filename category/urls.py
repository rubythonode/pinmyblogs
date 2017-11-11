from django.conf.urls import *

from category.views import category, showcategorylistwise

urlpatterns=[
    url(r'^show/$', category, name="categoryshow"),
    url(r'^show/category/$', showcategorylistwise, name="categoryshowlist")
]
