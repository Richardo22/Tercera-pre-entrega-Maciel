from django.db import models

# Create your models here.
class Empanada(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50)
    precio=models.IntegerField()

