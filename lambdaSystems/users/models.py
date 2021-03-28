from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Model base for Admin and Salesman."""
    name = models.CharField(max_length=120)
    identifacion_document = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Admin(Profile):
    """Model for admin user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Salesman(Profile):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    count_sells = models.IntegerField()
    earnings = models.DecimalField(max_digits=10, decimal_places=2)
