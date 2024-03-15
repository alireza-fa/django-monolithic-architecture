from django.contrib.auth import get_user_model

from rest_framework import serializers, status
from rest_framework.views import APIView

from apps.api import response_code
from apps.api.response import base_response, base_response_with_error, base_response_with_validation_error
from apps.authentication.services.register import register_user

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("username", "email", "password")


class RegisterView(APIView):
    serializer_class = RegisterSerializer

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
