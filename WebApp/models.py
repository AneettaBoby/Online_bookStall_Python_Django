from django.db import models
from django.utils.text import slugify
import uuid

from LibApp.models import ProductDb
from WebApp.utils import generate_unique_slug


# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)


class Product(models.Model):
    STATUS_CHOICES = [
        ('approve', 'Approve'),
        ('reject', 'Reject'),
    ]
    Category=models.CharField(max_length=255)
    ProductName = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Language = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=255)
    Publication_date = models.DateField()
    Pages = models.PositiveIntegerField()
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    ProductImage = models.ImageField(upload_to='product_images/')
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='approve')

    def __str__(self):
        return self.ProductName

    # stock= models.IntegerField(default=1)



class Register_db(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Confirm_password=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)



class CartDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    TotalPrice=models.IntegerField(null=True,blank=True)
    Product_Id = models.IntegerField(null=True, blank=True)

class WishlList(models.Model):
    Product_Id=models.IntegerField(null=True,blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)

class Review_Db(models.Model):
    Product_Id = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    Comment=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,blank=True,null=True)
    Rating=models.IntegerField(null=True,blank=True)

class CheckoutDb(models.Model):
    Name=models.CharField(max_length=100, blank=True, null=True)
    Email = models.EmailField(max_length=100, blank=True, null=True)
    Address= models.EmailField(max_length=100, blank=True, null=True)
    Phone=models.IntegerField(null=True,blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
