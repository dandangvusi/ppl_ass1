import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program_1(self):
        """Simple program with built in functions"""
        input = """
        Function: main
            Body:
                printLn();
                print("Hello BKIT");
                printStrLn("Hello Dan");
                read();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_simple_program_2(self):
        """Simple program with function call statement"""
        input = """
        Function: isGreaterThanZero
            Parameter: a
            Body:
                If a > 0 Then
                    Return True;
                Else
                    Return False;
            EndBody.
        Function: main
            Body:
                Var: x = 1;
                print(isGreaterThanZero(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """Var: ;"""
    #     expect = "Error on line 1 col 5: ;"
    #     self.assertTrue(TestParser.checkParser(input,expect,202))
