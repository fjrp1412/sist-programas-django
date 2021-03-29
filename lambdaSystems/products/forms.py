from django.forms import ModelForm

from products.models import Products


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('id_product', 'name', 'category', 'price', 'brand',)
