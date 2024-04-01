from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.views import APIView

from apps.api import response_code
from apps.api.response import base_response_with_error, base_response, base_response_with_validation_error
from apps.authentication.v1.services.sign_user import register_user, login_by_password
from apps.authentication.v1.serializers.sign_user import RegisterSerializer, \
    UserLoginByPasswordSerializer, AuthenticatedResponseSerializer


SCHEMA_TAGS = ("Auth",)


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    @extend_schema(request=RegisterSerializer, responses=AuthenticatedResponseSerializer, tags=SCHEMA_TAGS)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                vd = serializer.validated_data
                token = register_user(request=request, username=vd["username"],
                                      email=vd["email"], password=vd["password"])
            except:
                return base_response_with_error(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                                code=response_code.INTERNAL_SERVER_ERROR)

            return base_response(status_code=status.HTTP_201_CREATED, code=response_code.CREATED, result=token)

        return base_response_with_validation_error(error=serializer.errors)


class UserLoginByPasswordView(APIView):
    serializer_class = UserLoginByPasswordSerializer

    @extend_schema(request=UserLoginByPasswordSerializer, responses=AuthenticatedResponseSerializer, tags=SCHEMA_TAGS)
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
