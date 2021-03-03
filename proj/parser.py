from proj.lexer import Lexer
from proj.token_split import Tokenizer
from proj.utility_class.kind import Kind


class Parser:
    """
         Parser class.

         constructor with four fields:
            commands with type string - name of commands
            args with type list[list[string]]
            str - current interpretation lie
            vars - variables thar are local declared during the work of application
            with type - dict{name-str:value-str}
         Raisers:
             not raising ane exceptions
         """
    def __init__(self):
        self.commands = []
        self.args = []
        self.str = None
        self.vars = None

    def __set_str__(self, string):
        """
             method that set string to work with
             """
        self.str = string

    def __fillCommands__(self, variables):
        """
             method with one argument variables
             do line split into tokens,
             than substitute local vars, and then again split into tokens
             final tokens are transformed into commands and their args
             filling class fields args and commands
             """
        tokenizer1 = Tokenizer()
        tokenizer1.__run__(self.str)
        lex = Lexer()
        lex.__setvar__(variables)
        lex.__setTokens__(tokenizer1.tokens)
        string = lex.substitute()
        tokenizer2 = Tokenizer()
        tokenizer2.__run__(string)
        self.vars = lex.vars
        cur_arg = []
        index = 0
        for token in list(filter(lambda tok: tok.kind() != Kind.SPACE, tokenizer2.tokens)):
            if token.kind() != Kind.PIPE and index == 0:
                self.commands.append(token.data)
                index += 1
            elif token.kind() != Kind.PIPE and index != 0:
                cur_arg.append(token.data)
            else:
                self.args.append(cur_arg)
                cur_arg = []
                index = 0
        self.args.append(cur_arg)
