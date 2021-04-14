import matplotlib.pyplot as plt
from sells.models import Sells
from users.models import Salesman

""" Work in the Data Visualization """


# All Sales
def all_sells_by_salesman(id_salesman):
    data = []
    salesman = Salesman.objects.get(pk=id_salesman)
    sells = Sells.objects.filter(
        id_salesman__exact=salesman
    )
    for sell in sells:
        data.append(sell.income)
    print(data)
    plt.plot(data)
    plt.ylabel("Income (USD)")
    plt.xlabel("Sales")
    plt.savefig(f'media/plots/sellsBy{salesman.name}.png')
    plt.show()
    plt.close()