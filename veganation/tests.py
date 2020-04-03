from django.test import TestCase
from veganation.forms import User, UserRegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from veganation.models import UserProfile
from django.core.files import File
from django.utils import timezone
import os

#the tests for veganation website.

#this test checks if a user is set up correctly with username, email, password and default image. 

class MyAccountTest(TestCase):
    def set_up(self):
        user = User.objects.create(username = 'account1', email = 'account1@account.com', password = 'password123')
        user.save()

        myaccount = UserProfile.objects.create(user=user)
        imgpath = os.path.join(os.getcwd(), 'media', 'default' + '.jpg')
        myaccount.image.save('default', File(open(imgpath, 'rb')))
        myaccount.save()

