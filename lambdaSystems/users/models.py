from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Base class for User and Admin classes."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification_card = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User = {self.user.username}, Cedula= {self.identification_card}"


class Admin(Profile):
    """Model for user Admin, is a proxy class
    because this class not require any extra data."""

    class Meta:
        proxy = True


class Salesman(models.Model):
    """Model for seller model, this class is a 1to1 field
    cause require extra info"""

    seller = models.OneToOneField(Profile, on_delete=models.CASCADE)
    count_sells = models.IntegerField()
    earnings = models.DecimalField(max_digits=10, decimal_places=2)
