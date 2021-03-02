from abc import ABC, abstractmethod


class Token(ABC):
    def __init__(self):
        self.type = None
        self.data = None

    @abstractmethod
    def put(self, char):
        pass

    def kind(self):
        return self.type
