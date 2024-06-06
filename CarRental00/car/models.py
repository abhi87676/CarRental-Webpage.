from django.db import models

class contacts(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=30, blank=True)
    email = models.CharField(max_length=100)

    # car/models.py

from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=30, blank=True)
    
    

from django.db import models

class Login(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)  # Assuming you're using Django's built-in authentication system
    # Add other fields as needed

from django.db import models

class CarSignup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields as needed

    def _str_(self):
        return self.name


    

    # Add more fields as needed

# Create your models here.