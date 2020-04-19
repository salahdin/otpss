from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .finallist import programList


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    username = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password1 = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation', 'class': 'form-control'}))

    class Meta:
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']
        model = User


class UserProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.widgets.FileInput(attrs={'class': 'avatar avatar-24 img-circle'}))
    studentId = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'placeholder': 'student id', 'class': 'form-control'}))
    program = forms.ChoiceField(label='program', widget=forms.Select(attrs={'class': 'form-control'}), choices=programList)

    class Meta:
        model = UserProfile
        fields = ['avatar', 'studentId', 'program']


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))


