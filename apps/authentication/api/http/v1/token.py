from rest_framework import serializers, status
from rest_framework.views import APIView

from apps.api import response_code
from apps.api.response import base_response_with_error, base_response, base_response_with_validation_error
from apps.authentication.services.token import verify_token


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class VerifyTokenView(APIView):
    serializer_class = TokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token_verified = verify_token(request=request, token=serializer.validated_data["token"])

            if not token_verified:
                return base_response_with_error(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                                code=response_code.INVALID_TOKEN)

            return base_response(status_code=status.HTTP_200_OK, code=response_code.OK)

        return base_response_with_validation_error(error=serializer.errors)


class RefreshAccessToken(APIView):
    pass


class BlockRefreshToken(APIView):
    pass
