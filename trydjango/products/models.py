from pydoc import describe
from statistics import mode
from django.db import models

# Create your models here.

class Product(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(blank=True, null=True) # blank -> required field; null -> database
  price = models.DecimalField(decimal_places=2, max_digits=10000)
  summary = models.TextField(blank=False, null=False) #default='test'
  featured = models.BooleanField(default=False) #default not provided here