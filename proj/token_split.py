from proj.token_dir.toke_space import TokenSpace
from proj.token_dir.token_double_quote import TokenDoubleQuote
from proj.token_dir.token_pipe import TokenPipe
from proj.token_dir.token_single_quote import TokenSingleQuote
from proj.token_dir.token_word import TokenWord
from proj.utility_class.kind import Kind


class Tokenizer:
    """
         Class that split interpretation line in the tokens

         constructor without arguments, with one field, list of tokens
         """
    def __init__(self):
        self.tokens = []

    def __run__(self, string):
        """
             method that split line and fill list of tokens
             """
        for char in string:
            if char == '|':
                if len(self.tokens) == 0:
                    obj = TokenPipe()
                    self.tokens.append(obj)
                else:
                    cur_obj = self.tokens[-1]
                    if cur_obj.kind() == Kind.SPACE:
                        self.tokens.append(TokenPipe())
                    else:
                        cur_obj.put(char)
            elif char == ' ':
                if len(self.tokens) == 0:
                    self.tokens.append(TokenSpace())
                else:
                    cur_obj = self.tokens[-1]
                    check1 = cur_obj.kind() == Kind.OneQuote
                    check2 = cur_obj.kind() == Kind.DoubleQuote
                    check3 = cur_obj.kind() == Kind.SPACE
                    if check1 or check2 or check3:
                        cur_obj.put(char)
                    else:
                        self.tokens.append(TokenSpace())
            elif char == '\'':
                if len(self.tokens) == 0:
                    self.tokens.append(TokenSingleQuote())
                else:
                    cur_obj = self.tokens[-1]
                    if cur_obj.kind() == Kind.DoubleQuote:
                        cur_obj.put(char)
                    elif cur_obj.kind() == Kind.OneQuote:
                        self.tokens.append(TokenSpace())
                    else:
                        self.tokens.append(TokenSingleQuote())
            elif char == '"':
                if len(self.tokens) == 0:
                    obj = TokenDoubleQuote()
                    self.tokens.append(obj)
                else:
                    cur_obj = self.tokens[-1]
                    if cur_obj.kind() == Kind.DoubleQuote:
                        self.tokens.append(TokenSpace())
                    elif cur_obj.kind() == Kind.OneQuote:
                        cur_obj.put(char)
                    else:
                        self.tokens.append(TokenDoubleQuote())
            else:
                if len(self.tokens) == 0:
                    obj = TokenWord()
                    obj.put(char)
                    self.tokens.append(obj)
                else:
                    cur_obj = self.tokens[-1]
                    check1 = cur_obj.kind() == Kind.DoubleQuote
                    check2 = cur_obj.kind() == Kind.OneQuote
                    check3 = cur_obj.kind() == Kind.WORD
                    if check1 or check2 or check3:
                        cur_obj.put(char)
                    else:
                        obj = TokenWord()
                        obj.put(char)
                        self.tokens.append(obj)

    def __review__(self):
        """
             combine list of tokens in well readable string
             """
        final_str = ""
        for token in self.tokens:
            final_str += token.kind().name + ' ' + token.data + "\n"
        return final_str
