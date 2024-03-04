from django.conf import settings

from apps.pkg.logger.seq.logger import SeqDataLust


def new_logger():
    match settings.LOGGER:
        case "seq":
            return SeqDataLust(api_key=settings.SEQ_API_KEY, base_url=settings.SEQ_BASE_URL)
