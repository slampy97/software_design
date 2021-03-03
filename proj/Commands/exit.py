import sys

from proj.Commands.Commands_fabric import Command


class Exit(Command):
    """
        Exit class of user command.

        One method execute with args:
           [optional] args = None, or list[String]
           [optional] inp, out with type = String. Input and output data, that
        allow to use this command inside pipeline

        Just terminate current process, ignoring any arguments
        Raisers:
            not raising ant exceptions
        """
    def execute(self, args=None, inp=None, out=None):
        sys.exit()
