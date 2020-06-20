from django.db import models
from datetime import date

class Ionic(models.Model):
    
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    documento = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fecha = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
