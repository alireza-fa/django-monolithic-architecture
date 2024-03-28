import functools
from typing import Dict

from pkg.logger.base import Log


class DummyLogger(Log):

    def debug(self, message: str, category: str, sub_category: str, properties: Dict):
        print(f"message: {message}, category: {category}, sub category: {sub_category}, properties: {properties}")

    def info(self, message: str, category: str, sub_category: str, properties: Dict):
        print(f"message: {message}, category: {category}, sub category: {sub_category}, properties: {properties}")

    def warn(self, message: str, category: str, sub_category: str, properties: Dict):
        print(f"message: {message}, category: {category}, sub category: {sub_category}, properties: {properties}")

    def error(self, message: str, category: str, sub_category: str, properties: Dict):
        print(f"message: {message}, category: {category}, sub category: {sub_category}, properties: {properties}")


@functools.cache
def get_dummy_logger_once():
    return DummyLogger()
