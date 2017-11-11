# from settings import ALLOWED_SIGNUP_DOMAINS

from django import forms

from validator import *


class SignUpForm(forms.Form):
    username = forms.CharField(validators=[emptyCheck, nickNameValidator, UniqueUsernameIgnoreCaseValidator],
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}),
                               max_length=30,
                               required=True)

    password = forms.CharField(validators=[emptyCheck, passwordValidator],
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))

    email = forms.CharField(validators=[emptyCheck, emailValidator, UniqueEmailValidator, ],
                            widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            required=True,
                            max_length=100)

    def clean(self):
        super(SignUpForm, self).clean()

        print ("inside the clean")

        password = self.cleaned_data.get('password')

        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get('username')

        return self.cleaned_data


class LoginForm(forms.Form):
    password = forms.CharField(validators=[emptyCheck, ],
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))

    email = forms.CharField(validators=[emptyCheck, emailValidator, ],
                            widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            required=True,
                            max_length=100)

    def clean(self):
        super(LoginForm, self).clean()

        print ("inside the clean")

        password = self.cleaned_data.get('password')

        email = self.cleaned_data.get("email")

        return self.cleaned_data
