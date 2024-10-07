from django.db import models

# Create your models here.
class Contact(models.Model):
  name= models.CharField(max_length=100)
  email= models.EmailField(max_length=100)
  phone_numb= models.CharField(max_length=10)
  message= models.TextField(max_length=1000)

  def __str__(self) -> str:
    return self.name


class Product(models.Model):
  product_name= models.CharField(max_length=100)
  category= models.CharField(max_length=100, default="")
  subcategory= models.CharField(max_length=50, default="")
  price= models.IntegerField(default=0)
  descreption= models.TextField(max_length=300, default="")
  image =  models.ImageField(upload_to='shop/images', default="")

  def __str__(self) -> str:
    return self.product_name

