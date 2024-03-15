from django.conf import settings

from rest_framework_simplejwt.tokens import Token

from apps.pkg.encrypto.encryption import encrypt

refresh_token_claims = {
    "ip_address": "",
    "device_name": "",
    "user_id": 0,
}

access_token_claims = {
    "ip_address": "",
    "device_name": "",
    "user_id": 0,
    "username": "",
    "email": "",
}


def encrypt_token(token: Token) -> str:
    return encrypt(data=str(token), key=settings.ENCRYPT_KEY)
