from django.urls import path

from apps.authentication.api.http.v1.login import UserLoginByPasswordView
from apps.authentication.api.http.v1.register import RegisterView


urlpatterns = [
    path("login-by-password/", UserLoginByPasswordView.as_view()),
    path("register/", RegisterView.as_view()),
]
