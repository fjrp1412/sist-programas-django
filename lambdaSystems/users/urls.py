from django.urls import path
from users import views

urlpatterns = [
    path(
        route='signup/',
        view=views.Signup.as_view(),
        name='signup'
    ),

    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    path(
        route='home/',
        view=views.HomeView.as_view(),
        name='home'
    ),

    path(
        route='update/',
        view=views.UpdateSalesman.as_view(),
        name='update'
    ),

    path(
        route='detail/<int:pk>/0/',
        view=views.DetailSalesmanSells.as_view(),
        name='salesman_sells'
    ),

    path(
        route='detail/<int:pk>/1/',
        view=views.DetailSalesmanAccumulated.as_view(),
        name='salesman_accumulated'
    )

]
