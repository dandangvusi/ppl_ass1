import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_id_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_id_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("_abc", "_abc,<EOF>", 102))

    def test_id_3(self):
        """test illegal identifiers"""
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 103))

    def test_id_4(self):
        """test identifiers and reseeved words"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_array_lit_1(self):
        """test array literal"""
        self.assertTrue(TestLexer.checkLexeme(
            "Var: a[5] = {1,2,3,4,5};", "Var,:,a,[,5,],=,{1,2,3,4,5},;,<EOF>", 111))
