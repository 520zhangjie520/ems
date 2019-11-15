from django.db import models

# Create your models here.
class User1(models.Model):
    username = models.CharField(max_length=20,unique=True)
    name =models.CharField (max_length=20 )
    password = models.CharField(max_length=20)
    sex=models.CharField(max_length=20 )
class news1(models.Model):
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    age = models.SmallIntegerField()
    headpic = models.ImageField(upload_to="static")
