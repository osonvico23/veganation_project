from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from veganation.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
import datetime
from django.utils import timezone
from .models import Location
from datetime import date
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions



YEARS= [x for x in range(1940,2010)]
CHOICES = (
    (1, ('female')),
    (2, ('male')),
    (3, ('prefer not to say'))
    )


REST_CHOICES=((1,"V&V Café"),(2,"The 78"),(3,"Serenity No"),(4,"The Glasvegan"),(5,"Picnic"),(6,"Puti Vegan Cafe"),(7,"Hug and Pint"),(8,"Mono"))

AGE_CHOICES=((18,25),(25,35),(35,45),(45,55),(55,65),(65,75),(75,85),(95,100))
GENDER_CHOICES=((1,'Male'),(2,'Female'),(3,'No Preference'))

#class UserRegisterForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    #class Meta:
        #model = User
        #fields = ('username', 'email','password')
#birth_date= forms.DateField(label='What is your birth date?',initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS), required = False)

#inherits from the userCreationForm, adding extra fields
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    gender = forms.ChoiceField(choices = CHOICES, required = False)
    veganSince = forms.DateField(label='When did you become vegan?', initial="1990-06-21", widget=forms.SelectDateWidget(years=YEARS), required = False)
    age = forms.IntegerField()
    quote = forms.CharField(required = False)
    occupation = forms.CharField(required = False)
    city = forms.CharField()
    

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
	
    
    
    #def calculate_age(self):
     #   today = date.today()
      #  return today.year - self.year - ((today.month, today.day) < (self.month, self.day))



    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'firstName', 'lastName', 'gender', 'age','veganSince', 
        'quote', 'occupation', 'city',]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        #fields taken out firstName and lastName
        fields = ('firstName', 'lastName','veganSince', 'gender', 'age',
        'quote', 'occupation', 'city',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class LocationForm(forms.ModelForm):
	rest = forms.ChoiceField(label="Please choose a restaurant",choices = REST_CHOICES,required =True)
	date1 = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
	
	date2 = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
	
	date3 = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

	age = forms.ChoiceField(choices = AGE_CHOICES, required = False)
	gender = forms.ChoiceField(choices = GENDER_CHOICES, required = False)


	class Meta:
		model = Location
		fields = ['rest','date1',
		'date2',
		'date3',
		'age','gender',
		]
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.add_input(Submit('submit', 'Save'))
		
	
		


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		