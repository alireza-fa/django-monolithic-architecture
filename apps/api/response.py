from typing import Dict

from rest_framework.response import Response
from rest_framework.serializers import ValidationError


def base_response(status_code: int, success: bool, code: int, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code}, status=status_code)


def base_response_with_error(
        status_code: int, success: bool, code: int, error: str, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)


def base_response_with_validation_error(
        status_code: int, success: bool, code: int, error: ValidationError, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)
