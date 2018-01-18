from django.contrib.auth.models import User
from django import forms


class UserForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CommentForm(forms.Form):
    comment = forms.CharField()

class UserInfoForm(forms.Form):
    propic = forms.FileField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    profession = forms.CharField()
    color = forms.CharField()