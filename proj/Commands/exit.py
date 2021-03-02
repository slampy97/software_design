import sys

from proj.Commands.Commands_fabric import Command


class Exit(Command):
    def execute(self, args=None, inp=None, out=None):
        sys.exit()
