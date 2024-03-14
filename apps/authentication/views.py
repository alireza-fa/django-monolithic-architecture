from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import Token

from apps.pkg.token.token import generate_refresh_token_with_claims, validate_token


def access_validate(token: Token):
    if token["token_type"] == "access":
        print("access")
    print("refresh")


class Test(APIView):

    def get(self, request):
        # generate_refresh_token_with_claims(claims={"user_id": 1})
        validate_token(string_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6M"
                                    "TcxMzEyOTE4MCwiaWF0IjoxNzEwNDUwNzgwLCJqdGkiOiJlOTE1NDQwZTE4N2M0OTY2OWI3YmExYjU"
                                    "wOWIxNmE4NyIsInVzZXJfaWQiOjF9.Y0LuRp59H6sXOouQTOPN8bIYp9-5BnTfXXB2I5ob6Pg",
                       func=access_validate)

        return Response(status=200)
