from django.test import TestCase
from veganation.forms import User, UserRegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from veganation.models import UserProfile
from django.core.files import File
from django.utils import timezone
import os
import veganation
from veganation import forms

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

f"{FAILURE_HEADER} {FAILURE_FOOTER}"

#the tests for veganation website.

#this test checks if a user is set up correctly with username, email, password and default image. 

class MyAccountTest(TestCase):
    def set_up(self):
        user = User.objects.create(username = 'account1', email = 'account1@account1.com', password = 'password123')
        user.save()

        myaccount = UserProfile.objects.create(user=user)
        imgpath = os.path.join(os.getcwd(), 'media', 'default' + '.jpg')
        myaccount.image.save('default', File(open(imgpath, 'rb')))
        myaccount.save()

    
    def test_user_register(self):

       
       #test whether UserRegisterForm matches User Model
        user_form = forms.UserRegisterForm()
        self.assertEqual(type(user_form.__dict__['instance']), User, f"{FAILURE_HEADER}Your UserRegisterForm does not match up to the User model. Check your Meta definition of UserRegisterForm and try again.{FAILURE_FOOTER}")
        
        #form_data = {
           # 'username': 'account2',
            #'email' : 'account2@account2.com',
            #'password1' : 'password123',
            #'password2' : 'password123',
            #'firstName': 'TestfirstName',
            #'lastName': 'TestlastName',
            #'gender': 'gender1',
            #'veganSince' : 'child',
            #'age' : '23',
            #'quote' : 'vegan quote example',
            #'occupation' : 'occupation example',
            #'city' : 'Glasgow'
        #}
        #form = UserRegisterForm(data = form_data)
        #self.assertTrue(form.is_valid())

