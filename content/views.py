from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core import validators
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.models import Settings
from content.models import Url
from randomize.generate import send_hash
from scrapy.core import core


@login_required
def dashboard(request):
    title="pinmyblogs|dashboard"
    allUrl=None
    print ()

    if (request.method == "POST" and request.POST['save'] == "save" and request.session.has_key("email")):
        if (request.POST['q'] != ""):
            url=request.POST['q']
            email=request.session["email"]
            check=save(email, url)
            if (check):
                print ("Success")
    return redirect("index")
    # email=request.session["email"]
    # allUrl=showAllUrls(email=email)
    # if (allUrl):
    #     return render(request, 'dashboard.html', {'title': title, "allUrl": allUrl, })
    #
    # return render(request, 'dashboard.html', {'title': title})


def index(request):
    if request.user.is_authenticated():

        title="pinmyblogs|dashboard"
        email=request.session["email"]
        allUrl=showAllUrls(email=email)
        numberintrash=returnUrlTrashed(email=email)

        if (allUrl):

            if (not request.session.has_key("page") or not request.session.has_key("format")):
                # print (request.user.id)
                # page=Settings.objects.get(user_id=request.user.id)

                res=Settings.objects.filter(user_id=request.user.id).values('pagination', 'date_time_format')
                print ("Mydict")
                for r in res:
                    request.session['page']=r.get('pagination')
                    request.session['format']=r.get('date_time_format')
                    print (request.session['format'])
                    # request.session['page']=page.pagination
                    # request.session['format']=page.date_time_format

            page=request.session.get("page", "10")
            paginator=Paginator(allUrl, page)

            try:
                if (request.GET['page']):
                    page=request.GET['page']
                    session_paginator=request.GET['page']
                    allUrl=paginator.page(page)
            except Exception, e:
                print ("Error", e.message)
                allUrl=paginator.page(1)

            return render(request, 'dashboard.html', {'title': title,
                                                      "allUrl": allUrl,
                                                      "numberintrash": numberintrash, })

        return render(request, 'dashboard.html', {'title': title,
                                                  "allUrl": allUrl,
                                                  "numberintrash": numberintrash, })
    return render(request, "start.html")


@login_required
def saveinline(request):
    title="pinmyblogs|dashboard"
    if (request.method == "GET" and request.session.has_key("email")):
        print (request.get_full_path())

        url=request.get_full_path().lstrip('/').lower()
        if (url):

            if (not (str(url).startswith("#")) and (not str(url).startswith("?"))):
                email=request.session["email"]
                check=save(email, url)
                if (check):
                    print ("Success")
                    return redirect("index")
                else:
                    return redirect("index")
            else:
                return redirect("index")
                return HttpResponse("Go to Home Page")
                print("Here is the error")

    if (request.method == "POST" and request.POST['save'] == "save" and request.session.has_key("email")):
        if (request.POST['q'] != ""):
            url=request.POST['q']
            email=request.session["email"]
            check=save(email, url)
            if (check):
                print ("Success")

    email=request.session["email"]
    allUrl=showAllUrls(email=email)

    numberintrash=returnUrlTrashed(email=email)
    if (allUrl):
        return render(request, 'dashboard.html', {'title': title,
                                                  "allUrl": allUrl,
                                                  "numberintrash": numberintrash, })


def send(request):
    return HttpResponse("Please logged in")


def save(email, url):
    a=False
    print (url)
    import re
    exists=re.search('^[a-zA-Z0-9-\w]+\.[a-zA-Z0-9-\w\.]+', url, re.IGNORECASE | re.MULTILINE)

    if exists:
        a=True

    try:

        if a is not True:
            valid=validators.URLValidator()
            valid.__call__(url)
            print ("Good is works")
            a=True
    except validators.ValidationError as e:
        print("Thereis an error ", e.message)

    if a:
        details=core(url)
        url_hash=send_hash(Url, length=8)
        print (url_hash)

        save_content=Url()
        save_content.user_hash=str(url_hash)
        save_content.url=url
        save_content.user_email=email
        save_content.md5hash="md5hash"
        save_content.domain_name=details.get("domain_name")
        save_content.title=details.get("title")
        save_content.save()
        return True
    else:
        return False


def showAllUrls(email=""):
    if (email):
        allUrl=Url.objects.filter(user_email=email, is_blocked=0, is_delete_parmently=0,
                                  is_trashed=0).values('url', 'user_hash', 'date_modified', 'domain_name',
                                                       'title').order_by("-id")

        if (allUrl):
            # for u in allUrl:
            #     print (u.url)
            #     print (u.user_hash)
            #     print (u.category_name)
            #     print (u.title)
            #     print (u.domain_name)
            #     print (u.date_modified)
            return allUrl
        else:
            print ("Nothing")
            return None


@login_required
def edit(request, user_hash=""):
    print (user_hash)
    if (user_hash):
        return HttpResponse("Edit %s" % (user_hash))


def favicon(request):
    return HttpResponse("")


@login_required
def delete(request, user_hash=""):
    print (request)
    if (user_hash):
        try:
            delete=Url.objects.get(user_hash=str(user_hash))

            if (delete):
                delete.is_trashed=1
                delete.save()
                print (user_hash + "for the delete pattern")

        except Exception, e:
            print(e.message)

    return redirect("index")


@login_required
def trashedbin(request, *args, **kwargs):
    title="pinmyblogs|trash"
    email=request.session["email"]

    numberintrash=returnUrlTrashed(email=email)

    if (numberintrash):

        if (kwargs.has_key("user_hash")):
            print(kwargs["user_hash"])
        try:
            changes=Url.objects.get(user_hash=kwargs["user_hash"], user_email=email, is_delete_parmently=0,
                                    is_trashed=1)
            if (changes):
                changes.is_trashed=0
                changes.save()
                return redirect("trashedbin")

        except Exception, e:
            print ("Error ucought", e.message)

        return render(request, 'trash.html', {'title': title,
                                              "allUrl": numberintrash,
                                              "numberintrash": numberintrash, })

    return render(request, 'trash.html', {'title': title,

                                          "numberintrash": numberintrash, })


@login_required
def trashedbin_delete(request, **kwargs):
    if request.session.has_key("email"):
        try:
            email=request.session.get("email")
            changes=Url.objects.get(user_hash=kwargs["user_hash"], user_email=email, is_delete_parmently=0,
                                    is_trashed=1)
            if (changes):
                changes.is_delete_parmently=1
                changes.save()
                return redirect("trashedbin")

        except Exception, e:
            print ("Error ucought", e.message)

    return redirect("trashedbin")

    if (user_hash):
        try:
            delete=Url.objects.get(user_hash=str(user_hash))
            if (delete):
                delete.is_trashed=1
                delete.save()
                print (user_hash + "for the delete pattern")

        except Exception, e:
            print(e.message)

    return redirect("index")


@login_required
def trashedbin_delete(request, *args, **kwargs):
    title="pinmyblogs|trash"
    email=request.session["email"]

    numberintrash=returnUrlTrashed(email=email)

    if (numberintrash):
        print (args)
        print(kwargs)
        if (kwargs.has_key("user_hash")):
            print(kwargs["user_hash"])
        try:
            changes=Url.objects.get(user_hash=kwargs["user_hash"], user_email=email, is_delete_parmently=0,
                                    is_trashed=1)
            if (changes):
                changes.is_delete_parmently=1
                changes.save()
                return redirect("trashedbin")

        except Exception, e:
            print ("Error ucought", e.message)

        return redirect("trashedbin")

    return redirect("trashedbin")


def returnUrlTrashed(email=""):
    if (email):
        try:
            list=['url', "user_hash"]

            number=Url.objects.filter(user_email=email, is_trashed=1, is_delete_parmently=0).values('url', 'user_hash',
                                                                                                    'title')


        except  Exception, e:
            print (e.message)
    if (number):
        return number


@login_required
def trashed_empty(request):
    print ("reached")
    try:
        if (request.session.has_key("email")):
            email=request.session["email"]
            print ("Email is ", email)
            number=Url.objects.filter(user_email=email, is_trashed=1, is_delete_parmently=0)
            for n in number:
                n.is_delete_parmently=1;
                n.save()
                print ("Deleted")
    except  Exception, e:
        print (e.message)
    return redirect("index")
