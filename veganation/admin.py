from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from veganation.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm, UserProfileForm

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    #add_form = UserRegisterForm
    #form = UserProfileForm
    #model = UserProfile
    list_display = ["username", "email", "firstName", "lastName", 'veganSince',
        'isVegan',  'quote', 'occupation', 'city']

    add_fieldsets = (
            (
                None,
                {
                    "classes": ("wide",),
                    "fields": ("username", "password1", "password2", 'firstName', 'lastName','veganSince',
        'isVegan',  'quote', 'occupation', 'city'),
                },
            ),
        )
    

admin.site.register(UserProfile, CustomUserAdmin)

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
        'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
