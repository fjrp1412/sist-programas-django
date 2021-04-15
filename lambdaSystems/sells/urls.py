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
        view=views.DetailView.as_view(),
        name='detail'
    ),

]
