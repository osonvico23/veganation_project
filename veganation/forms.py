from django.contrib.auth.models import User
from veganation.models import UserProfile
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'veganSince',
        'isVegan', 'profilePic', 'quote', 'occupation', 'city',)
