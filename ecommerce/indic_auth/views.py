from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages  

from .forms import UserSignUpForm


# Create your views here... ... ... ... ... ...
def signup_view(request):
  if request.method == 'POST':
    form = UserSignUpForm(request.POST)
    if form.is_valid:
      user = form.save(commit=False)
      # user.is_active = False
      user.save()
      messages.success(request, 'Your account has been created! Please verify your email.')
      return redirect('login')
    else:
      return render(request, 'indic_auth/signup.html', context={'form': form})

  else:
    form = UserSignUpForm()
  return render(request, 'indic_auth/signup.html', context={'form': form})


  
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      messages.success(request, 'You are logged in successfully!')
      return redirect('home')
    else:
      messages.error(request, 'something went wrong. please try again later!')

      return render(request, 'indic_auth/login.html', context={'form': form})

  form = AuthenticationForm()
  return render(request, 'indic_auth/login.html', context={'form': form})


def logout_view(request):
  logout(request)
  messages.success(request, "You're logged out successfully!")
  return redirect('login')


