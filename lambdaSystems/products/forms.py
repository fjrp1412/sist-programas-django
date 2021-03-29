from django.forms import ModelForm

from products.models import Products, Category


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('id_product', 'name', 'category', 'price', 'brand',)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('id', 'name',)