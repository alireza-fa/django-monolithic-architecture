from django.urls import path, include

from apps.authentication.api.http.v1 import login


urlpatterns = [
    path("login-by-password/", login.UserLoginByPasswordView.as_view()),
]
