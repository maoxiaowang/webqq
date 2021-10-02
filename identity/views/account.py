from django.contrib.auth import (
    login as auth_login,
)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms.mixin import JsonFormMixin
from common.forms.utils import PrettyErrorList
from identity.forms.account import RegisterForm, LoginForm
from identity.models import User


class Register(JsonFormMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'identity/account/register.html'
    success_url = reverse_lazy('identity:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['error_class'] = PrettyErrorList
        return kwargs


class Login(JsonFormMixin, LoginView):
    template_name = 'identity/account/login.html'
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return self.json_to_response()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['error_class'] = PrettyErrorList
        return kwargs
