from typing import Dict

from django.http import HttpRequest
from django.contrib.auth import get_user_model

from apps.authentication.services.token import get_refresh_token_claims, get_access_token_claims, encrypt_token
from apps.pkg.token.token import generate_refresh_token_with_claims, generate_access_token_with_claims
from apps.utils import client

User = get_user_model()


def register_user(request: HttpRequest, username: str, email: str, password: str) -> Dict:
    user = User.objects.create_user(username=username, email=email, password=password)

    client_info = client.get_client_info(request=request)

    refresh_token = generate_refresh_token_with_claims(
        claims=get_refresh_token_claims(**client_info, user_id=user.id), encrypt_func=encrypt_token)

    access_token = generate_access_token_with_claims(
        claims=get_access_token_claims(**client_info, user_id=user.id, username=username, email=user.email),
        encrypt_func=encrypt_token)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
