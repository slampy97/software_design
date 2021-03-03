from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenSpace(Token, ABC):
    """
       Token class of space.

       constructor with two fields data and type of data.
       method put, with one argument char with type Char, if there are more
       than one space in a interpretation row,
       we should just ignore them, so put doing nothing
       Raisers:
           not raising ane exceptions
       """
    def __init__(self):
        super().__init__()
        self.data = ' '
        self.type = Kind.SPACE

    def put(self, char):
        pass
