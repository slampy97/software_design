from proj.Commands.Commands_fabric import Command


class Echo(Command):
    """
        Echo class of user command.

        One method execute with args:
           [optional] args = None, or list[String] where elements are just different strings
           [optional] inp, out with type = String. Input and output data, that
        allow to use this command inside pipeline
        Just print arguments with ' ' as sep
        Raisers:
            not raising any exceptions
        """
    def execute(self, args=None, inp=None, out=None):
        return " ".join(args)
