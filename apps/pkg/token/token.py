from typing import Dict

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, Token, UntypedToken, TokenError


def set_token_claims(*, token: Token, claims: Dict):
    for key, value in claims.items():
        token[key] = value


def generate_refresh_token_with_claims(*, claims: Dict) -> Token:
    refresh_token = RefreshToken()

    set_token_claims(token=refresh_token, claims=claims)

    return refresh_token


def generate_access_token_with_claims(*, claims: Dict) -> Token:
    access_token = AccessToken()

    set_token_claims(token=access_token, claims=claims)

    return access_token


def function(token: Token):
    pass


def validate_token(string_token: str, func: function or None = None) -> Token:
    try:
        token = UntypedToken(token=string_token)
    except TokenError as err:
        raise ValueError(err)

    if func:
        func(token=token)

    return token


def get_token_claims(*, string_token: str, claims: Dict):
    token = validate_token(string_token=string_token)

    for key in claims:
        claims[key] = token[key]
