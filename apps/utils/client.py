from typing import Dict

from django.http import HttpRequest


def get_client_info(request: HttpRequest) -> Dict:
    ip_address = request.META.get('REMOTE_ADDR')

    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_address = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]

    return {
        "device_name": request.META.get('HTTP_USER_AGENT', ''),
        "ip_address": ip_address
    }
