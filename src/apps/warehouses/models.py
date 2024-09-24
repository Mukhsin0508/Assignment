from django.db import models

class Warehouse(models.Model):
    material = models.CharField(max_length = 200)
    remainder = models.PositiveIntegerField()
    price = models.DecimalField(max_digits = 7, decimal_places = 2)




