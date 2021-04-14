import matplotlib.pyplot as plt
import base64
from io import BytesIO

from sells.models import Sells
from users.models import Salesman

""" Work in the Data Visualization """


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


# All Sales
def all_sells_by_salesman(id_salesman):
    salesman = Salesman.objects.get(pk=id_salesman)

    sells = Sells.objects.filter(
        id_salesman__exact=salesman
    )

    x_data = [sell.invoice_id for sell in sells]
    y_data = [sell.income for sell in sells]

    plt.switch_backend('AGG')
    plt.figure(figsize=(5.2, 4.5))
    plt.title('Sales By Salesman')
    plt.plot(x_data, y_data)
    plt.ylabel("Income (USD)")
    plt.xlabel("Sales")
    plt.tight_layout()
    graph = get_graph()
    return graph


