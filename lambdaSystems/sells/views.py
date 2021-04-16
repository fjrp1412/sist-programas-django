import decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.forms import formset_factory
from django.views.generic import DetailView, ListView

import json
from datetime import date

from sells.forms import OrderForm, InvoiceForm, SearchFilterForm
from sells.models import Sells
from products.models import Category
from users.models import Salesman


# Extra Function
def clean_order_info(order):
    full_order = []
    for i in range(6):
        if order[f'form-{i}-product_name'] != '':
            full_order.append(
                {
                    "product_name": order[f'form-{i}-product_name'],
                    "category": order[f'form-{i}-category'],
                    "base_price": order[f'form-{i}-base_price'],
                    "quantity": order[f'form-{i}-quantity'],
                    "total_price": round(
                        float(order[f'form-{i}-base_price']) *
                        float(order[f'form-{i}-quantity']), 2)
                }
            )
    return full_order


# Create your views here.
def register_sell(request):
    try:
        invoice_id = Sells.objects.latest('invoice_id').pk + 1
    except:
        invoice_id = 1

    if request.method == "POST":
        # Clean the data in the Sell and calculate what is needed
        data_dict = request.POST.dict()
        order_info = clean_order_info(data_dict)
        if order_info:
            salesman = Salesman.objects.get(pk=int(data_dict['salesman']))
            customer = data_dict['customer']
            income = 0
            for order in order_info:
                income += order['total_price']
            products = json.dumps(order_info)

            # Create and save the Sell Instance
            s = Sells(
                invoice_id=invoice_id,
                id_category=Category.objects.get(pk=1),
                id_salesman=salesman,
                customer=customer,
                income=income,
                products=products,
                date=date.today()
            )
            s.save()

            # Update Salesman Data
            salesman.count_sells += 1
            salesman.earnings += decimal.Decimal(s.income)
            salesman.save()

            # Redirect to the invoice detail
            return redirect(f"/sells/detail/{invoice_id}/")

    # Add the forms to add products orders
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


class SellDetailView(LoginRequiredMixin, DetailView):
    # See the Detail of a Sell

    template_name = 'sells/info_sales.html'

    # In which base will be the QuerySet made and sent by the URL
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    model = Sells
    queryset = Sells.objects.all()

    context_object_name = 'invoice_id'

    def get_context_data(self, **kwargs):
        #        Add the invoice data to the detail
        context = super().get_context_data(**kwargs)

        context['salesman'] = context['object'].id_salesman.name
        context['invoice_id'] = context['object'].invoice_id
        context['customer'] = context['object'].customer
        context['date'] = context['object'].date
        context['products'] = json.loads(context['object'].products)
        context['income'] = context['object'].income

        return context


class SearchSellsView(LoginRequiredMixin, ListView):
    # List Invoice as needed.
    template_name = "sells/search_sales.html"
    model = Sells
    ordering = ('-invoice_id')
    context_object_name = 'sells'

    def get_context_data(self, **kwargs):
        # Add the filter form into the Context
        context = super().get_context_data(**kwargs)
        context['form'] = SearchFilterForm
        return context

    def get_queryset(self, **kwargs):
        #        In This Function I Filter the Sells List in case is needed
        query_set = Sells.objects.all()
        info_get = dict(self.request.GET)

        try:
            if info_get['salesman'][0] != '-1':
                # Filter Salesman (Is a Salesman Object, search by PK)
                query_set = query_set.filter(
                    id_salesman__exact=Salesman.objects.get(
                        pk=int(info_get['salesman'][0])
                    )
                )

            if info_get['customer'][0] != '':
                # Filter By Customer (Is a String)
                query_set = query_set.filter(
                    customer__contains=info_get['customer'][0]
                )

            if info_get['invoice'] != '':
                # Search by Invoice ID
                # if contains one number of the id is Indexed in list
                query_set = query_set.filter(
                    invoice_id__contains=info_get['invoice'][0]
                )

        except:
            # If the Filter Form is not in the GET request
            pass

        return query_set
