from django import forms
from django.forms import ModelForm

from sells.models import Sells

class RegisterSellForm(ModelForm):
    class Meta:
        model = Sells
        fields = ['id_salesman', 'income', 'id_category',
                  'date', 'description', 'products']

