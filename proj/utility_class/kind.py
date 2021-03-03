from enum import Enum


class Kind(Enum):
    """
         Kind of different kinds of tokens

         Raisers:
             not raising ane exceptions
         """
    SPACE = 1
    DoubleQuote = 2
    OneQuote = 3
    PIPE = 4
    WORD = 5
