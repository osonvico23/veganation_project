from django.contrib import admin
<<<<<<< HEAD
from veganation.models import UserProfile
# Register your models here.

admin.site.register(UserProfile)
=======
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
        'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }
>>>>>>> f2988e38a9b2e10d4570b3084fef97df7b681f21
