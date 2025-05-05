from django.urls import path
from user.views import *

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("account/", AccountView.as_view(), name="account"),
    path("logout/", LogoutView.as_view(), name="logout")
]