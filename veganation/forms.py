from django.contrib.auth.models import User
from veganation.models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','firstName','lastName','email',
        'password')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False);


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('veganSince',
        'isVegan', 'profilePic', 'quote', 'occupation', 'city',)
