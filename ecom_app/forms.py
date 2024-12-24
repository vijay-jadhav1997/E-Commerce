from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
  class Meta:
    model = Contact
    fields = "__all__"
    widgets= {
      'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Name'}), 
      'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Your Email'}), 
      'phone_numb': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Mobile Number'}), 
      'message': forms.Textarea(attrs={'class': 'form-control', "rows":"4",'placeholder': 'Message'}), 
    }