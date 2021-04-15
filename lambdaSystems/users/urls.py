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
        route='update/<int:pk>/',
        view=views.UpdateSalesman.as_view(),
        name='update'
    )

]
