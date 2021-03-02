from abc import ABC

from proj.token_dir.token_fabric import Token
from proj.utility_class.kind import Kind


class TokenPipe(Token, ABC):
    def __init__(self):
        super().__init__()
        self.data = '|'
        self.type = Kind.PIPE

    def put(self, char):
        pass
