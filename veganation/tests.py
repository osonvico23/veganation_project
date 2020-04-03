from django.test import TestCase
from veganation.forms import UserRegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from veganation.models import UserProfile
from django.core.files import File
from django.utils import timezone
import os

#the tests for veganation website.

#this test checks if a user is set up correctly 


