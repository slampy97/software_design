from abc import ABC, abstractmethod


class Command(ABC):
    """
       Fabric of user command.

       One abstract method execute with args:
          [optional] args = None, or list[String]
          [optional] inp, out with type = String. Input and output data, that
       allow to use this command inside pipeline

       """
    @abstractmethod
    def execute(self, args=None, inp=None, out=None):
        pass
