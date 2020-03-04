from django.urls import path
from veganation import views

app_name = 'veganation'

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.restaurants, name ='restaurants'),
    path('', views.protests, name = 'protests'),
    ]
