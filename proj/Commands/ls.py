import os

from proj.Commands.Commands_fabric import Command


class Ls(Command):
    """
            Ld class of user command.

            One method execute with args:
               [optional] args = None, or list[String]
               [optional] inp, out with type = String. Input and output data, that
            allow to use this command inside pipeline

            Change working directory.
            - Printing content of the provided directory
            - ignoring filenames which starts on . and __
            Raisers:
                not raising any exceptions
            """
    def execute(self, args=None, inp=None, out=None):
        if not args:
            args = ["."]
        dirlist = filter(lambda x: x[0] != "." and x[0] != "_", os.listdir(args[0]))
        return "\t" + "\n\t".join(dirlist)