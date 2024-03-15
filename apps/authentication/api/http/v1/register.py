from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.views import APIView

from apps.api.response import base_response, base_response_with_error, base_response_with_validation_error

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
            pass

        return base_response_with_validation_error(error=serializer.errors)
