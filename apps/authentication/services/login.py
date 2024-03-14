from typing import Dict

from django.contrib.auth import get_user_model
from apps.pkg.token.token import generate_refresh_token_with_claims, generate_access_token_with_claims


User = get_user_model()


def login_by_password(username: str, password: str) -> Dict:
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist as err:
        raise ValueError(err)

    if not user.check_password(password):
        raise ValueError("user does not exist")

    refresh_token = generate_refresh_token_with_claims(claims={"user_id": user.id})
    access_token = generate_access_token_with_claims(claims={"user_id": user.id, "username": username})

    return {
        "access_token": str(access_token),
        "refresh_token": str(refresh_token),
    }
