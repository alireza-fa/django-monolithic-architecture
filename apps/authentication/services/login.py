from typing import Dict

from django.contrib.auth import get_user_model
from django.http import HttpRequest

from apps.pkg.token.token import generate_refresh_token_with_claims, generate_access_token_with_claims
from apps.utils.client import get_client_info
from apps.authentication.services.token import access_token_claims, refresh_token_claims, encrypt_token

User = get_user_model()


def login_by_password(request: HttpRequest, username: str, password: str) -> Dict:
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist as err:
        raise ValueError(err)

    if not user.check_password(password):
        raise ValueError("user does not exist")

    claims = {
        **get_client_info(request=request),
        "user_id": user.id
    }

    refresh_token = generate_refresh_token_with_claims(claims=claims, encrypt_func=encrypt_token)

    claims["username"] = username
    claims["email"] = user.email
    access_token = generate_access_token_with_claims(claims={"user_id": user.id, "username": username},
                                                     encrypt_func=encrypt_token)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }
