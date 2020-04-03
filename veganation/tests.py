from django.test import TestCase
from veganation.forms import User, UserRegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from veganation.models import UserProfile,Location
from django.core.files import File
from django.utils import timezone
import os
import veganation
from veganation import forms
from django.forms import fields as django_fields
from django.urls import reverse

import importlib

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


        fields = user_form.fields

        expected_fields = {
            'username': django_fields.CharField,
            'email': django_fields.EmailField,
            'password1': django_fields.CharField,
            'password2': django_fields.CharField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field {expected_field_name} was not found in the UserRegisterForm. Please try again{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field {expected_field_name} in UserRegisterForm was not of the correct type. Expected {expected_field}; got {type(fields[expected_field_name])}.{FAILURE_FOOTER}")


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

class TemplateTests(TestCase):

	def test_index_using_template(self):
		# Check the template base is being used
		response = self.client.get(reverse('index'))
		self.assertTemplateUsed(response, 'veganation/base.html')


class DataBaseTests(TestCase):
     def does_gitignore_include_database(self, path):
        """
        Takes the path to a .gitignore file, and checks to see whether the db.sqlite3 database is present in that file.
        """
        f = open(path, 'r')

        for line in f:
            line = line.strip()

            if line.startswith('db.sqlite3'):
                return True

        f.close()
        return False

class modelTests(TestCase):

    def setUp(self):
        UserProfile_py = UserProfile.objects.get_or_create(lastName= "veganation",email='veganation@gmail', firstName='veganation')
        UserProfile_py2=UserProfile.objects.get_or_create(lastName= "vegans",email='veganationglasgirls20@gmail', firstName='vegan')

        Location.objects.get_or_create(rest=1,
                                   gender=1,
                                   age=2,myage=2,mygender=1)

        Location.objects.get_or_create(rest=3,
                                   gender=1,
                                   age=2,myage=2,mygender=1)



    def test_location_model(self):
        """
        Runs a series of tests on the Location model.
        Do the correct attributes exist?
        """
        UserProfile_py = UserProfile.objects.get(firstName='veganation')
        location = Location.objects.get(rest=1)
        self.assertEqual(location.gender, 1, f"{FAILURE_HEADER}Tests on the Location model failed. {FAILURE_FOOTER}")
        self.assertEqual(location.age, 2, f"{FAILURE_HEADER}Tests on the Location model failed. {FAILURE_FOOTER}")
        self.assertEqual(location.mygender, 1, f"{FAILURE_HEADER}Tests on the Location model failed. {FAILURE_FOOTER}")
        self.assertEqual(location.myage, 2, f"{FAILURE_HEADER}Tests on the Location model failed. {FAILURE_FOOTER}")
