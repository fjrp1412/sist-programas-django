# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Forms
from products.forms import ProductForm


class CreateProductView(LoginRequiredMixin, CreateView):
    """Create a Product using the ProductForm"""
    template_name = "products/create_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("admin")
