from django.contrib.auth.models import User
from veganation.models import UserProfile
from django import forms
from captcha.fields import CaptchaField
from django.conf import settings

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email','password')


class UserProfileForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = UserProfile
        #fields taken out firstName and lastName
        fields = ('veganSince',
        'isVegan', 'firstName', 'lastName','picture', 'quote', 'occupation', 'city',
        'captcha')
