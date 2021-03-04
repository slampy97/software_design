from unittest import TestCase

from proj.Commands.echo import Echo
from proj.executor import Executor
from proj.parser import Parser
from proj.token_split import Tokenizer


class ProjTest(TestCase):
    def test_echo(self):
        received = Echo().execute(["one", "two", "three"])
        expected = "one two three"
        self.assertEqual(received, expected)

    def test_token_split(self):
        raw = "echo one two three"
        token_split = Tokenizer()
        token_split.__run__(raw)
        expected = "WORD echo\nSPACE  \nWORD one\nSPACE  \nWORD two\nSPACE  \nWORD three\n"
        self.assertEqual(token_split.__review__(), expected)

    def test_token_split_with_double_quotes(self):
        raw = "echo \"one two\" three"
        token_split = Tokenizer()
        token_split.__run__(raw)
        expected = "WORD echo\nSPACE  \nDoubleQuote one two\nSPACE  \nWORD three\n"
        self.assertEqual(token_split.__review__(), expected)

    def test_token_split_with_single_quotes(self):
        raw = "echo 'one two' three"
        token_split = Tokenizer()
        token_split.__run__(raw)
        expected = "WORD echo\nSPACE  \nOneQuote one two\nSPACE  \nWORD three\n"
        self.assertEqual(expected, token_split.__review__())

    def test_token_diff_quotes(self):
        raw = "echo 'one \"two\"' three"
        token_split = Tokenizer()
        token_split.__run__(raw)
        expected = "WORD echo\nSPACE  \nOneQuote one \"two\"\nSPACE  \nWORD three\n"
        self.assertEqual(expected, token_split.__review__())

    def test_cat_file(self):
        raw = "cat file1.txt file2.txt"
        parser = Parser()
        parser.__set_str__(raw)
        parser.__fillCommands__({})
        executor = Executor(parser.commands, parser.args)
        executor.__execute__()
        expected = "banana\nfruit\noleg\nmaksim\n1\n2\n3\n4\n5\n6\n"
        self.assertEqual(expected, executor.out)

    def test_cat_with_wc(self):
        raw = "cat file1.txt file2.txt | wc"
        parser = Parser()
        parser.__set_str__(raw)
        parser.__fillCommands__({})
        executor = Executor(parser.commands, parser.args)
        executor.__execute__()
        expected = "     11      11      27 "
        self.assertEqual(expected, executor.out)

    def test_subs_vars(self):
        raw = "cat $a $b"
        parser = Parser()
        parser.__set_str__(raw)
        parser.__fillCommands__({'$a': "file1.txt", '$b': "file2.txt"})
        executor = Executor(parser.commands, parser.args)
        executor.__execute__()
        expected = "banana\nfruit\noleg\nmaksim\n1\n2\n3\n4\n5\n6\n"
        self.assertEqual(expected, executor.out)

    def test_subs_in_pipe(self):
        raw = "cat $a $b | echo $a $b"
        parser = Parser()
        parser.__set_str__(raw)
        parser.__fillCommands__({'$a': "file1.txt", '$b': "file2.txt"})
        executor = Executor(parser.commands, parser.args)
        executor.__execute__()
        expected = "file1.txt file2.txt"
        self.assertEqual(expected, executor.out)

    def test_grep(self):
        raw = "grep f $a $b"
        parser = Parser()
        parser.__set_str__(raw)
        parser.__fillCommands__({'$a': "file1.txt", '$b': "file2.txt"})
        executor = Executor(parser.commands, parser.args)
        executor.__execute__()
        expected = "fruit\n"
        self.assertEqual(expected, executor.out)