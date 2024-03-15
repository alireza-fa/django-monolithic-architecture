from django.urls import path, include

from apps.authentication.api.http.v1 import login
from apps.authentication.api.http.v1 import register


urlpatterns = [
    path("login-by-password/", login.UserLoginByPasswordView.as_view()),
    path("register/", register.RegisterView.as_view()),
]
