from proj.token_split import Tokenizer
from proj.utility_class.kind import Kind


def is_var(string):
    if string.find('=') == -1:
        return None
    name, value = string.split('=')
    if name[1:].isalnum() and name[0] == '$':
        return {name: value}
    return None


class Lexer:
    def __init__(self):
        self.vars = None
        self.tokens = None

    def __setvar__(self, var):
        self.vars = var

    def __setTokens__(self, tokens):
        self.tokens = tokens

    def __make_str__(self):
        res_str = ""
        for token in self.tokens:
            if token.kind() == Kind.PIPE:
                res_str += '|'
            elif token.kind() == Kind.SPACE:
                res_str += ' '
            elif token.kind() == Kind.DoubleQuote:
                res_str += '"'
                res_str += token.data
                res_str += '"'
            elif token.kind() == Kind.OneQuote:
                res_str += '\''
                res_str += token.data
                res_str += '\''
            else:
                res_str += token.data
        return res_str

    def __updateTokens__(self, string):
        token_maker = Tokenizer()
        token_maker.__run__(string)
        self.tokens = token_maker.tokens

    def substitute(self):
        if self.tokens is not None and self.vars is not None:
            pipe_count = 0
            for token in self.tokens:
                if token.kind() == Kind.PIPE:
                    pipe_count += 1
            if pipe_count == 0:
                res_str = ""
                for token in self.tokens:
                    if token.kind() == Kind.WORD:
                        dict_or_none = is_var(token.data)
                        if dict_or_none is not None:
                            self.vars.update(dict_or_none)
                        else:
                            for key in self.vars.keys():
                                if token.data.find(key) != -1:
                                    token.data = token.data.replace(key, self.vars[key])
                            res_str += token.data
                    elif token.kind() == Kind.PIPE:
                        res_str += '|'
                    elif token.kind() == Kind.SPACE:
                        res_str += ' '
                    elif token.kind() == Kind.DoubleQuote:
                        res_str += '"'
                        words = token.data.split()
                        for word in words:
                            if word in self.vars.keys():
                                res_str += self.vars[word]
                            else:
                                res_str += word
                            res_str += ' '
                        res_str += '"'
                    else:
                        res_str += '\''
                        res_str += token.data
                        res_str += '\''
                return res_str
            else:
                res_str = ""
                for token in self.tokens:
                    if token.kind() == Kind.WORD:
                        for key in self.vars.keys():
                            if token.data.find(key) != -1:
                                token.data = token.data.replace(key, self.vars[key])
                        res_str += token.data
                    elif token.kind() == Kind.PIPE:
                        res_str += '|'
                    elif token.kind() == Kind.SPACE:
                        res_str += ' '
                    elif token.kind() == Kind.DoubleQuote:
                        res_str += '"'
                        words = token.data.split()
                        for word in words:
                            if word in self.vars.keys():
                                res_str += self.vars[word]
                            else:
                                res_str += word
                            res_str += ' '
                        res_str += '"'
                    else:
                        res_str += '\''
                        res_str += token.data
                        res_str += '\''
                return res_str
        return ""
