from django.urls import path

from sells import views

urlpatterns = [

    path(
        route='register/',
        view=views.register_sell,
        name='register'
    ),

]