from django.contrib import admin

# Register your models here.
from sells.models import Sells


class SellsAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'id_salesman', 'income', 'id_category', 'date', 'description', 'products')


admin.site.register(Sells, SellsAdmin)
