import argparse
import sys
import re
from proj.Commands.Commands_fabric import Command

my_parser = argparse.ArgumentParser()
my_parser.add_argument(
    "pattern",
    metavar="PATTERN",
    type=str,
    help="regexp or word thar you looking for",
)
my_parser.add_argument(
    "files",
    metavar="FILE",
    type=str,
    nargs="*",
    help="files"
)
my_parser.add_argument(
    "-i",
    dest="is_ignore_case",
    action="store_true",
    help="ignoring case during search"
)
my_parser.add_argument(
    "-w",
    dest="is_full_word",
    action="store_true",
    help="search full word",
)
my_parser.add_argument(
    "-A",
    dest="num_to_print",
    type=int,
    default=0,
    help="number of lines to print following the match",
)


class Grep(Command):
    """
    Grep class with three options, to see more details write grep --help
    behavior is similar to bas command
    """

    def execute(self, args=None, inp=None, out=None):
        sys.argv.extend(args)

        args = my_parser.parse_args()
        pattern = args.pattern

        if args.is_ignore_case:
            pattern = re.compile(pattern, re.IGNORECASE)
        else:
            pattern = re.compile(pattern)
        output = ""
        repeat = args.num_to_print
        if len(args.files) == 0:
            num_repeat = 0
            for line in sys.stdin:
                check = len(list(filter(lambda x: x != '', re.findall(pattern, line)))) != 0
                if check:
                    num_repeat = repeat + 1
                if num_repeat != 0:
                    output += line
                    num_repeat -= 1
        else:
            for file in args.files:
                with open(file, "r") as f:
                    num_repeat = 0
                    for line in f.readlines():
                        check = len(list(filter(lambda x: x != '', re.findall(pattern, line)))) != 0
                        if check:
                            num_repeat = repeat + 1
                        if num_repeat != 0:
                            output += line
                            num_repeat -= 1
        return output
