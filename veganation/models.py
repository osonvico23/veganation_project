from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from PIL import Image
import datetime

from django_google_maps import fields as map_fields
# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, unique = True, related_name = "myaccount")
	#firstName = models.CharField(max_length=30, blank = True)
	#lastName = models.CharField(max_length=40, blank = True)
	#username = models.CharField(max_length=40, blank = True)
	gender = models.IntegerField(blank = True, default = 3)
	email = models.EmailField(default = 'veganation@gmail.com')
	veganSince = models.DateTimeField(blank = True, default=datetime.date.today)
	birth_date= models.DateField(blank = True, default=datetime.date.today)
	image = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True)
	quote = models.TextField(max_length=100, blank=True)
	occupation = models.CharField(max_length=50, blank = True)
	city = models.CharField(max_length=40, blank=True)
	firstName = models.CharField(max_length=30, blank=True)
	lastName = models.CharField(max_length=40, blank=True)
    



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

#@receiver(post_save, sender = User)
#def create_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      UserProfile.objects.created(user = instance)
#@receiver(post_save, sender = User)
#def save_user_profile(sender, instance, **kwargs):
 #   instance.profile.save()

AGE_CHOICES=((18,25),(25,35),(35,45),(45,55),(55,65),(65,75),(75,85),(95,100))
GENDER_CHOICES=(('MALE','male'),('FEMALE','female'),('NO PREFERENCE','no preference'))


class Location(models.Model):
	date1 = models.DateField(default=datetime.date.today)
	time1 = models.TimeField(default=timezone.now)
	date2 = models.DateField(default=datetime.date.today)
	time2 = models.TimeField(default=timezone.now)
	date3 = models.DateField(default=datetime.date.today)
	time3 = models.TimeField(default=timezone.now)
	age = models.IntegerField( choices=AGE_CHOICES)
	gender = models.CharField(max_length=7, choices= GENDER_CHOICES)


class Rental(models.Model):
	address = map_fields.AddressField(max_length=200)
	geolocation = map_fields.GeoLocationField(max_length=100)
