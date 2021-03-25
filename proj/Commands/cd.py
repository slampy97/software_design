import sys
import os

from proj.Commands.Commands_fabric import Command


class Cd(Command):
    """
            Cd class of user command.

            One method execute with args:
               [optional] args = None, or list[String]
               [optional] inp, out with type = String. Input and output data, that
            allow to use this command inside pipeline

            Change working directory.
            - Ignoring everything except first argument which is treated as new directory.
            - If no arguments provided, this command does nothing
            Raisers:
                not raising any exceptions
            """
    def execute(self, args=None, inp=None, out=None):
        if not args:
            return
        new_dir = args[0]
        os.chdir(new_dir)
        return ""

