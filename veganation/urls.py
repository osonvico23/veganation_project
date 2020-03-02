from django.urls import path
from veganation import views

app_name = 'veganation'

urlpatterns = [
    path('', views.index, name='index'),
    ]
