from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from veganation.forms import UserRegisterForm, UserProfileForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from .forms import LocationForm, RateForm
from .models import Location
from django.contrib.auth.models import User
from .models import UserProfile
from django.db import models
from django.core.mail import send_mail
from django.core import mail

def index(request):
    return render(request, 'veganation/index.html')

def about(request):
    return render(request, 'veganation/about.html')

def restaurants(request):
    form = RateForm()
    if request.method == 'POST':
    # take care of instance
        form = RateForm(request.POST, instance=request.user)
        if form.is_valid():
            rate = form.save(commit=False)
            # adding the user here.
            rate.user = request.user
            rate.save()
    return render(request, 'veganation/restaurants.html',{'form': form})


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
			l = []
			same_rest=Location.objects.filter(rest=instance.rest).filter(date1=instance.date1).filter(age=instance.myage).filter(myage=instance.age).filter(mygender=instance.gender).filter(gender=instance.mygender)
			for r in same_rest:
				l.append(r.id)
			emails=[]
			flag="True";
			for meet in same_rest:
				person=meet.userBuddy
				user = User.objects.get(username=person)
				user_email=user.email
				for email in emails:
					if(email== user_email):
						flag="False";

				if(flag=="True"):
					emails.append(user_email);
				flag="True";
			print(same_rest)
			print(emails)
			if(instance.rest==1):
				restname="V&V Café"
			elif(instance.rest==2):
				restname="The 78"
			elif(instance.rest==3):
				restname="Serenity No"
			elif(instance.rest==4):
				restname="The Glasvegan"
			elif(instance.rest==5):
				restname="Picnic"
			elif(instance.rest==6):
				restname="Puti Vegan Cafe"
			elif(instance.rest==7):
				restname="Hug and Pint"
			elif(instance.rest==8):
				restname="Mono"
			if(len(emails)>1):
				if user.email:
					mail_body = ("Hello!" +  "\nYou've recently put in a request to find a buddy to visit " + restname +  " on " + str(instance.date1) +". " + "\nYour buddy(ies) is(are) also reciepents of this email so feel free to email them and arrange a meeting!" + "\n\nFeel free to contact us anytime."+ "\nHope you enjoy meeting our fellow vegans!" + "\n\nWith love \nVeganation")
					send_mail("We've found you a buddy!",mail_body,'veganationglasgirls20@gmail.com',emails,)


			return redirect('http://127.0.0.1:8000/veganation/restaurants/')
	else:
		form = LocationForm()
		return render(request, 'veganation/location.html',
                      {'form':form})





@login_required
def myaccount(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance= request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.myaccount)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('myaccount')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance = request.user.myaccount)


    context_dict = {
        'u_form' : u_form,
        'p_form' : p_form
    }

    return render(request, 'veganation/myaccount.html',context_dict)


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('veganation:login')
    else:
        form = UserRegisterForm()
    return render(request, 'veganation/signup.html', context = {'form': form})

def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        #authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                #log the user in and redirect to the home page
                login(request, user)
                return redirect(reverse('veganation:index'))
            else:
                #if users account is not active, report that the account is disabled
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
