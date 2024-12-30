from django.db import models

# Create your models here.
class Student(models.Model):  
    uname = models.CharField(max_length=20)  
    fname = models.CharField(max_length=30)  
    lname = models.CharField(max_length=30)  
    mob = models.CharField(max_length=10)  
    email = models.EmailField()  
	