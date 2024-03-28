from django.conf import settings

from pkg.logger.dummy.logger import get_dummy_logger_once
from pkg.logger.seq import get_seq_logger_once


def new_logger():
    match settings.LOGGER:
        case "seq":
            return get_seq_logger_once()
    return get_dummy_logger_once()
