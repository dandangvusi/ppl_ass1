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
                EndIf.
            EndBody.
        Function: main
            Body:
                Var: x = 1;
                print(isGreaterThanZero(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_simple_program_3(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    ElseIf x == 0 Then
                        print("x is equal to 0");
                    Else
                        print("x is less than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_simple_program_4(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_simple_program_5(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    ElseIf x == 0 Then
                        print("x is equal to 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_simple_program_6(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    Else
                        print("x is less than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_simple_program_7(self):
        """Simple program with If statement"""
        input = """
        Function: main
                Body:
                    Var: x = 5;
                    If x > 0 Then
                        print("x is greater than 0");
                    ElseIf x == 0 Then
                        print("x is equal to 0");
                    ElseIf x != 0 Then
                        print("x is not equal to 0");
                    Else
                        print("x is less than 0");
                    EndIf.
                EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_simple_program_8(self):
        """Simple program with Return statement"""
        input = """
        Function: add2int
            Parameter: a, b
            Body:
                Return a + b;
            EndBody.
        Function: main
            Body:
                Var: x = 1, y = 2, z;
                z = add2int(x, y);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_simple_program_9(self):
        """Simple program with Return statement"""
        input = """
        Function: foo
            Body:
                Return;
            EndBody.
        Function: main
            Body:
                foo();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_simple_program_10(self):
        """Simple program with Return statement outside function"""
        input = """
        Var: a, b = 1;
        Return a;
        Function: main
            Body:
                a = b + 2;
                print(a);
            EndBody.
        """
        expect = "Error on line 3 col 8: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_simple_program_11(self):
        """Simple program with variable declare statement"""
        input = """
        Var: x = 5, y = 2.0, z = "x*y = ";
        Function: main
            Body:
                Var: a;
                a = x * y;
                print(z);
                print(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_simple_program_12(self):
        """Simple program with variable declare statement"""
        input = """
        Var: x = 1.5e2, y = 3.6;
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                a[0] = 0;
                b = 5;
                print(b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_simple_program_13(self):
        """Simple program with variable declare statement apear after other statements"""
        input = """
        Var: x = 1.5e2, y = 3.6;
        Function: main
            Body:
                a[0] = 0;
                b = 5;
                Var: a[5] = {1,2,3,4,5}, b = 2;
                print(b);
            EndBody.
        """
        expect = "Error on line 7 col 16: Var"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_simple_program_14(self):
        """Simple program with assignment statement"""
        input = """
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                a[0] = getBigger(a[1], a[2]);
                b = 5 + 2*3;
                print(b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_simple_program_15(self):
        """Simple program with illegal assignment statement"""
        input = """
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                5 = getBigger(a[1], a[2]);
                b = 5 + 2*3;
                print(b);
            EndBody.
        """
        expect = "Error on line 5 col 16: 5"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_simple_program_16(self):
        """Simple program with illegal assignment statement"""
        input = """
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                a[0] = getBigger(a[1], a[2]);
                True = 5 + 2*3;
                print(b);
            EndBody.
        """
        expect = "Error on line 6 col 16: True"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """Var: ;"""
    #     expect = "Error on line 1 col 5: ;"
    #     self.assertTrue(TestParser.checkParser(input,expect,202))
