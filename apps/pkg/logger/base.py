from typing import Dict
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def debug(self, message: str, category: str, sub_category: str, properties: Dict):
        pass

    @abstractmethod
    def info(self, message: str, category: str, sub_category: str, properties: Dict):
        pass

    @abstractmethod
    def warn(self, message: str, category: str, sub_category: str, properties: Dict):
        pass

    @abstractmethod
    def error(self, message: str, category: str, sub_category: str, properties: Dict):
        pass
