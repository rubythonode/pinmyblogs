from __future__ import division, unicode_literals
from __future__ import print_function
from __future__ import print_function

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from account.forms import SignUpForm, LoginForm


def register(request):
    print(str(request.user))

    if (not (request.user.is_authenticated())):

        title="pinmyblogs|register"

        if (request.method == 'GET'):

            return render(request, 'register.html', {"title": title, })

        elif (request.method == "POST") and (request.POST['reg'] == 'REGISTER'):

            form=SignUpForm(request.POST)
            print(form.data['email'] + "")
            if (form.is_valid()):

                # try:#

                password=form.cleaned_data.get('password')
                username=form.cleaned_data.get('username')
                email=form.cleaned_data.get('email')

                User.objects.create_user(username=username, password=password, email=email)

                # _=send_hash()

                # print(_)
                # Settings.objects.create(user=username, user_nash=_)

                print("user created successfully")

                return redirect('login')


                # except:
                # print("Error in user creation")
                # return render(request, 'register.html', {"title": title, 'error': False})

            elif not form.is_valid():

                error=True
                errors={}

                if 'username' in form.errors:
                    errors['username']=form.errors['username']
                if 'email' in form.errors:
                    print(form.errors['email'])
                    errors['email']=form.errors['email']
                if 'password' in form.errors:
                    errors['password']=form.errors['password']

                print(form.errors)

                return render(request, 'register.html', {"title": title, 'errorlist': errors, 'error': error})
        else:
            return render(request, 'register.html', {"title": title, })

    else:

        return redirect('dashboard')


def loginuser(request):
    print(request.session.items())

    if (request.user.is_authenticated()):
        title="pinmyblogs|dashboard"
        return redirect('dashboard')

    else:
        title="Pinmyblogs|Login"
        data={}
        if (request.method == "POST"):

            form=LoginForm(request.POST)
            if form.is_valid():
                email=form.cleaned_data.get('email')
                password=form.cleaned_data.get('password')
                username=User.objects.filter(email=email)
                # print(username)
                if (username):

                    print(username[0])
                    try:
                        user=authenticate(username=username[0], password=password)
                        login(request, user)
                        request.session['email']=email

                        return redirect('dashboard')
                    except Exception:
                        print("error is here")
                        data['error']='Invalid E-mail/Password'
                        return render(request, 'login.html', {'title': title, 'error': data['error']})

                else:
                    print(form.errors)
                    print('Here we got the main error ')

                    data['error']='Invalid E-mail/Password'
                    return render(request, 'login.html', {'title': title, 'error': data['error']})
            else:
                data['error']='Invalid E-mail/Password'

                return render(request, 'login.html', {'title': title, 'error': data['error']})

        data={"title": title}
        return render(request, 'login.html', data)


def send(request):
    return HttpResponse("<okkkk>")
