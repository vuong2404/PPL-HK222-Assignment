import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    def test1(self):
        """test commment"""
        input = '// this is comment'
        expect = '// this is comment,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 101))
    def test2(self):
        """test commment"""
        input = """
        /* this is comment mutiple line
        *line 1 
        *line 2
        */"""
        expect ="""/* this is comment mutiple line

        *line 1 

        *line 2

        */,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))
    def test2(self):
        """test commment"""
        input = """
        /* this is comment mutiple line
        *line 1 
        *line 2
        */
        */"""
        expect ="""/* this is comment mutiple line

        *line 1 

        *line 2

        */,*,/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test3(self): 
        """Test 3 """
        input = """1_234_567 1_72 172"""
        expect = '1234567,172,172,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 103))
    def test4(self): 
        """Test 3 """
        input = """1.234 1.2e3 7E-10 1_234.567"""
        expect = '1.234,1.2e3,7E-10,1234.567,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 104))
    def test5(self): 
        """Test 3 """
        input = """a: boolean = true"""
        expect = 'a,:,boolean,=,true,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 105))
    def test6(self): 
        """Test 3 """
        input = """a = 1_234 + 5_678"""
        expect = 'a,=,1234,+,5678,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 106))
    def test7(self): 
        """Test 3 """
        input = """ "This is a string containing tab \\t" """
        expect = 'This is a string containing tab \\t,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 107))
    
    def test20(self): 
        """Test 3 """
        input = """ "My string: \\"hello" " """
        expect = 'My string: \\"hello,Unclosed String: " '
        self.assertTrue(TestLexer.test(input, expect, 120))
        
    def test8(self): 
        """Test 3 """
        input = """ "He asked me: \\"Where is John?\\" " """
        expect = 'He asked me: \\"Where is John?\\" ,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 108))
    def test9(self): 
        """Test 3 """
        input = """ a: array [4] of integer = {1, 5, 7, 12} """
        expect = 'a,:,array,[,4,],of,integer,=,{,1,,,5,,,7,,,12,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 109))
    def test10(self): 
        """Test 3 """
        input = """ {"Kangxi", "Yongzheng", "Qianlong"} """
        expect = '{,Kangxi,,,Yongzheng,,,Qianlong,},<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 110))
    def test11(self): 
        """Test 3 """
        input = """ a % 2 == 0 && a >= 10"""
        expect = 'a,%,2,==,0,&&,a,>=,10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 111))
    def test12(self): 
        """Test 3 """
        input = """ a + 21_234 == 15.234 && a <= -10"""
        expect = 'a,+,21234,==,15.234,&&,a,<=,-10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 112))
    def test13(self): 
        """Test 3 """
        input = """ a + 21_234 == 15.234 && a <= -10"""
        expect = 'a,+,21234,==,15.234,&&,a,<=,-10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 113))
    def test14(self): 
        """Test 3 """
        input = """ a + 21_234 == 15.234 && a <= -10"""
        expect = 'a,+,21234,==,15.234,&&,a,<=,-10,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 114))
    def test15(self): 
        """Test 3 """
        input = """ a = a::"string operator" """
        expect = 'a,=,a,::,string operator,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 115))
    def test16(self): 
        """Test 3 """
        input = """ i: int = array[0] """
        expect = 'i,:,int,=,array,[,0,],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 116))
    def test17(self): 
        """Test 3 """
        input = """ i: int = array[0] + b[0, 0] """
        expect = 'i,:,int,=,array,[,0,],+,b,[,0,,,0,],<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 117))
    def test18(self): 
        """Test 3 """
        input = """ if (a == 1) return 1; """
        expect = 'if,(,a,==,1,),return,1,;,<EOF>'
        self.assertTrue(TestLexer.test(input, expect, 118))
    
    
    
    
    
