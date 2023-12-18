from rest_framework.response import Response


def base_response(status_code: int, result: object, success: bool, code: int) -> Response:
    return Response(data={"result": result, success: success, code: code}, status=status_code)
