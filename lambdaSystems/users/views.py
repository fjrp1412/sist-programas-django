from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView
from django.views import View
from users.forms import SignupForm


class Signup(View):
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
            return render(
                request=request,
                template_name=self.template_name,
                context={'form': form})

        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form})
