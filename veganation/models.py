from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from PIL import Image
import datetime
import uuid
from django_google_maps import fields as map_fields
from star_ratings.models import Rating


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique = True, related_name = "myaccount", null=True)
	gender = models.IntegerField(blank = True, default = 3)
	email = models.EmailField(default = 'veganation@gmail.com')
	veganSince = models.CharField(max_length=30, blank=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True)
	quote = models.TextField(max_length=100, blank=True)
	occupation = models.CharField(max_length=50, blank = True)
	city = models.CharField(max_length=40, blank=True)
	firstName = models.CharField(max_length=30, blank=True)
	lastName = models.CharField(max_length=40, blank=True)
	age = models.IntegerField(default = 20)

	def __str__(self):
		return f'{self.user.username} UserProfile'

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user = kwargs['instance'])

post_save.connect(create_profile, sender = User)

def save(self):
	super().save()

	img = Image.open(self.image.path)

	if img.height > 300 or img.width > 300:
		output_size = (300, 300)
		img.thumbnail(output_size)
		img.save(self.image.path)



class Rental(models.Model):
	address = map_fields.AddressField(max_length=200)
	geolocation = map_fields.GeoLocationField(max_length=100)


class Location(models.Model):
	userBuddy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	date1 = models.DateField(default=timezone.now)
	date2 = models.DateField(default=timezone.now)
	date3 = models.DateField(default=timezone.now)
	rest = models.IntegerField(default=2)

	age = models.IntegerField(default=5)
	gender = models.IntegerField(default=2)

class Rate(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	hug_rate = models.IntegerField(null=True, blank=True)
	seren_rate = models.IntegerField(null=True, blank=True)
	the78_rate = models.IntegerField(null=True, blank=True)
	glasvegan_rate = models.IntegerField(null=True, blank=True)
	puti_rate = models.IntegerField(null=True, blank=True)
	mono_rate = models.IntegerField(null=True, blank=True)
	picnic_rate = models.IntegerField(null=True, blank=True)
	vandv_rate = models.IntegerField(null=True, blank=True)
