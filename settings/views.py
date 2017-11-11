import base64

from django.contrib.auth.decorators import login_required
from  django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from account.models import Settings
from category.views import Category
from content.models import Url
from content.views import returnUrlTrashed


@login_required()
def home(request):
    title="pinmyblogs|settings"
    if (request.session.has_key("email") and request.method == "GET"):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)
        q=""
        try:
            q=Category.objects.filter(created_by=email, is_blocked=0, ).values(("category_name"))
        except Exception, e:
            print  ("Here is the error ", e.message)

        return render(request, "setting.html", {"title": title,
                                                "numberintrash": numberintrash,
                                                "q": q
                                                })
    if (request.session.has_key("email") and request.method == "POST"):

        if ("oldpassword" in request.POST) and ("newpassword" in request.POST) and ("newpasswordagain" in request.POST):
            print ("Yes all the values are present")
            # print (request.POST)
            changed=False
            email=request.session.get("email")
            a=password_changing(request, email=email)
            if a:
                print("passwd changed")
                changed=True

        numberintrash=returnUrlTrashed(email=email)
        q=""
        try:
            q=Category.objects.filter(created_by=email, is_blocked=0, ).values(("category_name"))
        except Exception, e:
            print  ("Here is the error ", e.message)

        return render(request, "setting.html", {"title": title,
                                                "numberintrash": numberintrash,
                                                "q": q,
                                                "changed": changed
                                                })


@login_required
def password_changing(request, email=""):
    print (request.POST)
    old_password=request.POST['oldpassword']
    newpassword=request.POST['newpassword']
    newpasswordagain=request.POST['newpasswordagain']

    print (len(str(old_password)))

    if (len(str(old_password)) >= 6) and (len(str(newpassword)) >= 6) and (len(str(newpasswordagain)) >= 6):
        print ("reached")
        if newpassword == newpasswordagain and newpassword != old_password and old_password != newpasswordagain:
            print ("reached inner")
            email=email
            user=User.objects.get(email=email)
            check_password=user.check_password(raw_password=old_password)
            if check_password:
                print ("before")
                change_passed=User.objects.get(email=email)
                change_passed.set_password(newpasswordagain)
                change_passed.save()
                print ("yes password changed")
                return True
            else:
                return False

    return False

    # #############################


@login_required
def paginations(request, **kwargs):
    print (kwargs)
    if kwargs.has_key("page"):
        page=str(kwargs.get('page'))
        r=[10, 20, 40, 60]
        if (page.isdigit()) and (int(page) in r):
            s=Settings.objects.get(user_id=request.user.id)
            s.pagination=page
            s.save()
            request.session['page']=page
            print ("yes")
            pass

    return HttpResponse("")


##########################

@login_required
def remove_category(request, **kwargs):
    print (kwargs)
    if kwargs.has_key("base64string"):
        print (kwargs['base64string'])
        name=base64.b64decode((kwargs.get('base64string')))
        name=str(name).strip().lower()
        email=request.session['email']
        list=Category.objects.filter(created_by=email, is_blocked=0, )

        a=[str(i.category_name) for i in list]
        print (a)
        print (name + ":This is name")
        if (name in a):
            try:
                list=list.get(created_by=email, category_name=name)
                if list:
                    print (list.category_name)
                    print ("The category " + name + " is present")

                    an=None
                    an=Url.objects.filter(user_email=email, category_name=name)
                    for l in an:
                        l.category_name="not_defined"
                        l.save()
                    list.delete()
            except Exception, e:
                print ("Here is the error " + e.message)
    return HttpResponse("")


####################################
@login_required
def download(request, **kwargs):
    print(kwargs)
    if kwargs.has_key("base64string"):
        print (kwargs['base64string'])
        name=base64.b64decode((kwargs.get('base64string')))
        name=str(name).strip().lower()
        email=request.session['email']
        if name in ["csv", "html", "pdf"]:
            print (name + "format")
            try:
                all_url=Url.objects.filter(user_email=email, is_blocked=0, is_delete_parmently=0).order_by(
                    "-date_modified").values("url")
                list=[url['url'] for url in all_url]
                # print (list)

                if name == 'csv':
                    import csv

                    response=HttpResponse(content_type='text/csv')
                    response['Content-Disposition']='attachment; filename="somefilename.csv"'
                    writer=csv.writer(response)

                    writer.writerow([(str(i)) for i in list])
                    return response



                elif name == "html":
                    import csv

                    response=HttpResponse(content_type='text/csv')
                    response['Content-Disposition']='attachment; filename="somefilename.html"'
                    writer=csv.writer(response)
                    for i in list:
                        print (i)
                    writer.writerow([(str("<a href ='%s'>%s</a> </br>") % (i, i)) for i in list])
                    return response


                elif name == "pdf":
                    pass
            except Exception, e:
                print ("Downloading error ", e.message)

    return HttpResponse("")


@login_required
def format_date(request, **kwargs):
    if kwargs.has_key("base64string"):
        print (kwargs['base64string'])
        name=base64.b64decode((kwargs.get('base64string')))
        name=str(name).strip().lower()
        email=request.session['email']
        format_date=""
        if name in ["fixed", "relative"]:
            print (name + "format")
            try:

                if name == 'relative':
                    format_date="relative"
                elif name == "fixed":
                    format_date="fixed"

                s=Settings.objects.get(user_id=request.user.id)
                s.date_time_format=format_date
                s.save()
                request.session['format']=format_date
            except Exception, e:
                print ("Date Time format error ", e.message)

    return HttpResponse()
