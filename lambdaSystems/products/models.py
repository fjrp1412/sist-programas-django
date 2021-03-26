from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.id}:{self.name}'


class Products(models.Model):
    """Contains all relevant information about products"""

    id_product = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=120)

    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE)
    price = models.FloatField()
    brand = models.CharField(max_length=120)

    def __str__(self):
        return f" {self.name} by {self.brand}, category: {self.category} price: ${self.price} "
