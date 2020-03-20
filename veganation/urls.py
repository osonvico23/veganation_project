from django.urls import path
from veganation import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'veganation'

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.restaurants, name='restaurants'),
    path('protests/', views.protests, name='protests'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    ]
#serving files uploaded by user during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
