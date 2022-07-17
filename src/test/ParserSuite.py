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

    def test_simple_program_17(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_simple_program_18(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1 * 2) Do
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                    writeln(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_simple_program_19(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, getBigger(2, 3)) Do
                    writeln(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_simple_program_20(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x) Do
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "Error on line 5 col 33: )"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_simple_program_21(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1)
                    writeln(i);
                    If i % 2 == 0 Then
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "Error on line 6 col 20: writeln"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_simple_program_22(self):
        """Simple program with for statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_simple_program_23(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
                    a[i] = a[i]*b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_simple_program_24(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 + 1 Do
                    a[i] = a[i]*b;
                    i = i + 1;
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_simple_program_25(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
                EndWhile.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_simple_program_26(self):
        """Simple program with while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While i < 5 Do
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_simple_program_27(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While i < 5
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_simple_program_28(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                    a[i] = a[i]*b;
                    i = i + 1;
                While i < 5 + 1
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_simple_program_29(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                While i < 5
                EndDo.
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_simple_program_30(self):
        """Simple program with do-while statement"""
        input = """
        Function: multipleArray
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Do
                While i < 5
            EndBody.
        Function: main
            Body:
                Var: a[5] = {1,2,3,4,5}, b = 2;
                multipleArray(a,b);
            EndBody.
        """
        expect = "Error on line 8 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_simple_program_31(self):
        """Simple program with Break statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                    print(i);
                    If i > 3 Then
                        Break;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_simple_program_32(self):
        """Simple program with continue statement"""
        input = """
        Function: main
            Body:
                Var: x = 5;
                For (i = 0, i < x, 1) Do
                    If i%2==0 Then
                        Continue;
                    EndIf.
                    print(i);
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_simple_program_33(self):
        """Simple program with call and return statement"""
        input = """
        Function: isGreaterZero
        Parameter: a
            Body:
                Return a > 0;
            EndBody.
        Function: main
            Body:
                Var: x = 5;
                print(isGreaterZero(x));
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_simple_program_34(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = !b && a;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_simple_program_35(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = (c >. 1.0) || (c >. d);
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_simple_program_36(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = (c =/= d) && (d >. 0.0);
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_simple_program_37(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[1] + arr2[0] * arr2[1];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_simple_program_38(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = abs(-2) % multi(2, 3) - 4;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_simple_program_39(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = abs(arr1[1]) % multi(arr1[0], arr1[1]) - arr2[0];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_simple_program_40(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = -e - -3;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_simple_program_41(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = !!a && b || !b;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_simple_program_42(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = e\\f\\2 - 2*3*1;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_simple_program_43(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = e + 1 >= 3 * f;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_simple_program_44(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: r = 10., v; 
                v = (4.\. 3.) *. 3.14 *. r *. r*. r;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_simple_program_45(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[0] * 4 - 1;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_simple_program_46(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = !a && !b;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_simple_program_47(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                a = d *. 3.2 >. c;
                print(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_simple_program_48(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                a = arr1[0] >= arr2[0];
                print(a);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_simple_program_49(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[0] != arr2[0];
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_simple_program_50(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = arr1[1] * arr2[1] <= 100;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_simple_program_51(self):
        """Simple program with declare & assignment statement using expression"""
        input = """
        Function: main
            Body:
                Var: a = True, b = False, c = 2.4e-1, d = 1.0, e = 5, f = 3, g = "Hello", h = "Dan", arr1[2] = {1, 2}, arr2[2] = {3, 4};  
                res = 3.4 +. 5.3 -. c;
                print(res);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))