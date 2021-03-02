from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenWord(Token, ABC):
    def __init__(self):
        super().__init__()
        self.type = Kind.WORD
        self.data = ""

    def put(self, char):
        self.data += char
