import os
import sys

from proj.Commands.Commands_fabric import Command


class Cat(Command):
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
