from pyexpat import model
from django.db import models

# Create your models here.
class Decedent(models.Model):
    name = models.CharField(max_length=100)
    address_code = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    