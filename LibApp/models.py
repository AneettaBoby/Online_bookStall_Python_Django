from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    category_name=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=150,null=True,blank=True)
    Category_image=models.ImageField(upload_to="Category_image",null=True,blank=True)
class ProductDb(models.Model):
    Category=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Author = models.CharField(max_length=100, null=True, blank=True)
    Language= models.CharField(max_length=100, null=True, blank=True)
    Genre=models.CharField(max_length=100, null=True, blank=True)
    Publisher=models.CharField(max_length=100, null=True, blank=True)
    Publication_date=models.DateField(null=True,blank=True)
    Pages=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=150, null=True, blank=True)
    ProductImage=models.ImageField(upload_to="Product_Image",null=True,blank=True)
    status = models.CharField(max_length=7, default='pending')

    stock = models.IntegerField(default=1)

