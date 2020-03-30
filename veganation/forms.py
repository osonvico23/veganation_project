from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from veganation.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
import datetime
from django.utils import timezone
from veganation.models import Location

YEARS= [x for x in range(1940,2010)]



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
    veganSince = forms.DateField(label='When did you become vegan?', initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS), required = False)
    birth_date= forms.DateField(label='What is your birth date?',initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS), required = False)
    quote = forms.CharField(required = False)
    occupation = forms.CharField(required = False)
    city = forms.CharField()

    def signup(self, request, user):
        user.firstName = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.veganSince = self.cleaned_data['veganSince']
        user.birth_date = self.cleaned_data['birth_date']
        user.quote = self.cleaned_data['quote']
        user.occupation = self.cleaned_data['occupation']
        user.city = self.cleaned_data['city']
        user.save()



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstName', 'lastName','veganSince',
        'birth_date',  'quote', 'occupation', 'city',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        #fields taken out firstName and lastName
        fields = ('firstName', 'lastName','veganSince',
        'birth_date',  'quote', 'occupation', 'city',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']



class Location(forms.Form):
	
	date1 = forms.DateField()
	time1 = forms.TimeField(required= False)
	date2 = forms.DateField()
	time2 = forms.TimeField(required= False)
	date3 = forms.DateField()
	time3 = forms.TimeField(required= False)
	age = forms.IntegerField(
        max_length=7,
        widget=forms.Select(choices=AGE_CHOICES),)
	gender = forms.IntegerField( max_length=7, widget=forms.Select(choices=GENDER_CHOICES),)
	
	