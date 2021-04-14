from django import forms
from django.forms import ModelForm

from sells.models import Sells, Order
from users.models import Salesman


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = [
            'id',
            'product_name',
            'category',
            'base_price',
            'quantity',
        ]


class InvoiceForm(forms.Form):
    SALESMAN = []
    s_list = Salesman.objects.all()
    for s in s_list:
        SALESMAN.append((s.pk, s.name))



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


class SearchFilterForm(forms.Form):

    SALESMAN = [('-1', 'Todos')]
    s_list = Salesman.objects.all()
    for s in s_list:
        SALESMAN.append((s.pk,s.name))

    id_invoice = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'inputdata',
                'placeholder':'0'
            }
        ),
        required=False
    )

    customer = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'inputdata',
                'placeholder': 'Cliente'
            }
        ),
        required=False
    )

    salesman = forms.ChoiceField(
        help_text="Vendedor",
        choices=SALESMAN,
        widget=forms.Select(
            attrs={
                'class':'inputdata',
            }
        ),
        required=False
    )

    date   = forms.DateField(required=False)