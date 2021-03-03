import os
import sys

from proj.Commands.Commands_fabric import Command


class Wc(Command):
    """
            Exit class of user command.

            One method execute with args:
               [optional] args = None, or list[String] with element - filenames
               [optional] inp, out with type = String. Input and output data, that
            allow to use this command inside pipeline

            If args = None count lines, words and bytes from standard input, else if
            len(args) == 1 then only count lines, words and bytes from this file, otherwise
            gibe additional info - total count of lines, words and bytes
            Raisers:
                not raising ant exceptions, just 0 0 0 data if could not find the filename
            """
    def execute(self, args=None, inp=None, out=None):
        lines = 0
        words = 0
        my_bytes = 0
        if args is None:
            if inp is not None:
                for line in inp.split('\n'):
                    lines += 1
                    words += len(line.split(' '))
                    my_bytes += sys.getsizeof(line) - sys.getsizeof("")
                return f"     {lines}      {words}      {my_bytes} "

            else:
                for line in sys.stdin:
                    lines += 1
                    words += len(line.split(' '))
                    my_bytes += sys.getsizeof(line) - sys.getsizeof("")
                return f"      {lines}       {words}      {my_bytes} "
        if len(list(args)) == 1:
            name = args[0].rstrip()
            if not os.path.isfile(name):
                return f"wc: {name}: No such file or directory"
            else:
                with open(name) as file:
                    content = file.read()
                    all_strings = list(filter(lambda string: string != "", content.splitlines()))
                    lines = len(all_strings)
                    words = sum([len(line.split(' ')) for line in all_strings])
                    my_bytes = os.path.getsize(name)
                    return f" {lines}  {words} {my_bytes} {name}"
        total_line = 0
        total_words = 0
        total_bytes = 0
        res_str = ""
        for arg in args:
            name = arg.rstrip()
            if not os.path.isfile(name):
                return f"wc: {name}: No such file or directory"
            else:
                with open(name) as file:
                    content = file.read()
                    all_strings = list(filter(lambda string: string != "", content.splitlines()))
                    lines = len(all_strings)
                    total_line += lines
                    words = sum([len(line.split(' ')) for line in all_strings])
                    total_words += words
                    my_bytes = os.path.getsize(name)
                    total_bytes += my_bytes
                    res_str += f" {lines}  {words} {my_bytes} {arg}\n"
        res_str += f"{total_line} {total_words} {total_bytes} total\n"
        return res_str
