from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserLoginView(LoginView):
    template_name = "login.html"

class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = "registration.html"

class AccountView(DetailView):
    model = User
    template_name = "account.html"

class UserLogoutView(LogoutView):
    pass