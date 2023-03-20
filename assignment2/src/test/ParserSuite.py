import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_full_vardecl(self):
        """Test full variable declaration"""
        input = """a : integer = 3::4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_wrong_full_vardecl(self):
        """Test wrong full variable declaration"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program(self):
        """Test simple program"""
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_full_program(self):
        """Test full program"""
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void() {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test1(self):
        input = """kaBoLTRLe:float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 301))

    def test2(self):
        input = """dDDLJUlVn, tewqOOz2X, QarWYDmCs:boolean;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 302))

    def test3(self):
        input = """ovalOkHdJ:string;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 303))

    def test4(self):
        input = """wduH3Uqoc, ZSliw2f9T, SjOiHOwvK:integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 304))

    def test5(self):
        input = """PpveyeIjJ: array[5] of integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 305))

    def test6(self):
        input = """EhrJHKzeO, OLp5RUAbd:void;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 306))
   
    def test7(self):
        input = """EhrJHKzeO, OLp5RUAbd:auto;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 307))

    def tets8(self):
        input = """a, b, c, d: integer = 3, 4, 6, 7;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 308)) 

    def test9(self):
        input = """a, b: array [5,2_2] of integer = {1,2,3,4}, {1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 309))

    def test10(self):
        input = """a, b: array [1_522] of integer = 3,4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 310))

    def test11(self): 
        input = """a,b,c: string = "hello", "hello, World", "hello" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 311))

    def test12(self):
        input = """a,b,c: string = a == b , a + 1, c + d;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 312))

    def test13(self):
        input = """dvtNu, GkXYLy, CtWWg, BiMJ9, hgJvA, DohAb: boolean = OZTnq > "T3bce",S2ciZVlbO != 979,cXt1Dpk3l - _85 - 2_3,-438-_23-332209,585,-847-416-753 ;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 313))
    def test14(self): 
        input = """ gSMqQEvNS, ZXEcQaq : string = phcMklS8X != pEWZQjukz,QzqUlwQtU == 265 ; """ 
        expect = """successful""" 
        self.assertTrue(TestParser.test(input, expect, 314))

    def test15(self): 
        input = """ YGAOlFxv1 : string = mxZBZaMWK >= "k5z6\\'" ; """ 
        expect = """successful""" 
        self.assertTrue(TestParser.test(input, expect, 315)) 
