from django.urls import path

from apps.authentication.v1.views import token
from apps.authentication.v1.views import sign_user

app_name = "api_v1"

urlpatterns = [
    # login
    path("login-by-password/", sign_user.UserLoginByPasswordView.as_view()),
    # register
    path("register/", sign_user.RegisterView.as_view()),
    # token
    path("token/verify/", token.VerifyTokenView.as_view()),
    path("token/refresh/", token.RefreshAccessToken.as_view()),
]
