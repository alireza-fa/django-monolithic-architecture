from typing import Dict

from django.conf import settings
from django.http import HttpRequest

from rest_framework_simplejwt.tokens import Token

from apps.pkg.encrypto.encryption import encrypt, decrypt
from apps.pkg.token.token import validate_token
from apps.utils import client

IP_ADDRESS = "ip_address"
DEVICE_NAME = "device_name"
USER_ID = "user_id"
USERNAME = "username"
EMAIL = "email"

refresh_token_claims = {
    IP_ADDRESS: "",
    DEVICE_NAME: "",
    USER_ID: 0,
}

access_token_claims = {
    IP_ADDRESS: "",
    DEVICE_NAME: "",
    USER_ID: 0,
    USERNAME: "",
    EMAIL: "",
}


def get_refresh_token_claims(*, ip_address: str, device_name: str, user_id: int) -> Dict:
    return {
        IP_ADDRESS: ip_address,
        DEVICE_NAME: device_name,
        USER_ID: user_id,
    }


def get_access_token_claims(*, ip_address: str, device_name: str, user_id: int, username: str, email: str) -> Dict:
    return {
        IP_ADDRESS: ip_address,
        DEVICE_NAME: device_name,
        USER_ID: user_id,
        USERNAME: username,
        EMAIL: email,
    }


def encrypt_token(token: Token) -> str:
    return encrypt(data=str(token), key=settings.ENCRYPT_KEY)


def verify_token(*, request: HttpRequest, token: str) -> bool:
    try:
        token_string = decrypt(encrypted=token.encode(), key=settings.ENCRYPT_KEY)
        token = validate_token(string_token=token_string)
    except ValueError:
        return False

    client_info = client.get_client_info(request=request)
    if token[DEVICE_NAME] != client_info[client.DEVICE_NAME]:
        return False

    return True
