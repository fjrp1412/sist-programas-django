from django.shortcuts import render
from django.forms import formset_factory

import json
from datetime import date

from sells.forms import OrderForm, InvoiceForm
from sells.models import Sells
from products.models import Category

# Extra Functions
from users.models import Salesman


def clean_order_info(order):
    full_order = []
    for i in range(6):
        if order[f'form-{i}-product_name'] != '':
            full_order.append(
                {
                    "product_name" : order[f'form-{i}-product_name'],
                    "category" : order[f'form-{i}-category'],
                    "base_price": order[f'form-{i}-base_price'],
                    "quantity": order[f'form-{i}-quantity'],
                    "total_price": round(
                        float(order[f'form-{i}-base_price']) *
                        float( order[f'form-{i}-quantity'])
                        , 2)
                }
            )
    return full_order




# Create your views here.
def register_sell(request):
    invoice_id = Sells.objects.latest('invoice_id').pk + 1
    if request.method == "POST":
        data_dict = request.POST.dict()

        order_info = clean_order_info(data_dict)
        #print(request.POST)

        salesman = Salesman.objects.get(pk=int(data_dict['salesman']))
        customer = data_dict['customer']
        income = 0
        for order in order_info:
            income += order['total_price']
        products = json.dumps(order_info)

        s = Sells(
            invoice_id=invoice_id,
            id_category=Category.objects.get(pk=6),
            id_salesman=salesman,
            customer=customer,
            income=income,
            products=products,
            date = date.today()
        )

        s.save()
        print(s)


    order_form_set = formset_factory(OrderForm, extra=6)
    context = {'form': order_form_set(),
               'invoice_id': invoice_id,
               'form2': InvoiceForm
               }
    return render(
        request,
        template_name="sells/register_sales.html",
        context=context
    )
