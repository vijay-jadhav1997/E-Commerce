from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserSignUpForm(UserCreationForm):
  # password = forms.CharField(widget=forms.PasswordInput)
  # confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    # fields = ['username', 'email', 'password', 'confirm_password']
    # fields = "__all__"

  # def clean(self):
  #   cleaned_data = super().clean()
  #   password = cleaned_data.get('password')
  #   confirm_password = cleaned_data.get('confirm_password')

  #   if password and confirm_password and password != confirm_password:
  #     raise forms.ValidationError("Password do not match.")
    
  #   return cleaned_data

    


# class UserLoginForm(forms.ModelForm):
#   # password1 = forms.PasswordInput()
#   class Meta:
#     model = User
#     fields = ['username', 'password1']
#     # fields = "__all__"
#     widgets= {

#     }
    

