from django.urls import path
from users import views

urlpatterns = [
    path(
        route='signup/',
        view=views.Signup.as_view(),
        name='signup'
    )
]
