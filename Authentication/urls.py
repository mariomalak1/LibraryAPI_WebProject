from django.urls import path, include
from django.contrib.auth.views import auth_logout

from . import views

urlpatterns = [
    path("login/", views.UserAuthentication.login, name="signin"),
    path("signup/", views.UserAuthentication.signup, name="signup"),
    path("logout/", views.UserAuthentication.logout, name="logout"),
    path("check_token/", views.UserAuthentication.token_check_found, name="check_token"),
]