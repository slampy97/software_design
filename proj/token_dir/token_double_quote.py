from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenDoubleQuote(Token, ABC):
    def __init__(self):
        super().__init__()
        self.data = ''
        self.type = Kind.DoubleQuote

    def put(self, char):
        if char != '"':
            self.data += char
