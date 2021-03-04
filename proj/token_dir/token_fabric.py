from abc import ABC, abstractmethod


class Token(ABC):
    """
            fabric of tokens.

            constructor with two fields data and type of data.

            abstract method put, with one argument char with type Char,
            all type of tokens have their own behaviour, so need to implements
            in the inheritors

            method Kind without arguments, return the type of data in token

            Raisers:
                not raising ane exceptions
                """
    def __init__(self):
        self.type = None
        self.data = None

    @abstractmethod
    def put(self, char):
        pass

    def kind(self):
        return self.type
