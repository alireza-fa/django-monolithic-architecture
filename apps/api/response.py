from typing import Dict

from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.status import HTTP_400_BAD_REQUEST

from apps.api.response_code import ERROR_TRANSLATION, BAD_REQUEST


def base_response(*, status_code: int, code: int, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "code": code}, status=status_code)


def base_response_with_error(*, status_code: int, code: int, error: str | None = None) -> Response:
    if error:
        return Response(data={"code": code, "error": error}, status=status_code)
    return Response(data={"code": code, "error": ERROR_TRANSLATION[code]}, status=status_code)


def base_response_with_validation_error(*, error: ValidationError, status_code: int = HTTP_400_BAD_REQUEST, code: int = BAD_REQUEST) -> Response:
    return Response(data={"code": code, "error": error}, status=status_code)
