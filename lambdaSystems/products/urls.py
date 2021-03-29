from django.urls import path

from products import views

urlpatterns = [

    path(
        route='new/',
        view=views.CreateProductView.as_view(),
        name='newproduct'
    ),
]