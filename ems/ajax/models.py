from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.FloatField()
    brithday=models.DateTimeField()

