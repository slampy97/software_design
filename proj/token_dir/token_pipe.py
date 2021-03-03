from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenPipe(Token, ABC):
    """
        Token class of DoubleQuote.

        constructor with two fields data and type of data.
        method put, with one argument char with type Char,
        token of pipe is not expandable, so put doing nothing
        Raisers:
            not raising ane exceptions
        """
    def __init__(self):
        super().__init__()
        self.data = '|'
        self.type = Kind.PIPE

    def put(self, char):
        pass
