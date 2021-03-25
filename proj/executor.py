import subprocess
import sys

from proj.Commands.cat import Cat
from proj.Commands.echo import Echo
from proj.Commands.exit import Exit
from proj.Commands.pwd import Pwd
from proj.Commands.wc import Wc
from proj.Commands.cd import Cd
from proj.Commands.ls import Ls


class Executor:
    """
         Executor class

         constructor with three fields commands and args. (and out for check output)
         and method execute that eval current line interpretation line
         and print result on standard output


         Raisers:
             not raising ane exceptions
         """
    def __init__(self, commands, args):
        self.commands = [com.rstrip() for com in commands]
        self.args = [[el.rstrip() for el in arg] for arg in args]
        self.out = ""

    def __execute__(self):
        """
        implements work with pipelines
        """
        setup = {'wc': Wc(), 'exit': Exit(), 'pwd': Pwd(), 'echo': Echo(), 'cat': Cat(), 'cd': Cd(), 'ls': Ls()}

        if len(self.commands) == 0:
            return
        fst_comma = self.commands[0]
        if fst_comma in setup:
            if len(self.args[0]) > 0:
                output = setup[fst_comma].execute(self.args[0])
            else:
                output = setup[fst_comma].execute(None)
        else:
            if len(self.args[0]) > 0:
                ps = subprocess.Popen((fst_comma, *self.args[0]), stdin=sys.stdin, stdout=subprocess.PIPE)
            else:
                ps = subprocess.Popen(fst_comma, stdin=sys.stdin, stdout=subprocess.PIPE)
            output = ps.stdout.read().decode('UTF-8')
        for index in range(1, len(self.commands)):
            if self.commands[index] in setup.keys():
                comma = setup[self.commands[index]]
                if len(self.args[index]) > 0:
                    output = comma.execute(self.args[index], inp=output)
                else:
                    output = comma.execute(None, inp=output)
            else:
                if len(self.args[index]) > 0:
                    p = subprocess.run([self.commands[index], *self.args[index]], stdout=subprocess.PIPE,
                                       input=output, encoding='ascii')
                else:
                    p = subprocess.run(self.commands[index], stdout=subprocess.PIPE,
                                       input=output, encoding='ascii')
                output = p.stdout
        self.out = output
        for line in output.split("\n"):
            print(line)
