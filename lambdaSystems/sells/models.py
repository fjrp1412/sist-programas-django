from django.db import models as m


# Create your models here.

class Sells(m.Model):
    """
    Sells and invoice Model
    Contains multiple Foreign Keys. Such as:
        - id_salesman
        - id_category

    Also contains a JSON with Products FK and quantity.
    """
    invoice_id = m.AutoField(unique=True, primary_key=True, auto_created=True)

    id_salesman = m.ForeignKey('users.Salesman',
                               on_delete=m.CASCADE,
                               default=0)

    customer = m.CharField(max_length=20, default="None")

    income = m.DecimalField(max_digits=10, decimal_places=2)

    id_category = m.ForeignKey('products.Category',
                               on_delete=m.CASCADE)

    date = m.DateTimeField(auto_now_add=True)

    # Note on bill
    description = m.CharField(max_length=120, blank=True)

    # JSON MUST CONTAIN ProductID and Quantity
    products = m.JSONField()

    def __str__(self):
        return f"Invoice Number: {self.invoice_id}, date: {self.date}, salesman: {self.id_salesman}, \nproducts:" \
               f" {self.products},\ndescription: {self.description}  "


class Order(m.Model):
    """
    Line with product info in Sell
        - Product Name
        - Category
        - Base Price
        - Quantity
        - Total Price
    """

    id = m.AutoField(unique=True, primary_key=True, auto_created=True)
    product_name = m.CharField(max_length=20)
    category = m.CharField(max_length=20)
    base_price = m.DecimalField(max_digits=10, decimal_places=2)
    quantity = m.DecimalField(max_digits=10, decimal_places=2)
    total_price = m.DecimalField(max_digits=10, decimal_places=2)
