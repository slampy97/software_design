from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenSpace(Token, ABC):
    def __init__(self):
        super().__init__()
        self.data = ' '
        self.type = Kind.SPACE

    def put(self, char):
        pass
