import functools
from typing import Dict
import requests

from django.utils import timezone
from django.conf import settings

from pkg.logger.base import Log
from .urls import NEW_EVENT
from pkg.logger import log_level
# from apps.common.tasks import create_new_event_task


class SeqDataLust(Log):

    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def debug(self, *, message: str, category: str, sub_category: str, properties: Dict):
        # create_new_event_task.delay(
        #     self.base_url + NEW_EVENT, log_level.DEBUG,
        #     message, category, sub_category, properties
        # )
        self.create_new_event(level=log_level.DEBUG, message=message, properties=properties)

    def info(self, *, message: str, category: str, sub_category: str, properties: Dict):
        # create_new_event_task.delay(
        #     self.base_url + NEW_EVENT, log_level.INFO,
        #     message, category, sub_category, properties
        # )
        self.create_new_event(level=log_level.INFO, message=message, properties=properties)

    def warn(self, *, message: str, category: str, sub_category: str, properties: Dict):
        # create_new_event_task.delay(
        #     self.base_url + NEW_EVENT, log_level.WARN,
        #     message, category, sub_category, properties
        # )
        self.create_new_event(level=log_level.WARN, message=message, properties=properties)

    def error(self, *, message: str, category: str, sub_category: str, properties: Dict):
        # create_new_event_task.delay(
        #     self.base_url + NEW_EVENT, log_level.ERROR,
        #     message, category, sub_category, properties
        # )
        self.create_new_event(level=log_level.ERROR, message=message, properties=properties)

    def create_new_event(self, level: int, message: str, properties: Dict):
        data = {
            "Events": [
                {
                    "Level": level,
                    "MessageTemplate": message,
                    "Timestamp": str(timezone.now()),
                    "Properties": {
                        **properties
                    }
                }
            ]
        }
        requests.post(url=self.base_url + NEW_EVENT, headers={"X-Seq-ApiKey": "6CGsArH5o6q1jGeP0vsz"}, json=data)


@functools.cache
def get_seq_logger_once() -> Log:
    return SeqDataLust(api_key=settings.SEQ_API_KEY, base_url=settings.SEQ_BASE_URL)
