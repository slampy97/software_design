from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenSingleQuote(Token, ABC):
    """
         Token class of Single quote.

         constructor with two fields data and type of data.
         method put, with one argument char with type Char,
         token of single quotes consists from many chars, so
         put add them to our data
         Raisers:
             not raising ane exceptions
         """
    def __init__(self):
        super().__init__()
        self.data = ""
        self.type = Kind.OneQuote

    def put(self, char):
        if char != '\'':
            self.data += char
