from unittest import TestCase

from proj.Commands.echo import Echo
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
        pass
