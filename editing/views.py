from __future__ import print_function
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from content.models import Url, Category
from content.views import returnUrlTrashed


@login_required
def edit(request, **kwargs):
    title="pinmyblogs|edit"
    q=None

    if (request.method == 'GET' and request.session.has_key("email")):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)

        if (kwargs.has_key('user_hash')):

            user_hash=kwargs['user_hash']

            categorylist=None
            try:
                q=Url.objects.get(user_hash=user_hash, user_email=email, is_blocked=0,
                                  is_delete_parmently=0)
                categorylist=Category.objects.filter(created_by=email, is_blocked=0).values("category_name")
                print(categorylist.query)

                print(categorylist)
            except Exception, e:
                print("Exception caught ")

            return render(request, "edit.html", {

                "title": title,
                "edit": q,
                "message": "success",
                "categorylist": categorylist,
                "numberintrash": numberintrash,

            })

        return render(request, "edit.html", {

            "title": title,
            "edit": q,
            "message": "success",
            "numberintrash": numberintrash,

        })
    if (request.method == 'POST' and request.session.has_key("email")):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)
        message=None
        user_hash=None
        url_title=None
        is_archived=None
        summary=None
        c_name=None
        if "hash" in request.POST:
            user_hash=request.POST['hash']
        try:
            q=Url.objects.get(user_hash=user_hash, user_email=email, is_delete_parmently=0, is_blocked=0)
            url_title=q.user_hash
            is_archived=q.is_arhived
            c_name=q.category_name

            summaryp=q.summaryp

        except:
            pass

        if "title" in request.POST:
            url_title=request.POST['title']
        if "archive" in request.POST:

            is_archived=1
        else:
            is_archived=0
        if "c_name" in request.POST:
            c_name=(request.POST['c_name'])
            c_name=str(c_name).lower()
            print(c_name)
        if "summary" in request.POST:
            summaryp=request.POST['summary']

        try:

            q.category_name=c_name
            q.title=url_title
            q.is_arhived=is_archived
            q.summaryp=summaryp
            q.save()


        except Exception, e:
            print("Exception caught " + e.message)

        return render(request, "edit.html", {

            "title": title,
            "message": message,
            "messagetype": "success",
            "numberintrash": numberintrash,
        })


@login_required
def achiveShow(request):
    title="pinmyblogs|archive"
    q=""
    count=None
    if (request.method == 'GET' and request.session.has_key("email")):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)
        try:
            q=Url.objects.filter(user_email=email, is_blocked=0, is_arhived=1, is_trashed=0,
                                 is_delete_parmently=0).values('url')

            count=q.count()

        except  Exception, e:
            print("What is the error", e.message)

    return render(request, "archive.html", {"title": title,
                                            "numberintrash": numberintrash,
                                            "q": q,
                                            "count": count
                                            })
