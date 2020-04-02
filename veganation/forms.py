from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from veganation.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
import datetime
from django.utils import timezone
from .models import Location, Restaurant
from datetime import date
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


#these variables are used respectively for choices fields in the forms below.
YEARS= [x for x in range(2020,2060)]



REST_CHOICES=((1,"V&V Café"),(2,"The 78"),(3,"Serenity No"),(4,"The Glasvegan"),(5,"Picnic"),(6,"Puti Vegan Cafe"),(7,"Hug and Pint"),(8,"Mono"))

AGE_CHOICES=((18,25),(25,35),(35,45),(45,55),(55,65),(65,75),(75,85),(95,100))
GENDER_CHOICES=((1,'Male'),(2,'Female'),(3,'No Preference'))

#user form used when a user signs up. Note that username, password1, password2 are built in UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#profile form that is displayed and updated in my account page.
class UserProfileForm(forms.ModelForm):
    firstName = forms.CharField()
    lastName = forms.CharField()
    gender = forms.CharField(required = False)
    veganSince = forms.CharField(required = False)
    age = forms.IntegerField()
    quote = forms.CharField(required = False)
    occupation = forms.CharField(required = False)
    city = forms.CharField()

    #saving the fields.
    def signup(self, request, user):
        user.firstName = self.cleaned_data['firstName']
        user.lastName = self.cleaned_data['lastName']
        user.veganSince = self.cleaned_data['veganSince']
        user.quote = self.cleaned_data['quote']
        user.occupation = self.cleaned_data['occupation']
        user.city = self.cleaned_data['city']
        user.gender = self.cleaned_data['gender']
        user.age = self.calculate_age['age']

        user.save()
    class Meta:
        model = UserProfile
        fields = ['firstName', 'lastName','veganSince', 'gender', 'age',
        'quote', 'occupation', 'city',]


#The next two forms are used to update a user account.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'firstName', 'lastName','veganSince', 'gender', 'age',
        'quote', 'occupation', 'city',]


class LocationForm(forms.ModelForm):
	rest = forms.ChoiceField(label="Please choose a restaurant",choices = REST_CHOICES,required =True)
	date1 = forms.DateField(label="When are you free?",widget=forms.SelectDateWidget(years=YEARS))
	age = forms.ChoiceField(label="Let us know what age group you're comfortable meeting?",choices = AGE_CHOICES, required = False)
	gender = forms.ChoiceField(label="Let us know which gender you're comfortable meeting?",choices = GENDER_CHOICES, required = False)
	myage = forms.ChoiceField(label="Please enter your age",choices = AGE_CHOICES, required = False)
	mygender = forms.ChoiceField(label="Please enter your gender",choices = GENDER_CHOICES, required = False)

	class Meta:
		model = Location
		fields = ['rest','date1',
		'age','gender','myage','mygender'
		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Save'))


class RateForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Restaurant
        fields = ('name', 'user', 'rating')