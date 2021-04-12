from django import forms
from django.forms import ModelForm

from sells.models import Sells, Order
from users.models import Salesman

class RegisterSellForm(ModelForm):
    class Meta:
        model = Sells
        fields = [
            'id_salesman',
            'income',
            'id_category',
            #'date',
            'description',
            'products'
        ]


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'id',
            'product_name',
            'category',
            'base_price',
            'quantity',
            #'total_price'
        ]


class InvoiceForm(forms.Form):
    SALESMAN = []
    s_list = Salesman.objects.all()
    for s in s_list:
        SALESMAN.append((s.pk,s.name))



    # id_invoice = forms.IntegerField()
    salesman = forms.ChoiceField(
        help_text="Vendedor",
        choices=SALESMAN,
        widget=forms.Select(
            attrs={
                'class':'inputdata',
            }
        )
    )

    customer   = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'inputdata',
                'placeholder': 'Cliente'
            }
        )
    )
