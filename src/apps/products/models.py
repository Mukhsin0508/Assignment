import string
import random

from django.core.validators import MinValueValidator
from django.db import models



def generate_id():
    """ Generate unique id for the product """
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=8))


class Product(models.Model):
    name = models.CharField(max_length=55)
    code = models.SlugField(unique = True, default=generate_id)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name



class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product-name")
    material = models.ForeignKey('materials.Material', on_delete = models.PROTECT,
                                 related_name = "meterial-name"),
    quantity = models.FloatField (default = 0 , validators = [MinValueValidator(0)])


    class Meta:
        verbose_name = "Product Material"
        verbose_name_plural = "Product Materials"

    def __str__(self):
        return f"{self.product.name} - {self.material.name}"






