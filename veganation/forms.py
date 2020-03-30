from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from veganation.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
import datetime
from django.utils import timezone
from veganation.models import Location
from datetime import date


YEARS= [x for x in range(1940,2010)]
CHOICES = (
    (1, ('female')),
    (2, ('male')),
    (3, ('prefer not to say'))
    )

AGE_CHOICES=((18,25),(25,35),(35,45),(45,55),(55,65),(65,75),(75,85),(95,100))
GENDER_CHOICES=(('MALE','male'),('FEMALE','female'),('NO PREFERENCE','no preference'))



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
        user.birth_date = self.cleaned_data['birth_date']
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



class Location(forms.Form):
	date1 = forms.DateField()
	time1 = forms.TimeField(required= False)
	date2 = forms.DateField()
	time2 = forms.TimeField(required= False)
	date3 = forms.DateField()
	time3 = forms.TimeField(required= False)
	age = forms.IntegerField(
        widget=forms.Select(choices=AGE_CHOICES),)
	gender = forms.IntegerField( widget=forms.Select(choices=GENDER_CHOICES),)
	
	