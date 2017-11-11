import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from category.models import CategoryList
from content.models import Category, Url
from content.views import returnUrlTrashed


@login_required
def category(request, **kwargs):
    title="pinmyblogs|category"
    q=""

    if (request.method == 'GET' and request.session.has_key("email")):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)
        try:
            q=Category.objects.filter(created_by=email, is_blocked=0, ).values(("category_name"))

        except  Exception, e:
            print("What is the error", e.message)

        return render(request, "category.html", {"title": title,
                                                 "numberintrash": numberintrash,
                                                 "q": q
                                                 })

    if (request.method == 'POST' and request.session.has_key("email")):
        email=request.session.get("email")
        numberintrash=returnUrlTrashed(email=email)
        try:
            if ("createnew" in request.POST):
                new_category=str(request.POST["createnew"]).strip().lower()
                exists=CategoryList.objects.filter(name=new_category)

                if (not exists.exists()):
                    CategoryList.objects.create(name=new_category, is_blocked=0)

                    q=Category.objects.create(created_by=email, is_blocked=0, category_name=new_category)

                else:
                    q=None
                    q=Category.objects.filter(created_by=email, is_blocked=0, ).values(("category_name"))
                    filter=q.filter(category_name=new_category)
                    print (new_category)
                    if filter.exists():
                        print ("This is counted in the category that is already created by the user")
                    else:
                        print ("Not exists in the users list ")

        except  Exception, e:
            print("What is the error", e.message)

    return redirect("categoryshow")


@login_required
def showcategorylistwise(request):
    if (request.session.has_key("email")):
        email=request.session['email']
        if ("select_category" in request.POST):
            data=[]
            select_category=request.POST['select_category'].lower()
            print (select_category)

            hi=[]
            response_data={}

            try:
                q=Url.objects.filter(user_email=email,
                                     category_name=select_category,
                                     is_delete_parmently=0,
                                     is_trashed=0)

                for i in q:
                    hi.append(i.url)
                    response_data['message']=hi
            except Exception, e:

                print ("Error", e.message)
                response_data['message']="error"

            print (json.dumps(response_data))

            return HttpResponse(json.dumps(response_data), content_type="application/json")
