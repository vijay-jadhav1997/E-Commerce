from django.shortcuts import render, redirect
from django.contrib import messages

from math import ceil

from .models import Product
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
    all_products = []
    catgories_of_product = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catgories_of_product}

    for category in categories:
      products = Product.objects.filter(category=category)
      n=len(products)
      nSlides = n // 4 + ceil((n/4) - (n // 4))
      all_products.append([products, range(1, nSlides), nSlides])

  return render(request, 'index.html', context={'form':form, 'products':all_products})

