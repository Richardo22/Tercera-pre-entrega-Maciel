from django.db import models

# Create your models here.
class Empanada(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.ingredientes} - {self.precio}"

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.ingredientes} - {self.precio}"   

class Pizza(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=50)
    precio=models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.ingredientes} - {self.precio}"

