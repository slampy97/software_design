import sys

from proj.executor import Executor
from proj.parser import Parser


class Interpretation:
    """
    Interpretation class that read lines from input and
    run bash commands
    """
    def __init__(self):
        self.vars = {}

    def __run__(self):
        for line in sys.stdin:
            parser = Parser()
            parser.__set_str__(line)
            parser.__fillCommands__(self.vars)
            self.vars.update(parser.vars)
            exc = Executor(parser.commands, parser.args)
            exc.__execute__()
