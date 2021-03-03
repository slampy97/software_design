from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenDoubleQuote(Token, ABC):
    """
        Token class of DoubleQuote.

        constructor with two fields data and type of data.
        method put, with one argument char with type Char,
        token of double quotes consists from many chars, so
        put add them to our data
        Raisers:
            not raising ane exceptions
        """
    def __init__(self):
        super().__init__()
        self.data = ''
        self.type = Kind.DoubleQuote

    def put(self, char):
        if char != '"':
            self.data += char
