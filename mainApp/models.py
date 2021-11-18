from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name
    
    class Meta: 
        verbose_name_plural = 'ciudades'

# verbose name plural is a human readable name you give to the objects