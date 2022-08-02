from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    dateOfBirth=models.DateField()
    gender=models.CharField(max_length=20)
    height=models.CharField(max_length=20)
    weight=models.CharField(max_length=20)
    


