import os

from proj.Commands.Commands_fabric import Command


class Pwd(Command):
    """
            Exit class of user command.

            One method execute with args:
               [optional] args = None, or list[String]
               [optional] inp, out with type = String. Input and output data, that
            allow to use this command inside pipeline

            Print path of current process
            Raisers:
                not raising ant exceptions
            """
    def execute(self, args=None, inp=None, out=None):
        # ignore args
        return os.getcwd()
