from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from veganation.forms import UserRegisterForm, UserProfileForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.shortcuts import render_to_response
from django.contrib import messages

def index(request):
    return render(request, 'veganation/index.html')

def restaurants(request):
    context_dict = {}
    return render(request, 'veganation/restaurants.html', context=context_dict)

def protests(request):
    context_dict = {}
    return render(request, 'veganation/protests.html', context=context_dict)

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

    return render(request, 'veganation/myaccount.html', context=context_dict)

def socialsLogin(request):
    return render(request, 'veganation/socialsLogin.html')

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
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'veganation/signup.html', {'form': form})
def user_login(request):
# If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

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
