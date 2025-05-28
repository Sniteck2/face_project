
from abc import ABC, abstractmethod

class BaseCamera(ABC):
    @abstractmethod
    def get_capture(self):
        pass