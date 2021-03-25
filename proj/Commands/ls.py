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
        if len(args) == 1:
            return "\t" + "\n\t".join(dirlist)
        output = []
        for arg in args:
            output.append(arg)
            output.append(":\n\t")
            dirlist = filter(lambda x: x[0] != "." and x[0] != "_", os.listdir(arg))
            output.append("\n\t".join(dirlist))
            output.append("\n")
        # output.append("\n")
        return "".join(output)