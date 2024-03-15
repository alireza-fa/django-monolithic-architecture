from django.urls import path

from apps.authentication.api.http.v1.login import UserLoginByPasswordView
from apps.authentication.api.http.v1.register import RegisterView
from apps.authentication.api.http.v1.token import VerifyTokenView


urlpatterns = [
    # login
    path("login-by-password/", UserLoginByPasswordView.as_view()),
    # register
    path("register/", RegisterView.as_view()),
    # token
    path("token/verify/", VerifyTokenView.as_view()),
]
