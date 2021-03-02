from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, args=None, inp=None, out=None):
        pass
