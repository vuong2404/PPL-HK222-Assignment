import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    #     def test_short_vardecl(self):
    #         input = """a: array[3,4,5] of integer = c;"""
    #         expect = str(Program([VarDecl("a", ArrayType([3,4,5], IntegerType()), Id("c"))]))
    #         self.assertTrue(TestAST.test(input, expect, 300))

    #     def test_full_vardecl(self):
    #         input = """x, y, z: integer = 1, 2, 3;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, IntegerLit(1))
    # 	VarDecl(y, IntegerType, IntegerLit(2))
    # 	VarDecl(z, IntegerType, IntegerLit(3))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 301))

    #     def test_vardecls(self):
    #         input = """x, y, z: integer = 1, 2, 3;
    #         a, b: float;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, IntegerLit(1))
    # 	VarDecl(y, IntegerType, IntegerLit(2))
    # 	VarDecl(z, IntegerType, IntegerLit(3))
    # 	VarDecl(a, FloatType)
    # 	VarDecl(b, FloatType)
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 302))

    #     def test_simple_program(self):
    #         """Simple program"""
    #         input = """main: function void () {
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 303))

    #     def test_more_complex_program(self):
    #         """More complex program"""
    #         input = """main: function void () {
    #             printInteger(4);
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 304))

    #     def test_more_complex_program2(self):
    #         """More complex program"""
    #         input = """
    # foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

    # main: function void () {
    #      printInteger(4);
    # }"""
    #         expect = """Program([
    # 	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 305))

    # test varible declaration
    def test1(self):
        input = """kaBoLTRLe:float;"""
        expect = """Program([
	VarDecl(kaBoLTRLe, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test2(self):
        input = """dDDLJUlVn, tewqOOz2X, QarWYDmCs:boolean;"""
        expect = """Program([
	VarDecl(dDDLJUlVn, BooleanType)
	VarDecl(tewqOOz2X, BooleanType)
	VarDecl(QarWYDmCs, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test3(self):
        input = """ovalOkHdJ:string;"""
        expect = """Program([
	VarDecl(ovalOkHdJ, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test4(self):
        input = """wduH3Uqoc, ZSliw2f9T, SjOiHOwvK:integer;"""
        expect = """Program([
	VarDecl(wduH3Uqoc, IntegerType)
	VarDecl(ZSliw2f9T, IntegerType)
	VarDecl(SjOiHOwvK, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test5(self):
        input = """PpveyeIjJ: array[5] of integer;"""
        expect = """Program([
	VarDecl(PpveyeIjJ, ArrayType([5], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test6(self):
        input = """EhrJHKzeO, OLp5RUAbd:void;"""
        expect = """Program([
	VarDecl(EhrJHKzeO, VoidType)
	VarDecl(OLp5RUAbd, VoidType)
])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test7(self):
        input = """EhrJHKzeO, OLp5RUAbd:auto;"""
        expect = """Program([
	VarDecl(EhrJHKzeO, AutoType)
	VarDecl(OLp5RUAbd, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test8(self):
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(4))
	VarDecl(c, IntegerType, IntegerLit(6))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test9(self):
        input = """a, b: array [5,2_2] of integer = {1,2,3,4}, {1,2,3,4};"""
        expect = """Program([
	VarDecl(a, ArrayType([5, 22], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
	VarDecl(b, ArrayType([5, 22], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test10(self):
        input = """a, b: array [1_522] of integer = 3,4;"""
        expect = """Program([
	VarDecl(a, ArrayType([1522], IntegerType), IntegerLit(3))
	VarDecl(b, ArrayType([1522], IntegerType), IntegerLit(4))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))

    def test11(self):
        input = """a,b,c: string = "hello", "hello, World", "hello" ;"""
        expect = """Program([
	VarDecl(a, StringType, StringLit(hello))
	VarDecl(b, StringType, StringLit(hello, World))
	VarDecl(c, StringType, StringLit(hello))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test12(self):
        input = """a,b,c: string = a == b , a + 1, c + d;"""
        expect = """Program([
	VarDecl(a, StringType, BinExpr(==, Id(a), Id(b)))
	VarDecl(b, StringType, BinExpr(+, Id(a), IntegerLit(1)))
	VarDecl(c, StringType, BinExpr(+, Id(c), Id(d)))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test13(self):
        input = """dvtNu, GkXYLy, CtWWg, BiMJ9, hgJvA, DohAb: boolean = OZTnq > "T3bce",S2ciZVlbO != 979,cXt1Dpk3l - _85 - 2_3,-438-_23-332209,585,-847-416-753 ;"""
        expect = """Program([
	VarDecl(dvtNu, BooleanType, BinExpr(>, Id(OZTnq), StringLit(T3bce)))
	VarDecl(GkXYLy, BooleanType, BinExpr(!=, Id(S2ciZVlbO), IntegerLit(979)))
	VarDecl(CtWWg, BooleanType, BinExpr(-, BinExpr(-, Id(cXt1Dpk3l), Id(_85)), IntegerLit(23)))
	VarDecl(BiMJ9, BooleanType, BinExpr(-, BinExpr(-, UnExpr(-, IntegerLit(438)), Id(_23)), IntegerLit(332209)))
	VarDecl(hgJvA, BooleanType, IntegerLit(585))
	VarDecl(DohAb, BooleanType, BinExpr(-, BinExpr(-, UnExpr(-, IntegerLit(847)), IntegerLit(416)), IntegerLit(753)))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test14(self):
        input = """ gSMqQEvNS, ZXEcQaq : string = phcMklS8X != pEWZQjukz,QzqUlwQtU == 265 ; """
        expect = """Program([
	VarDecl(gSMqQEvNS, StringType, BinExpr(!=, Id(phcMklS8X), Id(pEWZQjukz)))
	VarDecl(ZXEcQaq, StringType, BinExpr(==, Id(QzqUlwQtU), IntegerLit(265)))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test15(self):
        input = """ YGAOlFxv1 : string = mxZBZaMWK >= "k5z6\\'" ; """
        expect = """Program([
	VarDecl(YGAOlFxv1, StringType, BinExpr(>=, Id(mxZBZaMWK), StringLit(k5z6\\')))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    # test simple function declaration

    def test16(self):
        input = """ 
        // main function
        main : function void() {
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test17(self):
        input = """ 
        main : function integer()  {
           printLn("@", "Hello world", 23342424);
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(printLn, StringLit(@), StringLit(Hello world), IntegerLit(23342424))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test18(self):
        input = """ 
        main : function void (a: integer)  {
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test19(self):
        input = """ 
        main : function float (a: integer, b: float, c: boolean)  {
           a = b + c ;
           {
               temp: string = a;
               a = b ;
               b= temp ;
           }
        }
        """
        expect = """Program([
	FuncDecl(main, FloatType, [Param(a, IntegerType), Param(b, FloatType), Param(c, BooleanType)], None, BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(b), Id(c))), BlockStmt([VarDecl(temp, StringType, Id(a)), AssignStmt(Id(a), Id(b)), AssignStmt(Id(b), Id(temp))])]))
])"""

        self.assertTrue(TestAST.test(input, expect, 319))

    def test20(self):
        input = """ 
        main : function auto (a: integer) inherit abc {
            return 212*c+b/a>c+a::b||a;
        }
        """
        expect = """Program([
	FuncDecl(main, AutoType, [Param(a, IntegerType)], abc, BlockStmt([ReturnStmt(BinExpr(::, BinExpr(>, BinExpr(+, BinExpr(*, IntegerLit(212), Id(c)), BinExpr(/, Id(b), Id(a))), BinExpr(+, Id(c), Id(a))), BinExpr(||, Id(b), Id(a))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test21(self):
        input = """
        fact: function integer (n: integer)  {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        /* inc: function void (out n: integer, delta: integer) {
            n = n + delta;
        } */
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test22(self):
        input = """
        sum: function void(out ressult:integer,inherit a: integer,inherit out b: integer) inherit abc{
           result =  a + b ; 
        }
        main: function void() {
            result,a,b: integer = 0, 10, 19 ;
            sum(result, a, b) ;
            printInteger(result) ; 
        }
        """
        expect = """Program([
	FuncDecl(sum, VoidType, [OutParam(ressult, IntegerType), InheritParam(a, IntegerType), InheritOutParam(b, IntegerType)], abc, BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(result, IntegerType, IntegerLit(0)), VarDecl(a, IntegerType, IntegerLit(10)), VarDecl(b, IntegerType, IntegerLit(19)), CallStmt(sum, Id(result), Id(a), Id(b)), CallStmt(printInteger, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test23(self):
        input = """ 
        ooMWtvLEh: function void () {
            if (___ >= 1_7)
            return qBWIBTwxF;
        }
        """
        expect = """Program([
	FuncDecl(ooMWtvLEh, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>=, Id(___), IntegerLit(17)), ReturnStmt(Id(qBWIBTwxF)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test24(self):
        input = """ 
        hjj9pfFxl : function  integer (inherit out jfigupugy:integer, out fDyvnqIxV:string) inherit TfcV9WZzb {
            nWHQpnfW = BwsvaDRoy > DxNrGYIKs;
        }
        """
        expect = """Program([
	FuncDecl(hjj9pfFxl, IntegerType, [InheritOutParam(jfigupugy, IntegerType), OutParam(fDyvnqIxV, StringType)], TfcV9WZzb, BlockStmt([AssignStmt(Id(nWHQpnfW), BinExpr(>, Id(BwsvaDRoy), Id(DxNrGYIKs)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    def test25(self):
        input = """ 
        foo : function string ( inherit out OMsQMycjS:float ) inherit yJyjJjUPU {
            a2 = a + b ;
        }
        """
        expect = """Program([
	FuncDecl(foo, StringType, [InheritOutParam(OMsQMycjS, FloatType)], yJyjJjUPU, BlockStmt([AssignStmt(Id(a2), BinExpr(+, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test26(self):
        input = """ 
        check : function  boolean ( str:string, out piq1PC3Aj:integer ) inherit String {
            return len(str) <= len("\\"eDfY");
        }
        """
        expect = """Program([
	FuncDecl(check, BooleanType, [Param(str, StringType), OutParam(piq1PC3Aj, IntegerType)], String, BlockStmt([ReturnStmt(BinExpr(<=, FuncCall(len, [Id(str)]), FuncCall(len, [StringLit(\\"eDfY)])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    # test expr
    def test27(self):
        input = """ 
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = a + b ;
            c = c * 4 ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType), AssignStmt(Id(c), BinExpr(+, Id(a), Id(b))), AssignStmt(Id(c), BinExpr(*, Id(c), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test28(self):
        input = """ 
        sum: function integer(a: integer, b: integer) {
            c = a + b ; 
            return c ; 
        }
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            c = sum(a,b) + 40 ;
            d = d - c - (b - a) * b * c * d / a / b;
        }
        """
        expect = """Program([
	FuncDecl(sum, IntegerType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(a), Id(b))), ReturnStmt(Id(c))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType), AssignStmt(Id(c), BinExpr(+, FuncCall(sum, [Id(a), Id(b)]), IntegerLit(40))), AssignStmt(Id(d), BinExpr(-, BinExpr(-, Id(d), Id(c)), BinExpr(/, BinExpr(/, BinExpr(*, BinExpr(*, BinExpr(*, BinExpr(-, Id(b), Id(a)), Id(b)), Id(c)), Id(d)), Id(a)), Id(b))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test29(self):
        input = """ 
        main : function  void () {
            a : array [5] of integer = {1,2,3,4} ;
            b = a[0] ;
            c = a[1] ;
            a[2] = b + c ;
            d[1,2,3] = a[1,2,3] + a[b] ;
            printInt(a[1,2,3,4]) ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)])), AssignStmt(Id(b), ArrayCell(a, [IntegerLit(0)])), AssignStmt(Id(c), ArrayCell(a, [IntegerLit(1)])), AssignStmt(ArrayCell(a, [IntegerLit(2)]), BinExpr(+, Id(b), Id(c))), AssignStmt(ArrayCell(d, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayCell(a, [Id(b)]))), CallStmt(printInt, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test30(self):
        input = """ 
        main : function  void () {
            a: integer = 1 ;
            b : integer = 2 ;
            c: integer ;
            a = b>c ;
            e , f : boolean = a[0,0] > b + sum(a,b) || b , a - b > !c + d*e/f || c +d + a;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType), AssignStmt(Id(a), BinExpr(>, Id(b), Id(c))), VarDecl(e, BooleanType, BinExpr(>, ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), BinExpr(||, BinExpr(+, Id(b), FuncCall(sum, [Id(a), Id(b)])), Id(b)))), VarDecl(f, BooleanType, BinExpr(>, BinExpr(-, Id(a), Id(b)), BinExpr(||, BinExpr(+, UnExpr(!, Id(c)), BinExpr(/, BinExpr(*, Id(d), Id(e)), Id(f))), BinExpr(+, BinExpr(+, Id(c), Id(d)), Id(a)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test31(self):
        input = """ 
        main : function  void () {
            a: string = 1.e2 ;
            b : auto ;
            c,d,e,f: integer = sum(a), len(a), a*b/c||a&&d, a + b - c * d /e ;
            e = a() + b(b(),c());
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, FloatLit(100.0)), VarDecl(b, AutoType), VarDecl(c, IntegerType, FuncCall(sum, [Id(a)])), VarDecl(d, IntegerType, FuncCall(len, [Id(a)])), VarDecl(e, IntegerType, BinExpr(&&, BinExpr(||, BinExpr(/, BinExpr(*, Id(a), Id(b)), Id(c)), Id(a)), Id(d))), VarDecl(f, IntegerType, BinExpr(-, BinExpr(+, Id(a), Id(b)), BinExpr(/, BinExpr(*, Id(c), Id(d)), Id(e)))), AssignStmt(Id(e), BinExpr(+, FuncCall(a, []), FuncCall(b, [FuncCall(b, []), FuncCall(c, [])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test32(self):
        input = """ 
        main : function  void () {
            a: integer = 1_243234;
            b : float = 2e-1 ;
            c: float = 12.5E-6 ;
            c = a + b ;
            c = c * 4 ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1243234)), VarDecl(b, FloatType, FloatLit(0.2)), VarDecl(c, FloatType, FloatLit(1.25e-05)), AssignStmt(Id(c), BinExpr(+, Id(a), Id(b))), AssignStmt(Id(c), BinExpr(*, Id(c), IntegerLit(4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test33(self):
        input = """ 
        main : function  void () {
            if (a == 5) {
                a = a + 1 ;
            }
        }
    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test34(self):
        input = """ 
        main : function  void () {
            if (a == 5) 
               return a ;
        }
    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), ReturnStmt(Id(a)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test35(self):
        input = """ 
        main : function  void () {
            if (a == 5) 
              return a ;
            else return b ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), ReturnStmt(Id(a)), ReturnStmt(Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test36(self):
        input = """ 
        main : function  void () {
                if (a == 5) 
                  if (b == 8)
                    if (c == 10)
                        return a ;
                    else return b;
                else return c;
        }
    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), IfStmt(BinExpr(==, Id(b), IntegerLit(8)), IfStmt(BinExpr(==, Id(c), IntegerLit(10)), ReturnStmt(Id(a)), ReturnStmt(Id(b))), ReturnStmt(Id(c))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test37(self):
        input = """ 
        main : function void () {
                if (a == 5) 
                   { 
                        a = a + 1 ;
                        return a ;
                        if (c == 1) 
                            return 1 ;
                            return 2 ;
                            return 3 ; {
                                a = 4 ;
                                c = 5 ;
                            }
                    }
                else return b ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), ReturnStmt(Id(a)), IfStmt(BinExpr(==, Id(c), IntegerLit(1)), ReturnStmt(IntegerLit(1))), ReturnStmt(IntegerLit(2)), ReturnStmt(IntegerLit(3)), BlockStmt([AssignStmt(Id(a), IntegerLit(4)), AssignStmt(Id(c), IntegerLit(5))])]), ReturnStmt(Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test38(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([5], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), Id(i))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7)])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test39(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([5], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), BinExpr(||, Id(a), Id(b))), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), Id(i))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7)])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test40(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([5], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(::, BinExpr(<, Id(i), Id(str)), StringLit(hello)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), Id(i))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7)])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test41(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([5], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), Id(i))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6), IntegerLit(7)])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test42(self):
        input = """ 
        sumOfArray : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i + 1) 
                result = result + i ; 
                print(result) ;
            for (i = 3, i > 0 ,  i - 1) {
                print(i) ;
                i =  i + 1 ;
            }
        }
        """
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([5], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), Id(i)))), CallStmt(print, Id(result)), ForStmt(AssignStmt(Id(i), IntegerLit(3)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(print, Id(i)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test43(self):
        input = """ 
        main : function void (a: array [5] of integer, out result:integer) inherit Array {
            if (result != 0 ) result = 0 ;
            for (i  =  0 , i < len(a) , i + 1) 
                for (j=0, j < i , j + 1)
                    print(i,j);
                    pritn(i);
        }
    
    
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, ArrayType([5], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(i)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(print, Id(i), Id(j)))), CallStmt(pritn, Id(i))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test44(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([2, 2], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(>, Id(j), FuncCall(len, [ArrayCell(a, [IntegerLit(0)])])), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(a, [Id(i), Id(j)])))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    def test45(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([2, 2], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(>, Id(j), FuncCall(len, [ArrayCell(a, [IntegerLit(0)])])), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(a, [Id(i), Id(j)])))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test46(self):
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
        expect = """Program([
	FuncDecl(sumOfArray, VoidType, [Param(a, ArrayType([2, 2], IntegerType)), OutParam(result, IntegerType)], Array, BlockStmt([IfStmt(BinExpr(!=, Id(result), IntegerLit(0)), AssignStmt(Id(result), IntegerLit(0))), VarDecl(countLoop, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(countLoop), BinExpr(+, Id(countLoop), IntegerLit(1))), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(>, Id(j), FuncCall(len, [ArrayCell(a, [IntegerLit(0)])])), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(a, [Id(i), Id(j)])))]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test47(self):
        input = """
        main: function void() {
            result = 0 ;
            a: array [2,2] of integer = {{1,2}, {2,3}} ;
            sumOfArray(a, result) ;
            printInt(result) ;
            a[1,1] = a + b + c * d *e *f /g;
            for (i = a[0], i < len(a) , i + 1) {
                if (i == 312_4234) print(i) ;
                else i(a[1,2,3]) ;
                print(a[0]) ;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), BinExpr(+, BinExpr(+, Id(a), Id(b)), BinExpr(/, BinExpr(*, BinExpr(*, BinExpr(*, Id(c), Id(d)), Id(e)), Id(f)), Id(g)))), ForStmt(AssignStmt(Id(i), ArrayCell(a, [IntegerLit(0)])), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(3124234)), CallStmt(print, Id(i)), CallStmt(i, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), CallStmt(print, ArrayCell(a, [IntegerLit(0)]))]))]))
])"""   
        self.assertTrue(TestAST.test(input, expect, 347))
    
    def test48(self):
        input = """
        main: function void() {
            result = 0 ;
            a: array [2,2] of integer = {{1,2}, {2,3}} ;
            sumOfArray(a, result) ;
            printInt(result) ;
            a[1,1] = a + b + c * d *e *f /g;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result)), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), BinExpr(+, BinExpr(+, Id(a), Id(b)), BinExpr(/, BinExpr(*, BinExpr(*, BinExpr(*, Id(c), Id(d)), Id(e)), Id(f)), Id(g))))]))
])"""   
        self.assertTrue(TestAST.test(input, expect, 348))
    
    def test49(self):
        input = """
        main: function void() {
            result = 0 ;
            for (i = a[0], i < len(a) , i + 1) {
                a ,b , c: string = "fafafa", a[12,3] , b ;
                if (i == 312_4234) print(i);
                else i(a[1,2,3]) ;
                print(a[0]) ;
                break ; 
                continue ;
            }
            a = a::b + 1 ;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), ForStmt(AssignStmt(Id(i), ArrayCell(a, [IntegerLit(0)])), BinExpr(<, Id(i), FuncCall(len, [Id(a)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(a, StringType, StringLit(fafafa)), VarDecl(b, StringType, ArrayCell(a, [IntegerLit(12), IntegerLit(3)])), VarDecl(c, StringType, Id(b)), IfStmt(BinExpr(==, Id(i), IntegerLit(3124234)), CallStmt(print, Id(i)), CallStmt(i, ArrayCell(a, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), CallStmt(print, ArrayCell(a, [IntegerLit(0)])), BreakStmt(), ContinueStmt()])), AssignStmt(Id(a), BinExpr(::, Id(a), BinExpr(+, Id(b), IntegerLit(1))))]))
])"""   
        self.assertTrue(TestAST.test(input, expect, 349))
        
    def test50(self):
        input = """
        main: function void() {
            result = 0 ;
            a: array [2,2] of integer = {{1,2}, {2,3}} ;
            sumOfArray(a, result) ;
            printInt(result) ;
            {
                a , b , c: string = a[1,2], a*b , b % a;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(3)])])), CallStmt(sumOfArray, Id(a), Id(result)), CallStmt(printInt, Id(result)), BlockStmt([VarDecl(a, StringType, ArrayCell(a, [IntegerLit(1), IntegerLit(2)])), VarDecl(b, StringType, BinExpr(*, Id(a), Id(b))), VarDecl(c, StringType, BinExpr(%, Id(b), Id(a)))])]))
])"""   
        self.assertTrue(TestAST.test(input, expect, 350))

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
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit()), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), AssignStmt(Id(result), BinExpr(::, Id(result), ArrayCell(s, [Id(i)]))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test52(self):
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
            printInt(substr) ; 
        }
        """
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit()), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), AssignStmt(Id(result), BinExpr(::, Id(result), ArrayCell(s, [Id(i)]))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test53(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            while (i <= (len(s) - 1)) {
                if ((i >= start) && (i <= end))
                    a = toString(s[i]) ;
                else 
                    i = i + 1 ;
            }
            return result ;
        }
        main: function void() {
            result = 0 ;
            s: string = "Hello world" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ; 
        }
    
        """
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit()), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), AssignStmt(Id(a), FuncCall(toString, [ArrayCell(s, [Id(i)])])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))

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
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit()), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), BlockStmt([VarDecl(a, StringType, FuncCall(toString, [ArrayCell(s, [Id(i)])])), AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))]), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world!)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))

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
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit()), DoWhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), BlockStmt([VarDecl(a, StringType, FuncCall(toString, [ArrayCell(s, [Id(i)])])), AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))]), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world!)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test56(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "fefafaw" ;
            do {
                if ((i >= start) && (i <= end)) { 
                    a: integer ;
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                }
                else 
                    i = i + 1 ;
            } while ((i <= len(s) - 1)) ;
            return result ;
        }
        """
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit(fefafaw)), DoWhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), BlockStmt([VarDecl(a, IntegerType), VarDecl(a, StringType, FuncCall(toString, [ArrayCell(s, [Id(i)])])), AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))]), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test57(self):
        input = """ 
        findSubstr : function string (s: string, start: integer, end: integer) inherit String {
            i: integer = 0 ;
            result: string = "" ;
            do 
                {if ((i >= start) && (i <= end)) { 
                    a: string = toString(s[i]) ;
                    result = result + s[i] ;
                }
                else 
                    i = i + 1 ; }
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
        expect = """Program([
	FuncDecl(findSubstr, StringType, [Param(s, StringType), Param(start, IntegerType), Param(end, IntegerType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, StringType, StringLit()), DoWhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>=, Id(i), Id(start)), BinExpr(<=, Id(i), Id(end))), BlockStmt([VarDecl(a, StringType, FuncCall(toString, [ArrayCell(s, [Id(i)])])), AssignStmt(Id(result), BinExpr(+, Id(result), ArrayCell(s, [Id(i)])))]), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world!)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))

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
        expect = """Program([
	FuncDecl(find, StringType, [Param(s, StringType), Param(ch, StringType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, IntegerType, UnExpr(-, IntegerLit(1))), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), Id(d)), BlockStmt([AssignStmt(Id(result), Id(i)), BreakStmt()]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt()]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), VarDecl(s, StringType, StringLit(Hello world!)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))

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
                    continue; 
                }
            }
            return result ;
        }
        """
        expect = """Program([
	FuncDecl(find, StringType, [Param(s, StringType), Param(ch, StringType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, IntegerType, UnExpr(-, IntegerLit(1))), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), Id(d)), BlockStmt([AssignStmt(Id(result), Id(i)), BreakStmt()]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt()]))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))

    def test60(self):
        input = """ 
        find : function string (s: string,ch: string) inherit String {
            i: integer = 0 ;
            result: integer = -1 ;
            while (i <= len(s) - 1) {
                while (i < 1) {
                    {
                        if (s[i] == d) { 
                        result = i ;
                        breaK() ; 
                        }
                        else {
                            i = i + 1 ; 
                            continue ;
                        } 
                    }
                    print(i);
                }
            }
            return result ;
        }
        main: function void() {
            result = 0 ; {
                a = 2 ;
                b = a ;
                a = temp[1] ;
            }
            s: string = "Hello world!" ;
            subtr = findSubtr(s, 0, 5) ;
            printInt(substr) ;
        }
        """
        expect = """Program([
	FuncDecl(find, StringType, [Param(s, StringType), Param(ch, StringType)], String, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(result, IntegerType, UnExpr(-, IntegerLit(1))), WhileStmt(BinExpr(<=, Id(i), BinExpr(-, FuncCall(len, [Id(s)]), IntegerLit(1))), BlockStmt([WhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([BlockStmt([IfStmt(BinExpr(==, ArrayCell(s, [Id(i)]), Id(d)), BlockStmt([AssignStmt(Id(result), Id(i)), CallStmt(breaK, )]), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), ContinueStmt()]))]), CallStmt(print, Id(i))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(result), IntegerLit(0)), BlockStmt([AssignStmt(Id(a), IntegerLit(2)), AssignStmt(Id(b), Id(a)), AssignStmt(Id(a), ArrayCell(temp, [IntegerLit(1)]))]), VarDecl(s, StringType, StringLit(Hello world!)), AssignStmt(Id(subtr), FuncCall(findSubtr, [Id(s), IntegerLit(0), IntegerLit(5)])), CallStmt(printInt, Id(substr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))

    # ramdom testcase

    def test61(self):
        input = """ 
        QzTwgNOAB : function  void (vuyNPU5gd:string, QTaIAPOeH:string){
            aWLohOnWo:float;
            for (QaPcp6Bgt=-393, xNILoTLv > waLauwzFr, -945+394)
                 while (igdEQlzAo >= k2gzstcol) 
                  { 
                     OjZfBbKNk, i6kLoeBqT, meVruOFBb : float = US1sy1G1d > 695, 642432.4324, .e2   ;
                }
        }
        """
        expect = """Program([
	FuncDecl(QzTwgNOAB, VoidType, [Param(vuyNPU5gd, StringType), Param(QTaIAPOeH, StringType)], None, BlockStmt([VarDecl(aWLohOnWo, FloatType), ForStmt(AssignStmt(Id(QaPcp6Bgt), UnExpr(-, IntegerLit(393))), BinExpr(>, Id(xNILoTLv), Id(waLauwzFr)), BinExpr(+, UnExpr(-, IntegerLit(945)), IntegerLit(394)), WhileStmt(BinExpr(>=, Id(igdEQlzAo), Id(k2gzstcol)), BlockStmt([VarDecl(OjZfBbKNk, FloatType, BinExpr(>, Id(US1sy1G1d), IntegerLit(695))), VarDecl(i6kLoeBqT, FloatType, FloatLit(642432.4324)), VarDecl(meVruOFBb, FloatType, FloatLit(0.0))])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))

    def test62(self):
        input = """ 
        eOYtvrJUG : function  float (out YTIjDWw:float) {
            if (jMjL5hzsc >= _37)
                rYiamy = jzaSXMzfw != "\\'zrRu";
        }
        """
        expect = """Program([
	FuncDecl(eOYtvrJUG, FloatType, [OutParam(YTIjDWw, FloatType)], None, BlockStmt([IfStmt(BinExpr(>=, Id(jMjL5hzsc), Id(_37)), AssignStmt(Id(rYiamy), BinExpr(!=, Id(jzaSXMzfw), StringLit(\\'zrRu))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))

    def test63(self):
        input = """ 
        gumCiFlgP : void = pCgXMdc9Z >= 664 ;
        """
        expect = """Program([
	VarDecl(gumCiFlgP, VoidType, BinExpr(>=, Id(pCgXMdc9Z), IntegerLit(664)))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test64(self):
        input = """ 
        zNUBT1a5I : string = FBJ5dxfoH < "mDana" ;
        """
        expect = """Program([
	VarDecl(zNUBT1a5I, StringType, BinExpr(<, Id(FBJ5dxfoH), StringLit(mDana)))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))

    def test65(self):
        input = """ 
        ZovgPbMwK : integer = U7kDjPhZQ > _93 ;
        """
        expect = """Program([
	VarDecl(ZovgPbMwK, IntegerType, BinExpr(>, Id(U7kDjPhZQ), Id(_93)))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))

    def test66(self):
        input = """ 
        XrRvlJIG1, UYDCYwcGf:void;
        """
        expect = """Program([
	VarDecl(XrRvlJIG1, VoidType)
	VarDecl(UYDCYwcGf, VoidType)
])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test67(self):
        input = """ 
        CmEUgpnkq:void;
        """
        expect = """Program([
	VarDecl(CmEUgpnkq, VoidType)
])"""
        self.assertTrue(TestAST.test(input, expect, 367))

    def test68(self):
        input = """ 
      bxvKBRuF6:void;
    
        """
        expect = """Program([
	VarDecl(bxvKBRuF6, VoidType)
])"""
        self.assertTrue(TestAST.test(input, expect, 368))

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
                if (KBEOoNfEZ == 969) {
                 HSZLsNxAs = -63_123 == -345;
                }
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
        expect = """Program([
	FuncDecl(SQZNr6JOY, FloatType, [OutParam(NedsZTMtH, FloatType)], W4QFwM1J3, BlockStmt([ForStmt(AssignStmt(Id(NhfQBlxmW), IntegerLit(146)), BinExpr(<, FuncCall(d6pxmSLCh, [BinExpr(>, Id(Xpfhh7LFC), IntegerLit(65)), BinExpr(>=, IntegerLit(598), Id(_44)), BinExpr(==, Id(dKzLwvNek), IntegerLit(48))]), StringLit(tod\\nQ)), BinExpr(+, Id(fKNqGDGYc), UnExpr(-, IntegerLit(64))), CallStmt(QnVjBrmDD, BinExpr(!=, FuncCall(vbieKp8V2, [BinExpr(<, Id(yVZXv2EhK), Id(__8))]), StringLit(A\\t3zi)))), IfStmt(BinExpr(==, IntegerLit(1), IntegerLit(2)), ReturnStmt(BinExpr(>, Id(kRwazdB4N), Id(_5_)))), ForStmt(AssignStmt(Id(gEi6fQPQB), IntegerLit(425)), BinExpr(>=, Id(qYOnZ3hwi), StringLit(hPUJa)), BinExpr(+, Id(qNpoRODYk), UnExpr(-, IntegerLit(638))), BreakStmt()), DoWhileStmt(BinExpr(==, IntegerLit(1), IntegerLit(1)), BlockStmt([ContinueStmt(), VarDecl(RPNq9nmQP, IntegerType), ForStmt(AssignStmt(Id(ocPVclnMe), Id(_)), BinExpr(<, Id(klFUkqweP), Id(jWICdQ2CQ)), BinExpr(-, Id(sXYMDAjia), IntegerLit(99)), AssignStmt(Id(mfVpPkzTY), BinExpr(==, Id(xusb1AWu), IntegerLit(188)))), AssignStmt(Id(yBPgOgYSC), BinExpr(==, Id(DdNwSxsmA), UnExpr(-, IntegerLit(653)))), VarDecl(rNDHXKOsd, BooleanType, BinExpr(>=, Id(NQcJmdWaP), UnExpr(-, Id(__)))), ForStmt(AssignStmt(Id(HiTlfTpMe), IntegerLit(781)), BinExpr(<, Id(lKWNHUrPP), UnExpr(-, IntegerLit(137))), BinExpr(+, UnExpr(-, IntegerLit(25)), UnExpr(-, IntegerLit(13))), BreakStmt()), ForStmt(AssignStmt(Id(BRnXVp5jf), UnExpr(-, IntegerLit(532))), BinExpr(>=, Id(gdKobkUKF), UnExpr(-, IntegerLit(30))), BinExpr(+, Id(_12), UnExpr(-, IntegerLit(276))), AssignStmt(Id(ROhemMlFf), BinExpr(==, IntegerLit(452), UnExpr(-, IntegerLit(640))))), AssignStmt(Id(b7zYBtH8Q), BinExpr(!=, Id(TGwqX0ZYr), StringLit(q0YeF))), AssignStmt(Id(gyrVSjPLL), BinExpr(>, Id(kXqgyNmdu), IntegerLit(87))), AssignStmt(Id(qHK0JAHAU), BinExpr(>=, Id(eSoCE7TDt), UnExpr(-, IntegerLit(828)))), IfStmt(BinExpr(==, Id(KBEOoNfEZ), IntegerLit(969)), BlockStmt([AssignStmt(Id(HSZLsNxAs), BinExpr(==, UnExpr(-, IntegerLit(63123)), UnExpr(-, IntegerLit(345))))])), AssignStmt(Id(AdMJWZpyY), BinExpr(>, Id(ExVUnyC9), StringLit(yGN1y))), AssignStmt(Id(JxXXIJUsG), BinExpr(>=, Id(mccZoXdJP), Id(lrnxrVNcF))), IfStmt(BinExpr(>=, Id(xmCf0MWaK), IntegerLit(15)), AssignStmt(Id(fDchDmwrH), BinExpr(>, UnExpr(-, IntegerLit(935)), UnExpr(-, IntegerLit(398))))), ForStmt(AssignStmt(Id(QDXdeeZBo), IntegerLit(578)), BinExpr(<, Id(jsygghYqP), IntegerLit(550)), BinExpr(+, IntegerLit(458), UnExpr(-, IntegerLit(55))), ForStmt(AssignStmt(Id(uW8c6rQDY), UnExpr(-, IntegerLit(330))), BinExpr(>, Id(CcvvtHjnA), IntegerLit(355)), BinExpr(-, Id(wKl9DiNnE), IntegerLit(83)), BreakStmt())), AssignStmt(Id(CZCw8cUf), BinExpr(>, Id(LPylsYZrd), UnExpr(-, IntegerLit(682)))), VarDecl(IuizFfhrq, BooleanType), IfStmt(BinExpr(!=, Id(uczTlZWJH), IntegerLit(72)), CallStmt(irJTIvhDm, BinExpr(>, IntegerLit(322), IntegerLit(321)))), AssignStmt(Id(GPxYKhqnw), BinExpr(>, Id(Agu4lEcHy), StringLit(8J\\ts9))), IfStmt(BinExpr(==, Id(aLIrfQsK3), IntegerLit(680)), BlockStmt([AssignStmt(Id(tSBSXfUg), BinExpr(>, Id(SoyTBUUxp), StringLit(qFiUV))), AssignStmt(Id(RBLIjgAJI), BinExpr(!=, Id(FxNygjJzH), UnExpr(-, IntegerLit(925)))), CallStmt(OJZV9xycB, BinExpr(>, Id(zRgEknsut), StringLit(gqyVu))), AssignStmt(Id(ZVJcNkYmA), BinExpr(>=, Id(PRhMHgujf), IntegerLit(310)))]))])), ForStmt(AssignStmt(Id(p9FnpJc4j), UnExpr(-, IntegerLit(657))), BinExpr(!=, Id(lkJVLdvi7), IntegerLit(7322)), BinExpr(-, Id(NZGBdAt6K), IntegerLit(15)), BreakStmt()), AssignStmt(Id(vpbcvQCyW), BinExpr(>, Id(UUqfdf0Cp), StringLit(\\t\\'toR))), ReturnStmt(BinExpr(>, Id(aCygSBmlc), StringLit(vK4Cy)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))

    def test70(self):
        input = """ 
         cywr1OjLX , b: integer = zNIcmcOOv == -451,skZOr5KxB >= 101 ;
        """
        expect = """Program([
	VarDecl(cywr1OjLX, IntegerType, BinExpr(==, Id(zNIcmcOOv), UnExpr(-, IntegerLit(451))))
	VarDecl(b, IntegerType, BinExpr(>=, Id(skZOr5KxB), IntegerLit(101)))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))

    def test71(self):
        input = """ 
        abczyz : function  float ( inherit out e9XgkiuWr:integer, WEceApeFD:string, inherit out fFQiZPzNi:integer, out pjHUhUpkl:string ) inherit VYLtCaatH {
             return ltOPmdJQP(XfC5CRYcb(NwWTHICwq < 846) >= "JD7Yu",zEBkvdbBi < "GMASN",aeemhejkH >= 949) != "VQ3vb";
        }
        """
        expect = """Program([
	FuncDecl(abczyz, FloatType, [InheritOutParam(e9XgkiuWr, IntegerType), Param(WEceApeFD, StringType), InheritOutParam(fFQiZPzNi, IntegerType), OutParam(pjHUhUpkl, StringType)], VYLtCaatH, BlockStmt([ReturnStmt(BinExpr(!=, FuncCall(ltOPmdJQP, [BinExpr(>=, FuncCall(XfC5CRYcb, [BinExpr(<, Id(NwWTHICwq), IntegerLit(846))]), StringLit(JD7Yu)), BinExpr(<, Id(zEBkvdbBi), StringLit(GMASN)), BinExpr(>=, Id(aeemhejkH), IntegerLit(949))]), StringLit(VQ3vb)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))

    def test72(self):
        input = """
         ZaMTvuSQB, FLKljqK6A : boolean = MIktlKXeg(KHGfDvEpQ >= "CByxr") == "XJWWO" , 43124;
        """
        expect = """Program([
	VarDecl(ZaMTvuSQB, BooleanType, BinExpr(==, FuncCall(MIktlKXeg, [BinExpr(>=, Id(KHGfDvEpQ), StringLit(CByxr))]), StringLit(XJWWO)))
	VarDecl(FLKljqK6A, BooleanType, IntegerLit(43124))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))

    def test73(self):
        input = """
        main : function  float ( inherit out xxrRpmn9v:float, out dr4hE0KO5:string ) inherit xHDmbATrr {
            break;
            MUcczyWVC = Aol0ZSZKf < 473;
        }

        """
        expect = """Program([
	FuncDecl(main, FloatType, [InheritOutParam(xxrRpmn9v, FloatType), OutParam(dr4hE0KO5, StringType)], xHDmbATrr, BlockStmt([BreakStmt(), AssignStmt(Id(MUcczyWVC), BinExpr(<, Id(Aol0ZSZKf), IntegerLit(473)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))

    def test74(self):
        input = """
          IjRzmSpGy : string = iFvFtLejK >= SDtEJEFuV ;
        """
        expect = """Program([
	VarDecl(IjRzmSpGy, StringType, BinExpr(>=, Id(iFvFtLejK), Id(SDtEJEFuV)))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    def test75(self):
        input = """
        YLKpfAUkC : function  float (ULQRfuoRb:string) inherit AWW0TYqJW {
             while (WWAcGS58C == vfLkEQmDD)
                 while (N1jNxtOkU(rhSFE8wPK == 592) < "OehJj")
                    aXUSZOHGq = Dn0DlQhGD != 498;
                 if (170 != 659)
                    {H8aHMGS2N: float;}

        }
        """
        expect = """Program([
	FuncDecl(YLKpfAUkC, FloatType, [Param(ULQRfuoRb, StringType)], AWW0TYqJW, BlockStmt([WhileStmt(BinExpr(==, Id(WWAcGS58C), Id(vfLkEQmDD)), WhileStmt(BinExpr(<, FuncCall(N1jNxtOkU, [BinExpr(==, Id(rhSFE8wPK), IntegerLit(592))]), StringLit(OehJj)), AssignStmt(Id(aXUSZOHGq), BinExpr(!=, Id(Dn0DlQhGD), IntegerLit(498))))), IfStmt(BinExpr(!=, IntegerLit(170), IntegerLit(659)), BlockStmt([VarDecl(H8aHMGS2N, FloatType)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test76(self):
        input = """
        HKzSuOpwB : function  string (out Y46sILsGL:string){
             VEuUTaAYd, qALCcPbwB:void;
        }
        """
        expect = """Program([
	FuncDecl(HKzSuOpwB, StringType, [OutParam(Y46sILsGL, StringType)], None, BlockStmt([VarDecl(VEuUTaAYd, VoidType), VarDecl(qALCcPbwB, VoidType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))

    def test77(self):
        input = """
        YsBaKPqDO : function  float (inherit out EBjrIFazv:float){
            etBDUv = rCvHpuMkh(Hf4ArivdD < 152) == "VcuLS";
        }
        """
        expect = """Program([
	FuncDecl(YsBaKPqDO, FloatType, [InheritOutParam(EBjrIFazv, FloatType)], None, BlockStmt([AssignStmt(Id(etBDUv), BinExpr(==, FuncCall(rCvHpuMkh, [BinExpr(<, Id(Hf4ArivdD), IntegerLit(152))]), StringLit(VcuLS)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test78(self):
        input = """
            vmmzFSDHH: float;
        """
        expect = """Program([
	VarDecl(vmmzFSDHH, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 378))

    def test79(self):
        input = """
            Lk9KhmSVz, QeVWLd6Vq, gWS85dvnJ : void = JoDJsJfJQ(RDd9RKpRe == -0.95) != "6gpNE",feIxHhHCv == -675 , 2;
        """
        expect = """Program([
	VarDecl(Lk9KhmSVz, VoidType, BinExpr(!=, FuncCall(JoDJsJfJQ, [BinExpr(==, Id(RDd9RKpRe), UnExpr(-, FloatLit(0.95)))]), StringLit(6gpNE)))
	VarDecl(QeVWLd6Vq, VoidType, BinExpr(==, Id(feIxHhHCv), UnExpr(-, IntegerLit(675))))
	VarDecl(gWS85dvnJ, VoidType, IntegerLit(2))
])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test80(self):
        input = """
        main : function  void ( ) {
             for (pDMYsFcRT=-430, wooxtuKmR >= 277, BvYfEnhaL+346)
                continue;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(pDMYsFcRT), UnExpr(-, IntegerLit(430))), BinExpr(>=, Id(wooxtuKmR), IntegerLit(277)), BinExpr(+, Id(BvYfEnhaL), IntegerLit(346)), ContinueStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test81(self):
        input = """
            UqqrNJybN:float;
        """
        expect = """Program([
	VarDecl(UqqrNJybN, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test82(self):
        input = """
            vnyFswZXh, ChHuAcFwC : integer = 4,mFQIbs8W != "bT2\\ts" ;
        """
        expect = """Program([
	VarDecl(vnyFswZXh, IntegerType, IntegerLit(4))
	VarDecl(ChHuAcFwC, IntegerType, BinExpr(!=, Id(mFQIbs8W), StringLit(bT2\\ts)))
])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test83(self):
        input = """
         FjrrhieXg, Ne4CdQa6n:boolean;
        """
        expect = """Program([
	VarDecl(FjrrhieXg, BooleanType)
	VarDecl(Ne4CdQa6n, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test84(self):
        input = """
            vvtWKqch2, eUkbFTQVw:float;
        """
        expect = """Program([
	VarDecl(vvtWKqch2, FloatType)
	VarDecl(eUkbFTQVw, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test85(self):
        input = """
             sGzjvlUge, IhcERyqGZ, SZVDdcwrN : boolean = BSZSBIdFI == xhWaFgGgJ,QqVFtERLG == 913,vgc6gZSJY > -907 ;
        """
        expect = """Program([
	VarDecl(sGzjvlUge, BooleanType, BinExpr(==, Id(BSZSBIdFI), Id(xhWaFgGgJ)))
	VarDecl(IhcERyqGZ, BooleanType, BinExpr(==, Id(QqVFtERLG), IntegerLit(913)))
	VarDecl(SZVDdcwrN, BooleanType, BinExpr(>, Id(vgc6gZSJY), UnExpr(-, IntegerLit(907))))
])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test86(self):
        input = """
        mdRe2OYKc : function  string (ClProGWDX:string, bZPlYgHtq:integer) inherit OrpsNUbuz {
             return O6koCBrmc > -211;
         }
        """
        expect = """Program([
	FuncDecl(mdRe2OYKc, StringType, [Param(ClProGWDX, StringType), Param(bZPlYgHtq, IntegerType)], OrpsNUbuz, BlockStmt([ReturnStmt(BinExpr(>, Id(O6koCBrmc), UnExpr(-, IntegerLit(211))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test87(self):
        input = """
            WKdYgvrTt, dhUTkloVQ, fiLNFipIe : float = LnYoiyYpr >= _1_*OoeEixaYD + 629, {1,2,3}, "hello\\"world\\"" ;
        """
        expect = """Program([
	VarDecl(WKdYgvrTt, FloatType, BinExpr(>=, Id(LnYoiyYpr), BinExpr(+, BinExpr(*, Id(_1_), Id(OoeEixaYD)), IntegerLit(629))))
	VarDecl(dhUTkloVQ, FloatType, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
	VarDecl(fiLNFipIe, FloatType, StringLit(hello\\"world\\"))
])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test88(self):
        input = """
            mpkKNxSqe, LpgofFs4e : string = -622 > 814,KxnYX5Pzt >= "mBc6m" ;
        """
        expect = """Program([
	VarDecl(mpkKNxSqe, StringType, BinExpr(>, UnExpr(-, IntegerLit(622)), IntegerLit(814)))
	VarDecl(LpgofFs4e, StringType, BinExpr(>=, Id(KxnYX5Pzt), StringLit(mBc6m)))
])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test89(self):
        input = """
             IZHthNCgV:float;
        """
        expect = """Program([
	VarDecl(IZHthNCgV, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 389))

    def test90(self):
        input = """
            OYaSEPl, Wq5zomqwR : boolean;
        """
        expect = """Program([
	VarDecl(OYaSEPl, BooleanType)
	VarDecl(Wq5zomqwR, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 390))

    def test91(self):
        input = """
        ZRzoWPdnj : function  float (gI88wGAPm:string){
            nBkzFSeDj = CWEKsKjip(qVex8sapu != "OIHPj",ryJoZgjhu > 477) < "BYOq4";
        }
        """
        expect = """Program([
	FuncDecl(ZRzoWPdnj, FloatType, [Param(gI88wGAPm, StringType)], None, BlockStmt([AssignStmt(Id(nBkzFSeDj), BinExpr(<, FuncCall(CWEKsKjip, [BinExpr(!=, Id(qVex8sapu), StringLit(OIHPj)), BinExpr(>, Id(ryJoZgjhu), IntegerLit(477))]), StringLit(BYOq4)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 391))

    def test92(self):
        input = """
            BsRCTPAAt: auto;
        """
        expect = """Program([
	VarDecl(BsRCTPAAt, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 392))

    def test93(self):
        input = """
        main : function  boolean ( IgkpHtFkf:float ) inherit twZzJOmAB {
             OxT8qePFi:void;
        }
        """
        expect = """Program([
	FuncDecl(main, BooleanType, [Param(IgkpHtFkf, FloatType)], twZzJOmAB, BlockStmt([VarDecl(OxT8qePFi, VoidType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 393))

    def test94(self):
        input = """
        main : function  void ( zXj5zrjTi:integer ) inherit NitnmwZEY {
             bwmUW2clD = A6brMCwbM >= "X\\'k\\t6";
        }

        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(zXj5zrjTi, IntegerType)], NitnmwZEY, BlockStmt([AssignStmt(Id(bwmUW2clD), BinExpr(>=, Id(A6brMCwbM), StringLit(X\\'k\\t6)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 394))

    def test95(self):
        input = """
        main : function  integer ( PxRPBzeQ7:integer, out qBk3lx3jH:float, out FvLziXwJo:float, qwqPErqbf:string ) inherit VSmgoSkVm {
            NTbZIVteN = 979 < 993;
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(PxRPBzeQ7, IntegerType), OutParam(qBk3lx3jH, FloatType), OutParam(FvLziXwJo, FloatType), Param(qwqPErqbf, StringType)], VSmgoSkVm, BlockStmt([AssignStmt(Id(NTbZIVteN), BinExpr(<, IntegerLit(979), IntegerLit(993)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 395))

    def test96(self):
        input = """
             swytrnjUF,fawfaw : void = lGSBYGJgJ >= -0.03,iklUnomKB(JjxIQuWRi == _75,dQF6QWJmB == -982) < "HxnRu" ;
        """
        expect = """Program([
	VarDecl(swytrnjUF, VoidType, BinExpr(>=, Id(lGSBYGJgJ), UnExpr(-, FloatLit(0.03))))
	VarDecl(fawfaw, VoidType, BinExpr(<, FuncCall(iklUnomKB, [BinExpr(==, Id(JjxIQuWRi), Id(_75)), BinExpr(==, Id(dQF6QWJmB), UnExpr(-, IntegerLit(982)))]), StringLit(HxnRu)))
])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test97(self):
        input = """
        lVAuLrqDZ : function  string (inherit out UMhKL4xEV:integer){
            continue;
            for (udM6kBJiX=-124, kDVsZHYeT > tUrjHXEP2, QZX3Rjneb+-214)
            tJckJBAAc = BHQqd9HTy(FSemFBxy3 < "okW6o",ZxwoJAlXB == rIkPoeV8Z) > "NS\\'\\"K";
        }

        """
        expect = """Program([
	FuncDecl(lVAuLrqDZ, StringType, [InheritOutParam(UMhKL4xEV, IntegerType)], None, BlockStmt([ContinueStmt(), ForStmt(AssignStmt(Id(udM6kBJiX), UnExpr(-, IntegerLit(124))), BinExpr(>, Id(kDVsZHYeT), Id(tUrjHXEP2)), BinExpr(+, Id(QZX3Rjneb), UnExpr(-, IntegerLit(214))), AssignStmt(Id(tJckJBAAc), BinExpr(>, FuncCall(BHQqd9HTy, [BinExpr(<, Id(FSemFBxy3), StringLit(okW6o)), BinExpr(==, Id(ZxwoJAlXB), Id(rIkPoeV8Z))]), StringLit(NS\\'\\"K))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 397))

    def test98(self):
        input = """
    main : function  integer ( PRePBOs4t:string ) inherit ETgcJPDgn {
        for (ACIopKahZ=721, VjMjP4mlY == 840, 159 +- 514)
            fjPgpVPFu = mqiuaPD == -674;
        return oBaOBI > "Yq8V7";
    }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(PRePBOs4t, StringType)], ETgcJPDgn, BlockStmt([ForStmt(AssignStmt(Id(ACIopKahZ), IntegerLit(721)), BinExpr(==, Id(VjMjP4mlY), IntegerLit(840)), BinExpr(+, IntegerLit(159), UnExpr(-, IntegerLit(514))), AssignStmt(Id(fjPgpVPFu), BinExpr(==, Id(mqiuaPD), UnExpr(-, IntegerLit(674))))), ReturnStmt(BinExpr(>, Id(oBaOBI), StringLit(Yq8V7)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 398))

    def test99(self):
        input = """
            Lzj3Kokx0:integer;
        """
        expect = """Program([
	VarDecl(Lzj3Kokx0, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 399))

    def test100(self):
        input = """
         LpjzGPwCo : float = zzMHIlqRf != "vF\\nG\\'" ;
        """
        expect = """Program([
	VarDecl(LpjzGPwCo, FloatType, BinExpr(!=, Id(zzMHIlqRf), StringLit(vF\\nG\\')))
])"""
        self.assertTrue(TestAST.test(input, expect, 400)) 
    
    def test_vardecls(self):
        input = """x, y, z: integer = -1, -2, -3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 401))