import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    # def test_comment(self):
    #     """test commment"""
    #     input = '// this is comment'
    #     expect = '// this is comment,<EOF>'
    #     self.assertTrue(TestLexer.test(input, expect, 101))
    def test(self): 
        """Test string"""
        input = """ "He, asked me: \\"Where is John?\\"" """
        expect = "He, asked me: \\\"Where is John?\\\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))
    # def test_keyword(self): 
    #     """Test identifier"""
    #     input = 'break'
    #     expect = 'auto,<EOF>'
    #     self.assertTrue(TestLexer.test(input, expect, 103))
    
