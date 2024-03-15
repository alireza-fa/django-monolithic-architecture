from typing import Dict

from django.conf import settings

from rest_framework_simplejwt.tokens import Token

from apps.pkg.encrypto.encryption import encrypt

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
