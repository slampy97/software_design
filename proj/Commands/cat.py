import os
import sys

from proj.Commands.Commands_fabric import Command


class Cat(Command):
    """
    Cat class of user command.

    One method execute with args:
       [optional] args = None, or list[String] where elements are filenames
       [optional] inp, out with type = String. Input and output data, that
    allow to use this command inside pipeline
    Concat data from all file or standard input
    Raisers:
        raising IOError if not such name of file exists
    """
    def execute(self, args=None, inp=None, out=None):
        output = ""
        if args is None:
            if inp is not None:
                output = inp
            else:
                for line in sys.stdin:
                    output += line
        else:
            for name in args:
                name = name.rstrip()
                if not os.path.isfile(name):
                    raise IOError(f"No such file exists {name}")
                with open(name) as file:
                    for line in file:
                        output += line
        return output
