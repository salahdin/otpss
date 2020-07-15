from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from . forms import *
from .models import UserProfile
from django.contrib.auth.models import User


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
    """
    delete session and redirect to landing page
    :param request:
    :return:
    """
    logout(request)
    return redirect('/')


def frontpage(request):
    # redirect user to main page if authenticated
    """

    :param request:
    :return: signin and register form
    """
    if request.user.is_authenticated:
        return redirect('core:home_page')
    profileform = UserProfileForm()
    if request.method == 'POST':
        if 'signupform' in request.POST:
            signupform = SignUpForm(data=request.POST)
            profileform = UserProfileForm(request.POST, request.FILES)
            signinform = SignInForm()

            if signupform.is_valid():
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                signupform.save()
                user = authenticate(username=username, password=password)
                # create user profile object
                try:
                    UserProfile.objects.create(user=user, studentId=request.POST['studentId'],
                                               program=request.POST['program'],
                                               avatar=request.FILES['avatar']
                                               )
                except Exception:
                    pass
                # log the user in
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

    context = {'signupform': signupform,
               'signinform': signinform,
               'profileform': profileform
               }
    return render(request, 'frontpage.html', context)


def profileDetailView(request, id_):
    """
    detail view of a user
    :param request:
    :param id_: user id
    :return: profile and user instance
    """
    if request.user.is_authenticated:
        person = get_object_or_404(User, id=id_)
        person_profile = person.profile

        return render(request, 'profileview.html', {'person': person, 'person_profile': person_profile})
    return redirect('/')


def editProfile(request, id_):
    pass
