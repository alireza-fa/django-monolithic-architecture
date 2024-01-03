from typing import Dict

from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.api.response_code import ERROR_TRANSLATION


def base_response(status_code: int, success: bool, code: int, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code}, status=status_code)


def base_response_with_error(
        status_code: int, success: bool, code: int, error: str | None = None, result: Dict | None = None) -> Response:
    if error:
        return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)
    return Response(data={"result": result, "success": success, "code": code, "error": ERROR_TRANSLATION[code]},
                    status=status_code)


def base_response_with_validation_error(
        status_code: int, success: bool, code: int, error: ValidationError, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)
