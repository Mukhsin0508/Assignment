from django.db import models

class Material(models.Model):
    name = models.CharField(max_length = 55)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.name


