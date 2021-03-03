from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenWord(Token, ABC):
    """
         Token class of Word.

         constructor with two fields data and type of data.
         method put, with one argument char with type Char,
         token of word consists from many chars, so
         put add them to our data
         Raisers:
             not raising ane exceptions
         """
    def __init__(self):
        super().__init__()
        self.type = Kind.WORD
        self.data = ""

    def put(self, char):
        self.data += char
