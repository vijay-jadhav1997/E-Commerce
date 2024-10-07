from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm

# Create your views here.
def home_view(request):
  if request.method == "POST":
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "Successful...!")
      return redirect('home')
    else:
      return render(request, 'index.html', context={'form':form})
  else:
    form= ContactForm()
  return render(request, 'index.html', context={'form':form})