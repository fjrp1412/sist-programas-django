from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView


class SingupView(FormView):
    template_name = "singup.html"
    form_class = None
    success_url = ""