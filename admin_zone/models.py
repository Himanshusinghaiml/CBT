from django.db import models

class addnewCenterlist(models.Model):
    center_code = models.CharField(max_length=10, unique=True)
    center_name = models.CharField(max_length=255)
    state = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=100)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.center_name
    
    
