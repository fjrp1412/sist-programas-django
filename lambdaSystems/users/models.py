from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """Base class for User and Admin classes."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user_id = models.AutoField(primary_key=True, unique=True)
    identification_card = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User = {self.user.username}, Cédula= {self.identification_card}"


class Admin(models.Model):
    """Model for user Admin, is a proxy class
    because this class not require any extra data."""
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    admin_id = models.AutoField(primary_key=True, unique=True, default=0)


class Salesman(models.Model):
    """Model for seller model, this class is a 1to1 field
    cause require extra info"""

    seller = models.OneToOneField(Profile, on_delete=models.CASCADE)
    count_sells = models.IntegerField()
    earnings = models.DecimalField(max_digits=10, decimal_places=2)
    #seller_id = models.AutoField(primary_key=True, unique=True)
