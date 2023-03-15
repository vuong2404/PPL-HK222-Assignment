import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    

    ### test varible declaration
    def test1(self):
        input = """kaBoLTRLe:float;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 201))

    def test2(self):
        input = """dDDLJUlVn, tewqOOz2X, QarWYDmCs:boolean;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 202))

    def test3(self):
        input = """ovalOkHdJ:string;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 203))

    def test4(self):
        input = """wduH3Uqoc, ZSliw2f9T, SjOiHOwvK:integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 204))

    def test5(self):
        input = """PpveyeIjJ: array[5] of integer;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 205))

    def test6(self):
        input = """XZqNzJwbm, mAkYb7JSV, SmDls1MgA, VJuXHyopJ:Float;"""
        expect = """Error on line 1 col 43: Float"""
        self.assertTrue(TestParser.test(input, expect, 206))

    def test7(self):
        input = """Zq8dPsFvA, KZoTPReQv:bool;"""
        expect = """Error on line 1 col 21: bool"""
        self.assertTrue(TestParser.test(input, expect, 207))

    def test8(self):
        input = """EhrJHKzeO, OLp5RUAbd:void;"""
        expect = """Error on line 1 col 21: void"""
        self.assertTrue(TestParser.test(input, expect, 208))

    def test9(self):
        input = """GvayUOdQA, fDFguZEyB: int,float;"""
        expect = """Error on line 1 col 22: int"""
        self.assertTrue(TestParser.test(input, expect, 209))

    def test10(self):
        input = """kgpInzKzB: array [] of integer;"""
        expect = """Error on line 1 col 18: ]"""
        self.assertTrue(TestParser.test(input, expect, 210))

    def test11(self):
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test12(self):
        input = """a, b: array [5,2] of integer = {1,2,3,4}, {1,2,3,4};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test13(self):
        input = """a, b: array [1_5] of integer = 3,4;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test14(self):
        input = """a: array [1,2,3] of boolean = {1,2,3,4,5};"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test15(self):
        input = """a,b,c: string = {1,2,3,4,5};"""
        expect = "Error on line 1 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test16(self): 
        input = """a,b,c: string = "hello", "hello, World", "hello" ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test17(self):
        input = """a,b,c: string = a == b , a + 1, c + d;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test18(self):
        input = """dvtNu, GkXYLy, CtWWg, BiMJ9, hgJvA, DohAb: boolean = OZTnq > "T3bce",S2ciZVlbO != 979,cXt1Dpk3l - _85 - 2_3,-438-_23-332209,585,-847-416-753 ;"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))
    def test19(self): 
        input = """ gSMqQEvNS, ZXEcQaq : string = phcMklS8X != pEWZQjukz,QzqUlwQtU == 265,NiumiBfDZ ; """ 
        expect = """Error on line 1 col 81: ;""" 
        self.assertTrue(TestParser.test(input, expect, 219))

    def test20(self): 
        input = """ YGAOlFxv1 : string = mxZBZaMWK >= "k5z6\\'" ; """ 
        expect = """successful""" 
        self.assertTrue(TestParser.test(input, expect, 220)) 
    
    
    ### test simple function declaration
    def test21(self):
        input = """ 
        // main function
        main : function void() {
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 221))
    def test22(self):
        input = """ 
        main : function integer ()  {
           // typr of main function is void
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 222))
    def test23(self):
        input = """ 
        main : function void (a: integer)  {
           // main function have no parameter
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))
    
    def test24(self):
        input = """ 
        main : function void ()  {
            return 1;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))
    
    def test25(self):
        input = """
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        /* inc: function void (out n: integer, delta: integer) {
            n = n + delta;
        } */
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test26(self):
        input = """
        sum: function void(out ressult:integer, a: integer, b: integer) {
           result =  a + b ; 
        }
        main: function void() {
            result,a,b: integer = 0, 10, 19 ;
            sum(result, a, b) ;
            printInteger(result) ; 
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test27(self):
        input = """ 
        ooMWtvLEh : function  void (){
            if (___ >= 1_7)
            qBWIBTwxF = WzcyGkfcn < 983;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))

    def test28(self):
        input = """ 
        hjj9pfFxl : function  integer (inherit out jfigupugy:integer, out fDyvnqIxV:string) inherit TfcV9WZzb {
            2nWHQpnfW = BwsvaDRoy > DxNrGYIKs;
        }
        """
        expect = """Error on line 3 col 12: 2"""
        self.assertTrue(TestParser.test(input, expect, 228))

    def test29(self):
        input = """ 
        foo : function string ( inherit out OMsQMycjS:float ) inherit yJyjJjUPU {
            a2 + 3 = a + b ;
        }
        """
        expect = """Error on line 3 col 15: +"""
        self.assertTrue(TestParser.test(input, expect, 229))

    def test30(self):
        input = """ 
        check : function  boolean ( str:string, out piq1PC3Aj:integer ) inherit String {
            return len(str) <= len("\\"eDfY");
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 230))
   
    ### test statement
    def test31(self):
        input = """ 
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = a + b ;
            c = c * 4 ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test32(self):
        input = """ 
        sum: function integer(a: integer, b:integer) {
            c = a + b ; 
            return c ; 
        }
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = sum(a,b) + 40 ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))
    def test33(self):
        input = """ 
        main : function  void () {
            a : array [5] of integer = {1,2,3,4} ;
            b = a[0] ;
            c = a[1] ;
            a[2] = b + c ;
            d[1,2,3] = a[c,1,2,3] + a[b] ;
            printInt(a[1,2,3,4]) ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 233))
    
    def test34(self):
        input = """ 
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = a + b ;
            c = c * 4 ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 234))
    
    def test35(self):
        input = """ 
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = a + b ;
            c = c * 4 ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))
    
    def test36(self):
        input = """ 
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = a + b ;
            c = c * 4 ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 236))
    
    def test37(self):
        input = """ 
        main : function  void () {
            if (a == 5) {
                a = a + 1 ;
            }
        }
    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 237))
    def test38(self):
        input = """ 
        main : function  void () {
            if (a == 5) 
               return a ;
        }
    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 238))

    def test39(self):
        input = """ 
        main : function  void () {
            if (a == 5) 
              return a ;
            else return b ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))
        

    def test40(self):
        input = """ 
        main : function  void () {
                if (a == 5) 
                    a = a + 1 ;
                    return a ;
                else return b ;
        }
    
        """
        expect = """Error on line 6 col 16: else"""
        self.assertTrue(TestParser.test(input, expect, 240))
        

    def test41(self):
        input = """ 
        main : function void () {
                if (a == 5) 
                   { 
                        a = a + 1 ;
                        return a ;
                    }
                else return b ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 241))
        

    def test42(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i + 1) 
                result = result + i ; 
        }
        main: function void() {
            result = 0 ;
            a: array [5] of integer = {1,2,3,4,5,6,7} ;
            sumOfArray(a, result) ;
            printInt(result) ;
        }
    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 242))
        

    def test43(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  a || b , i < len(a) , i + 1) 
                result = result + i ; 
        }
        main: function void() {
            result = 0 ;
            a: array [5] of integer = {1,2,3,4,5,6,7} ;
            sumOfArray(a, result) ;
            printInt(result) ;
        }
        """
        expect = """Error on line 4 col 25: ||"""
        self.assertTrue(TestParser.test(input, expect, 243))
        

    def test44(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < str::"hello" , i + 1) 
                result = result + i ; 
        }
        main: function void() {
            result = 0 ;
            a: array [5] of integer = {1,2,3,4,5,6,7} ;
            sumOfArray(a, result) ;
            printInt(result) ;
        }
        """
        expect = """Error on line 4 col 34: ::"""
        self.assertTrue(TestParser.test(input, expect, 244))
        

    def test45(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i = i + 1) 
                result = result + i ; 
        }
        main: function void() {
            result = 0 ;
            a: array [5] of integer = {1,2,3,4,5,6,7} ;
            sumOfArray(a, result) ;
            printInt(result) ;
        }
        """
        expect = """Error on line 4 col 42: ="""
        self.assertTrue(TestParser.test(input, expect, 245))
        

    def test46(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i + 1, i + 2) 
                result = result + i ; 
        }
        main: function void() {
            result = 0 ;
            a: array [5] of integer = {1,2,3,4,5,6,7} ;
            sumOfArray(a, result) ;
            printInt(result) ;
        }
        """
        expect = """Error on line 4 col 45: ,"""
        self.assertTrue(TestParser.test(input, expect, 246))
        

    def test47(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 ; i < len(a) ; i + 1) 
                result = result + i ; 
        }
        main: function void() {
            result = 0 ;
            a: array [5] of integer = {1,2,3,4,5,6,7} ;
            sumOfArray(a, result) ;
            printInt(result) ;
        }
    
        """
        expect = """Error on line 4 col 25: ;"""
        self.assertTrue(TestParser.test(input, expect, 247))

    def test48(self):
        input = """ 
        // Nested for
        sumOfArray : function void (a: array [2,2] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i + 1) 
                for (j = 0 , j > len(a[0]) , j + 1)
                    result = result + a[i,j] ;
        }
        main: function void() {
            result = 0 ;
            a: array [2,2] of integer = {{1,2}, {2,3}} ;
            sumOfArray(a, result) ;
            printInt(result) ; // 8
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 248))
        

    def test49(self):
        input = """ 
        // Nested for
        sumOfArray : function void (a: array [2,2] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i + 1) 
                for (j = 0 , j > len(a[0]) , j + 1)
                    result = result + a[i][j] ; // error
        }
        main: function void() {
            result = 0 ;
            a: array [2,2] of integer = {{1,2}, {2,3}} ;
            sumOfArray(a, result) ;
            printInt(result) ; // 8
        }
        """
        expect = """Error on line 7 col 42: ["""
        self.assertTrue(TestParser.test(input, expect, 249))
        

    def test50(self):
        input = """ 
        // Nested for with block
        sumOfArray : function void (a: array [2,2] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            countLoop: integer = 0 ;
            for (i  =  0 , i < len(a) , i + 1) {
                countLoop = countLoop + 1 ;
                for (j = 0 , j > len(a[0]) , j + 1) {
                    result = result + a[i,j] ;
                }
            }
        }
        main: function void() {
            result = 0 ;
            a: array [2,2] of integer = {{1,2}, {2,3}} ;
            sumOfArray(a, result) ;
            printInt(result) ; // 8
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 250))
    def test51(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            while (i <= len(s) - 1) {
                if ((i >= start) && (i <= end))
                    result = result::s[i] ;
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ; // 8
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 251))
        
    def test52(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            while (i <= len(s) - 1) {
                if (i >= start && i <= end) //error 
                    result = result::s[i] ;
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ; // 8
        }
        """
        expect = """Error on line 6 col 36: <="""
        self.assertTrue(TestParser.test(input, expect, 252))
        

    def test53(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            while (i <= len(s) - 1) {
                if ((i >= start) && (i <= end))
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                else 
                    i = i + 1 ;
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ; // 8
        }
    
        """
        expect = """Error on line 9 col 16: else"""
        self.assertTrue(TestParser.test(input, expect, 253))
        

    def test54(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            while (i <= len(s) - 1) {
                if ((i >= start) && (i <= end)) { 
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                }
                else 
                    i = i + 1 ;
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 254))
        

    def test55(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            do {
                if ((i >= start) && (i <= end)) { 
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                }
                else 
                    i = i + 1 ;
            } while ((i <= len(s) - 1)) ;
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
    
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))
        

    def test56(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            do {
                if ((i >= start) && (i <= end)) { 
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                }
                else 
                    i = i + 1 ;
            } while ((i <= len(s) - 1)) // error 
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
        """
        expect = """Error on line 13 col 12: return"""
        self.assertTrue(TestParser.test(input, expect, 256))
        

    def test57(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            do 
                if ((i >= start) && (i <= end)) { 
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                }
                else 
                    i = i + 1 ; 
             while ((i <= len(s) - 1)) ;
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
        """
        expect = """Error on line 6 col 16: if"""
        self.assertTrue(TestParser.test(input, expect, 257))
        

    def test58(self):
        input = """ 
            find : function string (s: string,ch: string) inherit String {
            i: integer = 0 ;
            result: integer = -1 ;
            while (i <= len(s) - 1) {
                if (s[i] == d) { 
                  result = i ;
                  break ;
                }
                else {
                    i = i + 1 ; 
                    continue ;
                } 
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 258))
        

    def test59(self):
        input = """ 
        find : function string (s: string,ch: string) inherit String {
            i: integer = 0 ;
            result: integer = -1 ;
            while (i <= len(s) - 1) {
                if (s[i] == d) { 
                  result = i ;
                  break ;
                }
                else {
                    i = i + 1 ; 
                    Continue; // error
                } 
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
        """
        expect = """Error on line 12 col 28: ;"""
        self.assertTrue(TestParser.test(input, expect, 259))
        

    def test60(self):
        input = """ 
        find : function string (s: string,ch: string) inherit String {
            i: integer = 0 ;
            result: integer = -1 ;
            while (i <= len(s) - 1) {
                if (s[i] == d) { 
                  result = i ;
                  breaK ; // error
                }
                else {
                    i = i + 1 ; 
                    continue ;
                } 
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
        """
        expect = """Error on line 8 col 24: ;"""
        self.assertTrue(TestParser.test(input, expect, 260))
        
    ### ramdom testcase 

    def test61(self):
        input = """ 
        QzTwgNOAB : function  void (vuyNPU5gd:string, QTaIAPOeH:string){
            aWLohOnWo:float;
            for (QaPcp6Bgt=-393, 8xNILoTLv > waLauwzFr, -945+394)
            while (igdEQlzAo >= k2gzstcol) 
                 OjZfBbKNk, i6kLoeBqT, meVruOFBb : float = US1sy1G1d > 695  ;
        }
        """
        expect = """Error on line 4 col 34: xNILoTLv"""
        self.assertTrue(TestParser.test(input, expect, 261))
        

    def test62(self):
        input = """ 
        eOYtvrJUG : function  float (out 4EYTIjDWw:float) {
            if (jMjL5hzsc >= _37)
            8pXrYiamy = jzaSXMzfw != "\\'zrRu";
        }
        """
        expect = """Error on line 2 col 41: 4"""
        self.assertTrue(TestParser.test(input, expect, 262))
        

    def test63(self):
        input = """ 
        gumCiFlgP : void = pCgXMdc9Z >= 664 ;
        """
        expect = """Error on line 2 col 20: void"""
        self.assertTrue(TestParser.test(input, expect, 263))
        

    def test64(self):
        input = """ 
        zNUBT1a5I : string = FBJ5dxfoH < "mDana" ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 264))
        

    def test65(self):
        input = """ 
        ZovgPbMwK : integer = U7kDjPhZQ > _93 ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 265))
        

    def test66(self):
        input = """ 
        XrRvlJIG1, UYDCYwcGf:void;
        """
        expect = """Error on line 2 col 29: void"""
        self.assertTrue(TestParser.test(input, expect, 266))
        

    def test67(self):
        input = """ 
        CmEUgpnkq:void;
        """
        expect = """Error on line 2 col 18: void"""
        self.assertTrue(TestParser.test(input, expect, 267))
        

    def test68(self):
        input = """ 
    bxvKBRuF6:void;
    
        """
        expect = """Error on line 2 col 14: void"""
        self.assertTrue(TestParser.test(input, expect, 268))
        

    def test69(self):
            input = """ 
        SQZNr6JOY : function  float (out NedsZTMtH:float) inherit W4QFwM1J3 {
            for (NhfQBlxmW=146, d6pxmSLCh(Xpfhh7LFC > 6_5,598 >= _44,dKzLwvNek == 48) < "tod\\nQ", fKNqGDGYc+-64)
                QnVjBrmDD(vbieKp8V2(yVZXv2EhK < __8) != "A\\t3zi");
            if (1 == 2) return kRwazdB4N > _5_;
            for (gEi6fQPQB=425, qYOnZ3hwi >= "hPUJa", qNpoRODYk+-638)
                break;
            do {
                continue;
                RPNq9nmQP:integer;
                for (ocPVclnMe=_, klFUkqweP < jWICdQ2CQ, sXYMDAjia-9_9)
                    mfVpPkzTY = xusb1AWu == 188;
                yBPgOgYSC = DdNwSxsmA == -653;
                rNDHXKOsd : boolean = NQcJmdWaP >= -__ ;
                for (HiTlfTpMe=781, lKWNHUrPP < -137, -25+-13)
                    break;
                
                for (BRnXVp5jf=-53_2, gdKobkUKF >= -30, _12+-276)
                    ROhemMlFf = 452 == -640;
                b7zYBtH8Q = TGwqX0ZYr != "q0YeF";
                gyrVSjPLL = kXqgyNmdu > 8_7;
                qHK0JAHAU = eSoCE7TDt >= -828;
                if (KBEOoNfEZ == 969)
                HSZLsNxAs = -63_123 == -345;
                AdMJWZpyY = ExVUnyC9 > "yGN1y";
                JxXXIJUsG = mccZoXdJP >= lrnxrVNcF;
        
                if (xmCf0MWaK >= 15)
                    fDchDmwrH = -935 > -398;
                for (QDXdeeZBo=578, jsygghYqP < 550, 458+-55)
                    for (uW8c6rQDY=-330, CcvvtHjnA > 355, wKl9DiNnE-8_3)
                        break;
                    CZCw8cUf = LPylsYZrd > -68_2;
                IuizFfhrq:boolean;
                if (uczTlZWJH != 7_2)
                    irJTIvhDm(322 > 321);
                GPxYKhqnw = Agu4lEcHy > "8J\\ts9";
                if (aLIrfQsK3 == 680) {
                    tSBSXfUg = SoyTBUUxp > "qFiUV";
                    RBLIjgAJI = FxNygjJzH != -925;
                    OJZV9xycB(zRgEknsut > "gqyVu");
                    ZVJcNkYmA = PRhMHgujf >= 310;   
                }
            } while (1==1);
            
            for (p9FnpJc4j=-657, lkJVLdvi7 != 73_22, NZGBdAt6K-15)
                break;
            vpbcvQCyW = UUqfdf0Cp > "\\t\\'toR";
            return aCygSBmlc > "vK4Cy";
        }

            """
            expect = """successful"""
            self.assertTrue(TestParser.test(input, expect, 269))

    def test70(self):
        input = """ 
         cywr1OjLX : integer = zNIcmcOOv == -451,skZOr5KxB >= 101 ;
        """
        expect = """Error on line 2 col 66: ;"""
        self.assertTrue(TestParser.test(input, expect, 270))
        
    def test71(self):
        input = """ 
        abczyz : function  float ( inherit out e9XgkiuWr:integer, WEceApeFD:string, inherit out fFQiZPzNi:integer, out pjHUhUpkl:string ) inherit VYLtCaatH {
             return ltOPmdJQP(XfC5CRYcb(NwWTHICwq < 846) >= "JD7Yu",zEBkvdbBi < "GMASN",aeemhejkH >= 949) != "VQ3vb";
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 271))
        

    def test72(self):
        input = """ 
         ZaMTvuSQB, FLKljqK6A : bool = MIktlKXeg(KHGfDvEpQ >= "CByxr") == "XJWWO" ;
        """
        expect = """Error on line 2 col 32: bool"""
        self.assertTrue(TestParser.test(input, expect, 272))
        

    def test73(self):
        input = """ 
        main : function  float ( inherit out xxrRpmn9v:float, out dr4hE0KO5:string ) inherit xHDmbATrr {
            break;
            MUcczyWVC = Aol0ZSZKf < 473;
        }

        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 273))
        

    def test74(self):
        input = """ 
          IjRzmSpGy : string = iFvFtLejK >= SDtEJEFuV ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 274))
        
    def test75(self):
        input = """ 
        YLKpfAUkC : function  float (ULQRfuoRb:string) inherit AWW0TYqJW {
             while (WWAcGS58C == vfLkEQmDD) 
                 while (N1jNxtOkU(rhSFE8wPK == 592) < "OehJj") 
                    aXUSZOHGq = Dn0DlQhGD != 498;
                 if (170 != 659)
                    H8aHMGS2N:float;

        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 275))
        

    def test76(self):
        input = """ 
        HKzSuOpwB : function  string (out Y46sILsGL:string){
             VEuUTaAYd, qALCcPbwB:void;
        }
        """
        expect = """Error on line 3 col 34: void"""
        self.assertTrue(TestParser.test(input, expect, 276))
        

    def test77(self):
        input = """ 
        YsBaKPqDO : function  float (inherit out EBjrIFazv:float){
            2ASetBDUv = rCvHpuMkh(Hf4ArivdD < 152) == "VcuLS";
        }
        """
        expect = """Error on line 3 col 12: 2"""
        self.assertTrue(TestParser.test(input, expect, 277))
        

    def test78(self):
        input = """ 
            vmmzFSDHH:float;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 278))
        

    def test79(self):
        input = """ 
            Lk9KhmSVz, QeVWLd6Vq, gWS85dvnJ : void = JoDJsJfJQ(RDd9RKpRe == -095) != "6gpNE",feIxHhHCv == -675 ;
        """
        expect = """Error on line 2 col 46: void"""
        self.assertTrue(TestParser.test(input, expect, 279))
        

    def test80(self):
        input = """ 
        main : function  void ( ) {
             for (pDMYsFcRT=-430, wooxtuKmR >= 277, BvYfEnhaL+346)
                continue;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 280))
        

    def test81(self):
        input = """ 
            UqqrNJybN:float;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 281))
        

    def test82(self):
        input = """ 
            vnyFswZXh, ChHuAcFwC : integer = 4,mFQIbs8W != "bT2\\ts" ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 282))
        

    def test83(self):
        input = """ 
         FjrrhieXg, Ne4CdQa6n:bool;
        """
        expect = """Error on line 2 col 30: bool"""
        self.assertTrue(TestParser.test(input, expect, 283))
        

    def test84(self):
        input = """ 
            vvtWKqch2, eUkbFTQVw:float;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 284))
        

    def test85(self):
        input = """ 
             sGzjvlUge, IhcERyqGZ, SZVDdcwrN : bool = BSZSBIdFI == xhWaFgGgJ,QqVFtERLG == 913,vgc6gZSJY > -907 ;
        """
        expect = """Error on line 2 col 47: bool"""
        self.assertTrue(TestParser.test(input, expect, 285))
        

    def test86(self):
        input = """ 
        mdRe2OYKc : function  string (ClProGWDX:string, bZPlYgHtq:integer) inherit OrpsNUbuz {
             return O6koCBrmc > -211;
         }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 286))
        

    def test87(self):
        input = """ 
            WKdYgvrTt, dhUTkloVQ, fiLNFipIe : float = LnYoiyYpr >= _1_*OoeEixaYD + 629, {1,2,3}, "hello\\"world\\"" ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))
        

    def test88(self):
        input = """ 
            mpkKNxSqe, LpgofFs4e : string = -622 > 814,KxnYX5Pzt >= "mBc6m" ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 288))
        

    def test89(self):
        input = """ 
             IZHthNCgV:float;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 289))
        

    def test90(self):
        input = """ 
            4lOYaSEPl, Wq5zomqwR:bool;
        """
        expect = """Error on line 2 col 12: 4"""
        self.assertTrue(TestParser.test(input, expect, 290))
        

    def test91(self):
        input = """ 
        ZRzoWPdnj : function  float (gI88wGAPm:string){
            nBkzFSeDj = CWEKsKjip(qVex8sapu != "OIHPj",ryJoZgjhu > 477) < "BYOq4";
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 291))
        

    def test92(self):
        input = """ 
            BsRCTPAAt:bool;
        """
        expect = """Error on line 2 col 22: bool"""
        self.assertTrue(TestParser.test(input, expect, 292))
        

    def test93(self):
        input = """ 
        main : function  bool ( IgkpHtFkf:float ) inherit twZzJOmAB {
             OxT8qePFi:void;
        }
        """
        expect = """Error on line 2 col 25: bool"""
        self.assertTrue(TestParser.test(input, expect, 293))
        

    def test94(self):
        input = """ 
        main : function  void ( zXj5zrjTi:integer ) inherit NitnmwZEY {
             bwmUW2clD = A6brMCwbM >= "X\\'k\\t6";
        }

        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 294))
        

    def test95(self):
        input = """ 
        main : function  integer ( PxRPBzeQ7:integer, out qBk3lx3jH:float, out FvLziXwJo:float, qwqPErqbf:string ) inherit VSmgoSkVm {
            NTbZIVteN = 979 < 993;
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 295))
        

    def test96(self):
        input = """ 
             swytrnjUF : void = lGSBYGJgJ >= -003,iklUnomKB(JjxIQuWRi == _75,dQF6QWJmB == -982) < "HxnRu" ;
        """
        expect = """Error on line 2 col 25: void"""
        self.assertTrue(TestParser.test(input, expect, 296))
        

    def test97(self):
        input = """ 
        lVAuLrqDZ : function  string (inherit out UMhKL4xEV:integer){
            continue;
            for (udM6kBJiX=-124, kDVsZHYeT > tUrjHXEP2, QZX3Rjneb+-214)
            tJckJBAAc = BHQqd9HTy(FSemFBxy3 < "okW6o",ZxwoJAlXB == rIkPoeV8Z) > "NS\\'\\"K";
        }

        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 297))
        

    def test98(self):
        input = """ 
    main : function  integer ( PRePBOs4t:string ) inherit ETgcJPDgn {
        for (ACIopKahZ=721, VjMjP4mlY == 840, 159+-514)
            fjPgpVPFu = 4AmqiuaPD == -674;
        return 7QYoBaOBI > "Yq8V7";
    }
        """
        expect = """Error on line 4 col 25: AmqiuaPD"""
        self.assertTrue(TestParser.test(input, expect, 298))
        

    def test99(self):
        input = """ 
            Lzj3Kokx0:integer;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 299))
        

    def test100(self):
        input = """ 
         LpjzGPwCo : float = zzMHIlqRf != "vF\\nG\\'" ;
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 300))

##############################################################################
    
    # def testprogram22(self):
    #     input = """a,b,c : float = 2,foo(foo(3+ 5)), 3 *9, 3+4;"""
    #     expect = "Error on line 1 col 38: ,"
    #     self.assertTrue(TestParser.test(input, expect, 222))   
    


    # def testprogram54(self):
    #     input = """main : function void() {
    #                 for (a[i] = 2, i < 2, i * 2) a[i,2] = 3;
    #             }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 254))


