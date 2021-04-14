from django.urls import path

from sells import views

urlpatterns = [

    path(
        route='register/',
        view=views.register_sell,
        name='register'
    ),

    path(
        route='search/',
        view=views.SearchSellsView.as_view(),
        name='search'
    ),

    path(
        route='detail/<int:pk>/',
        view=views.SellDetailView.as_view(),
        name='detail'
    ),

    path(
        route='salesman/<int:pk>/',
        view=views.SellsBySalesman.as_view(),
        name='salesman'
    )
]