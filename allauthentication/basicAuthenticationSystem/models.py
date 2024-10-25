from django.db import models

# Create your models here.
class MyDetails(models.Model):
    fullName = models.CharField(max_length=100)
    age = models.IntegerField(max_length=40)
    