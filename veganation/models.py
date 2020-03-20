from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from django_google_maps import fields as map_fields
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #firstName = models.CharField(max_length=30, blank = True)
    #lastName = models.CharField(max_length=40, blank = True)

    email = models.EmailField(default = 'veganation@gmail.com')
    veganSince = models.DateTimeField(blank = True)
    isVegan = models.BooleanField(blank = True, default=False)
    profilePic = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True)
    quote = models.TextField(max_length=100, blank=True)
    occupation = models.CharField(max_length=50, blank = True)
    city = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.user.username

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
