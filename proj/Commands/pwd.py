import os

from proj.Commands.Commands_fabric import Command


class Pwd(Command):
    def execute(self, args=None, inp=None, out=None):
        # ignore args
        return os.getcwd()
