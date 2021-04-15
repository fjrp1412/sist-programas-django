from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import DetailView, ListView
from users.forms import SignupForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from users.models import Salesman
from django.urls import reverse
import users.utils as utils


class Signup(View):
    """View for signup a new user."""
    template_name = 'users/html/register_admin.html'

    def get(self, request):
        form = SignupForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form}
        )

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form})


class LoginView(auth_views.LoginView):
    """View for login session."""
    template_name = 'users/html/log_in.html'


class HomeView(ListView, LoginRequiredMixin):
    """View for home page."""
    template_name = 'users/html/index.html'
    model = Salesman
    ordering = ('seller_id',)
    context_object_name = 'salesmans'


class UpdateSalesman(UpdateView, LoginRequiredMixin):
    """View for update a salesman user"""
    model = Salesman
    template_name = 'users/html/update_salesman.html'
    fields = ['name', 'identification_document', 'picture']

    def get_object(self, queryset=None):
        return self.request.user.salesman

    def get_success_url(self):
        return reverse('users:home')


class DetailSalesmanSells(DetailView, LoginRequiredMixin):
    template_name = "users/html/info_salesman.html"

    # In which base will be the QuerySet made and sent by the URL
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    model = Salesman
    queryset = Salesman.objects.all()

    context_object_name = 'salesman'

    def get_context_data(self, **kwargs):
        # Add the invoice data to the detail
        context = super().get_context_data(**kwargs)
        context['plot'] = utils.all_sells_by_salesman(context['salesman'].pk)

        return context


class DetailSalesmanAccumulated(DetailView, LoginRequiredMixin):
    template_name = "users/html/info_salesman.html"

    # In which base will be the QuerySet made and sent by the URL
    slug_field = 'pk'
    slug_url_kwarg = 'pk'

    model = Salesman
    queryset = Salesman.objects.all()

    context_object_name = 'salesman'

    def get_context_data(self, **kwargs):
        # Add the invoice data to the detail
        context = super().get_context_data(**kwargs)

        context['plot'] = utils.accumulated_by_salesman(context['salesman'].pk)

        return context
