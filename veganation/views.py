from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from veganation.forms import UserRegisterForm, UserProfileForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from .forms import LocationForm
from .models import Location
from django.contrib.auth.models import User
from .models import UserProfile
from django.db import models
from django.core.mail import send_mail
from django.core import mail

def index(request):
    return render(request, 'veganation/index.html')

def restaurants(request):
    context_dict = {}
    return render(request, 'veganation/restaurants.html', context=context_dict)


def protests(request):
    context_dict = {}
    return render(request, 'veganation/protests.html', context=context_dict)


@login_required(login_url="http://127.0.0.1:8000/veganation/login/")
def location(request):
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.userBuddy=request.user
			instance.save()
			form.save()


			same_rest=Location.objects.filter(rest=instance.rest).filter(date1=instance.date1)
			l = []
			for r in same_rest:
				l.append(r.id)
			emails=[]
			same_rest=Location.objects.filter(rest=instance.rest).filter(date1=instance.date1)
			for meet in same_rest:
				person=meet.userBuddy
				user = User.objects.get(username=person)
				user_email=user.email
				emails.append(user_email)

			print(same_rest)
			print(emails)

			if(len(emails)>1):
				if user.email:
					mail_body = ("hi!")
					send_mail('Checking!',mail_body,'veganationglasgirls20@gmail.com',emails,)


			return redirect('http://127.0.0.1:8000/veganation/restaurants/')
	else:
		form = LocationForm()
		return render(request, 'veganation/location.html',
                      {'form':form})





@login_required
def myaccount(request):
    if request.method == 'POST':
        u_form = UserProfileForm(request.POST, instance= request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.myaccount)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('myaccount')
    else:
        u_form = UserProfileForm(instance= request.user)
        p_form = ProfileUpdateForm(instance = request.user.myaccount)


    context_dict = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'veganation/myaccount.html',context=context_dict)

def signup(request):
    #registered = False

    #if request.method == 'POST':
        #user_form = UserForm(request.POST)
        #profile_form = UserProfileForm(request.POST)

        #if user_form.is_valid() and profile_form.is_valid():
            #user = user_form.save()


            #user.set_password(user.password)
            #user.save()


            #profile = profile_form.save(commit=False)
            #profile.user = user

            #if 'image' in request.FILES:
                #profile.image = request.FILES['image']

            #profile.save()

            #registered = True
            #messages.success(request, f'Account created for {user} !')
            #return redirect('index')
        #else:
            #print(user_form.errors, profile_form.errors)
    #else:
       # user_form = UserForm()
        #profile_form = UserProfileForm()

    #return render(request, 'veganation/signup.html',
                #  context = {'user_form': user_form,
                 #            'profile_form': profile_form,
                  #           'registered':registered})

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('veganation:login')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'veganation/signup.html', context = {'form': form, 'profile_form':profile_form} )

def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('veganation:index'))
            else:
                return HttpResponse("Your Veganation account is disabled.")
        else:
            context_dict = {}
            context_dict['invalid'] = True
            return render(request, 'veganation/login.html', context = context_dict)

    else:
        return render(request, 'veganation/login.html')

@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
    logout(request)
# Take the user back to the homepage.
    return redirect(reverse('veganation:index'))
