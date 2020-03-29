from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from veganation.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm



#class UserRegisterForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    #class Meta:
        #model = User
        #fields = ('username', 'email','password')

#inherits from the userCreationForm, adding extra fields
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    veganSince = forms.CharField()
    isVegan = forms.CharField()
    quote = forms.CharField(required = False)
    occupation = forms.CharField(required = False)
    city = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstName', 'lastName','veganSince',
        'isVegan',  'quote', 'occupation', 'city',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        #fields taken out firstName and lastName
        fields = ('firstName', 'lastName','veganSince',
        'isVegan',  'quote', 'occupation', 'city',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
