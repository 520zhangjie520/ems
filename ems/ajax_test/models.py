from django.db import models

# Create your models here.
class Ajax_user(models.Model):
    name=models.CharField(max_length=20)
    password=models.IntegerField()
    class Meta:
        db_table='Ajax_user'