from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status

from apps.api import response_code
from apps.api.response import base_response_with_validation_error, base_response_with_error, base_response
from apps.authentication.services.login import login_by_password
from ..common.serializers import AuthenticatedResponseSerializer


User = get_user_model()


class UserLoginByPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=64)
    password = serializers.CharField(min_length=8, max_length=128)


class UserLoginByPasswordView(APIView):
    serializer_class = UserLoginByPasswordSerializer

    @extend_schema(request=UserLoginByPasswordSerializer, responses=AuthenticatedResponseSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                token = login_by_password(request=request, username=serializer.validated_data["username"],
                                          password=serializer.validated_data["password"])
            except ValueError:
                return base_response_with_error(status_code=status.HTTP_404_NOT_FOUND,
                                                code=response_code.USER_NOT_FOUND)

            return base_response(status_code=status.HTTP_200_OK, code=response_code.OK, result=token)

        return base_response_with_validation_error(error=serializer.errors)
