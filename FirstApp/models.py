from django.db import models


# Create your models here.

class Product(models.Model):
    itemid = models.CharField(unique=True, max_length=50)
    ItemName = models.CharField(null=False, blank=False, max_length=100)
    Price = models.IntegerField(null=False, blank=False)
    Availability = models.BooleanField(default=True)
