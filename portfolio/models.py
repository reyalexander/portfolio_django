from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Portfolio(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', max_length=255, null=True) #(que puede ser una URL)
    title = models.CharField(max_length=50) # Project Title
    description = models.TextField(max_length=500) # Project Description
    tags = models.CharField(max_length=100) # HTML, CSS, PYTHON, etc
    url = models.CharField(max_length=200) # URL de github
    
    def __str__(self):
        return self.title + ' - ' + self.url


class IpAddress(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models. GenericIPAddressField()