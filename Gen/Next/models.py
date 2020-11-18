from django.db import models

# Create your models here.
class Banner(models.Model): 
    name = models.CharField(max_length=50)
    banner_image = models.ImageField(upload_to='images/')