from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from content.models import Url
from content.views import returnUrlTrashed


@login_required
def search(request, **kwargs):
    title="pinmyblogs|search"

    if (request.session.has_key("email") and request.method == "GET"):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)
        count=None
        serch=None

        if ("search" in request.GET and len(request.GET['search']) > 0):
            string=request.GET['search']

            print (string)
            serch=Url.objects.filter(user_email=email, url__icontains=string, is_blocked=0, is_delete_parmently=0,
                                     is_trashed=0, ).values("url")

            count=len(serch)
            print (count)

            print (serch)
    return render(request, "search.html", {"title": title,
                                           "numberintrash": numberintrash,
                                           "search": serch,
                                           "count": count
                                           })
