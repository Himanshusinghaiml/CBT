from django.db import models

from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class contact_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    organization = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name


