from django.urls import path

from products import views

urlpatterns = [

    path(
        route='new/',
        view=views.CreateProductView.as_view(),
        name='newproduct'
    ),

    path(
        route='new/category/',
        view=views.CreateCategoryView.as_view(),
        name='newcategory'
    ),
]