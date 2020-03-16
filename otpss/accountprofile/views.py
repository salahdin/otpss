from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from . forms import *


# Create your views here.
"""def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profileform = UserProfileForm(request.POST)
        if form.is_valid() and profileform.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()
            # remember to log the user in
            login(request, user)
            return redirect('accounts:login')
    else:
        form = SignUpForm()
        profileform = UserProfileForm()
    return render(request, 'accounts/signup.html', {'form': form , 'profile':profileform})
"""

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            return redirect('core:list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def frontpage(request):
    if request.method == 'POST':
        if 'signupform' in request.POST:
            signupform = SignUpForm(data=request.POST)
            profileform = UserProfileForm(data=request.POST)
            signinform = SignInForm()

            if signupform.is_valid():
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                profile = profileform.save(commit=False)
                profile.user = user
                profile.save()
                # remember to log the user in
                login(request, user)
                return redirect('core:home_page')
        else:
            signinform = SignInForm(data=request.POST)
            signupform = SignUpForm()

            if signinform.is_valid():
                login(request, signinform.get_user())
                return redirect('core:home_page')
    else:
        signupform = SignUpForm()
        signinform = SignInForm()
        profileform = UserProfileForm()

    return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform, 'profileform':profileform })