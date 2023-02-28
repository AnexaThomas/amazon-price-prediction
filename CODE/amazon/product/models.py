from distutils.command.upload import upload
from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)

class feed(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    message=models.CharField(max_length=255)

class contac(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Phone=models.CharField(max_length=10)
    Message=models.CharField(max_length=255)



class mobilelist(models.Model):
    mobimg = models.ImageField(upload_to = 'mobiles')
    mobname = models.CharField(max_length= 255)
    mobprice = models.CharField(max_length=50)

    def __str__(self):
        return self.mobname

class brand(models.Model):
    brname = models.CharField(max_length=255)
    brimg = models.ImageField(upload_to = 'brands')

    def __str__(self):
        return self.brname

class PredResults(models.Model):

    Title=models.TextField()
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.Title