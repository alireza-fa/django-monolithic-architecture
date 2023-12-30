from typing import Dict

from rest_framework.response import Response


def base_response(status_code: int, result: Dict, success: bool, code: int) -> Response:
    return Response(data={"result": result, "success": success, "code": code}, status=status_code)


def base_response_with_error(status_code: int, result: Dict, success: bool, code: int, error) -> Response:
    return Response(data={"result": result, "success": success, "code": code, "error": error}, status=status_code)
