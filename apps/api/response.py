from typing import Dict

from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from apps.api.response_code import ERROR_TRANSLATION
from apps.api.response_code import BAD_REQUEST


def base_response(status_code: int, code: int, success: bool = True, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code}, status=status_code)


def base_response_with_error(
        status_code: int, code: int, success: bool = False,
        error: str | None = None, result: Dict | None = None) -> Response:
    if error:
        return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)
    return Response(data={"result": result, "success": success, "code": code, "error": ERROR_TRANSLATION[code]},
                    status=status_code)


def base_response_with_validation_error(
        status_code: int, error: ValidationError, code: int = BAD_REQUEST,
        success: bool = False, result: Dict | None = None) -> Response:
    return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)
