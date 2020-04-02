from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from veganation.models import UserProfile
from .models import Location, Restaurant
from django.contrib.auth.admin import UserAdmin
from veganation.forms import UserRegisterForm


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "firstName", "lastName", 'veganSince',
        'age', 'gender',  'quote', 'occupation', 'city']

# Register your models here.

#class CustomUserAdmin(admin.ModelAdmin):
    #add_form = UserRegisterForm
    #form = UserProfileForm
    #model = UserProfile
    #list_display = ["username", "email", "firstName", "lastName", 'veganSince',
        #'isVegan',  'quote', 'occupation', 'city']
    #list_filter = ("username",)

   # add_fieldsets = (
   #         (
    #            None,
     #           {
      #              "classes": ("wide",),
       #             "fields": ("username", "password1", "password2", 'firstName', 'lastName','veganSince',
        #'isVegan',  'quote', 'occupation', 'city'),
         #       },
          #  ),
        #)


admin.site.register(UserProfile, UserProfileAdmin,)
admin.site.register(Location)
admin.site.register(Restaurant)

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
        'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
