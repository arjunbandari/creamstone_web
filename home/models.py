from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=22)
    email =models.CharField(max_length=22)
    address=models.CharField(max_length=22)
    phone=models.CharField(max_length=22)
    reason=models.TextField()
    date=models.DateField()

class payment(models.Model):
    name=models.CharField(max_length=22)
    order=models.CharField(max_length=22)
    no=models.CharField(max_length=22)
    date=models.DateField()
 

