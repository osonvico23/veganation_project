"""veganation_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from veganation import views
from django.urls import include
from veganation import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from veganation import views as user_views

urlpatterns = [
    path('', views.index, name='index'),
    path('veganation/', include('veganation.urls')),
    path('accounts/', include('allauth.urls')),
    path('myaccount/', user_views.myaccount, name='myaccount'),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings'), name='ratings'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='veganation/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='veganation/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='veganation/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
