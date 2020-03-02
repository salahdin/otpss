from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #remember to log the user in
            login(request, user)
            return redirect('accounts:signup')
        else:
            form = UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect('core:list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form':form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:signup')