from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from users.forms import SignupForm
from django.contrib.auth import views as auth_views


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


class HomeView(View):
    """View for home page."""
    template_name = 'users/html/index.html'

    def get(self, request):
        return render(
            request=request,
            template_name=self.template_name,
        )

    def post(self, request):
        return render(
            request=request,
            template_name=self.template_name,
        )
