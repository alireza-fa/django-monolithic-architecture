from django.conf import settings

from apps.pkg.logger.dummy.logger import get_dummy_logger_once
from apps.pkg.logger.seq.logger import get_seq_logger_once


def new_logger():
    match settings.LOGGER:
        case "seq":
            return get_seq_logger_once()
    return get_dummy_logger_once()
