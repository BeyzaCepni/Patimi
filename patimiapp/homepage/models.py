from django.db import models

# Create your models here.
class Ilan(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=50)
    description = models.TextField()
    ilce = models.CharField(max_length=20)
    sehir = models.CharField(max_length=20)
    tarih = models.models.DateField()
    is_active = models.models.BooleanField()  
