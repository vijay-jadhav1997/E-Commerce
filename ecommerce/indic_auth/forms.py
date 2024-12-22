from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserSignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']
    # fields = "__all__"


# class UserLoginForm(forms.ModelForm):
#   # password1 = forms.PasswordInput()
#   class Meta:
#     model = User
#     fields = ['username', 'password1']
#     # fields = "__all__"
#     widgets= {

#     }
    

