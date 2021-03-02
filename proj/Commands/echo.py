from proj.Commands.Commands_fabric import Command


class Echo(Command):
    def execute(self, args=None, inp=None, out=None):
        return " ".join(args)
