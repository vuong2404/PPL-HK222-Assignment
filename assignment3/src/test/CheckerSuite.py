import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_short_vardecl0(self):
        input = """x: integer;"""
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_short_vardecl1(self):
        input = """
        a,b: integer;
        c,d: float;
        e,f: string;
        g,h: boolean;
        h,i: integer;
        //main: function void(){}
        """
        expect = """Redeclared Variable: h"""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_short_vardecl2(self):
        input = """
        x,y: array[2] of integer;
        a,b: array[2] of boolean;
        printInteger: integer ;
        //main: function void(){}

        """
        expect = """Redeclared Variable: printInteger"""
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_short_vardecl3(self):
        input = """
        x,y: array[2] of integer;
        a,b: array[2] of boolean;
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_short_vardecl4(self):
        input = """
        x,y: auto;
        """
        expect = """Invalid Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_short_vardecl5(self):
        input = """
        x,y: auto;
        //main: function void() {}
        """
        expect = """Invalid Variable: x"""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_simple_full_vardecl1(self):
        input = """
            a: integer = 1 ;
            b: float = 1 ;
            c: integer = 1.1 ;
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, FloatLit(1.1))"""
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_simple_full_vardecl2(self):
        input = """
            a: boolean = true ;
            b: boolean = 1 ;
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_simple_full_vardecl3(self):
        input = """
            a,b: boolean = true,false ;
            c: string = "abcd" ;
            d: array [2] of integer = {1,2};
            e: auto = 1 ;
            f: integer = e ;
            g: float = f ;
            h: boolean = e ;
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(h, BooleanType, Id(e))"""
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_simple_full_vardecl4(self):
        input = """
            a,b: auto = true,false ;
            c: string = "abcd" ;
            d: array[2] of boolean = {a,b} ;
            e: array[2] of boolean = {1,2};
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(e, ArrayType([2], BooleanType), ArrayLit([IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_simple_full_vardecl5(self):
        input = """
           a,b: array[2,2] of integer = {{1,2},{2,3}}, {{1,2},{2,3}};
           c,d: array[2,2,2] of integer = {a,b}, {b,a} ;
           e: auto = {c,d};
           f: array[2,2,2] of integer = c ;
           g: array[2,2,2] of integer = e ;
           
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(g, ArrayType([2, 2, 2], IntegerType), Id(e))"""
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_simple_full_vardecl6(self):
        input = """
           a: array[2] of integer = {1, 1_1, 1.1};
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(11), FloatLit(1.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_simple_full_vardecl7(self):
        input = """
           a: array[3] of integer = {1, 1_1, 11};
           b: array[3] of float = {1, 1.1, 1.1};
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(1.1), FloatLit(1.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_simple_full_vardecl8(self):
        input = """
           a: array[2,3] of integer = {{1,2,3.5}, {3,4,5}};
           b: array[3] of float = {1, 1.1, 1.1};
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_simple_full_vardecl9(self):
        input = """
           a: array[2,3] of integer = {{1,2,35}, {3,4,5}};
           b: array[3] of float = {1.2, 1.1, 1.1};
           c: array[3] of integer = {12,13,14};
           d: array[3] of integer = {1,2,3} ;
           f: array[2,3] of integer = {c,d};
           e: array[2,3] of integer = {b,c};
        """
        expect = """Illegal array literal: ArrayLit([Id(b), Id(c)])"""
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_simple_full_vardecl10(self):
        input = """
           a: array[2,3] of integer = {{1,2,35}, {3,4,5}};
           b: array[3] of float = {1.2, 1.1, 1.1};
           c: array[2,3] of integer = {{1,2,3}, {1.2,1.3,1.4}};
        """
        expect = """Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([FloatLit(1.2), FloatLit(1.3), FloatLit(1.4)])])"""
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_complex_full_vardecl1(self):
        input = """
           a: array[2,3] of integer = {{1,2,35}, {3,4,5}};
           b: auto = a[0];
           c: array[2] of integer = b ;
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, ArrayType([2], IntegerType), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_complex_full_vardecl2(self):
        input = """
           a: array[2,3] of integer = {{1,2,35}, {3,4,5}};
           b: auto = a[0,1];
           c: float = b ;
           d: boolean = b ;
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(d, BooleanType, Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_complex_full_vardecl3(self):
        input = """
           a,b: integer = 1,2 ;
           c: integer = a + b - 31 + 3.1  ;
           d: float = a + c ;
           e: auto = 1.2 + 1 ;
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, BinExpr(+, BinExpr(-, BinExpr(+, Id(a), Id(b)), IntegerLit(31)), FloatLit(3.1)))"""
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_complex_full_vardecl4(self):
        input = """
           a,b: integer = 1,2 ;
           c: integer = a*b  ;
           d: integer = a%b ;
           e: float = a + c ;
           f: auto = d%e ;
           main: function void() {}
        """
        expect = """Type mismatch in expression: BinExpr(%, Id(d), Id(e))"""
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_complex_full_vardecl5(self):
        input = """
           a,b: integer = 1,2 ;
           c: float = a/b  ;
           d: auto = a/b ;
           e: auto = c%d ;
           main: function void() {}
        """
        expect = """Type mismatch in expression: BinExpr(%, Id(c), Id(d))"""
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_complex_full_vardecl6(self):
        input = """
           a,b: integer = -1, -2 ;
           c: auto = a > b ;
           d: auto = c == false ;
           e: auto = c > 12 ;
           main: function void() {}
        """
        expect = """Type mismatch in expression: BinExpr(>, Id(c), IntegerLit(12))"""
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_complex_full_vardecl7(self):
        input = """
           a,b: integer = -1, -2 ;
           c,d: float = 1,2.2 ;
           e,f: auto = c >= d , a == b ;
           g,h : auto = "hello", "world" ;
           i: auto = g::h ;
           t: boolean = !e ;
           k: auto =  1 != f || ( f == e) || false || (true || e );
           l: float = k ;
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(l, FloatType, Id(k))"""
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_complex_full_vardecl8(self):
        input = """
           a: array [2] of integer = {foo1() , foo2() };
           foo1: function auto() {}
           foo2: function auto() {}
           c: auto = foo1() ;
           d: auto = c + 1.1 ;
           e: integer = d ;
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(e, IntegerType, Id(d))"""
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_func_prototype1(self):
        input = """
           foo: function integer(inherit a: integer, b: float) {}
           foo1: function void(a: integer, b: float) inherit foo {
               
           }
          
           main: function void() {}
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_func_prototype2(self):
        input = """
           foo: function integer(inherit a: integer, b: float) {}
           a: integer = foo1(1,1) ;
           b: float = foo1(1,2) ;
           c: boolean = foo1(2,3);
           foo1: function auto (e: integer, b: integer) inherit foo {
               
           }
        
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, BooleanType, FuncCall(foo1, [IntegerLit(2), IntegerLit(3)]))"""
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_func_prototype3(self):
        input = """
           foo: function integer(inherit a: integer, b: float) {}
           a: integer = foo1(1,1) ;
           b: integer = foo1(1,2.1) ;
           foo1: function auto (e: auto, b: auto) inherit foo {
               
           }
        
           main: function void() {}
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [IntegerLit(1), FloatLit(2.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_func_prototype4(self):
        input = """
           foo: function integer(inherit a: integer, b: float) {}
           a: auto = foo(foo1(1,1), foo1(2,2)) ;
           foo1: function auto (e: integer, b: integer) inherit foo {
               
           }
        
           main: function void() {}
        """
        expect = """Invalid statement in function: foo1"""
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_func_prototype5(self):
        input = """
           foo: function integer(inherit a: integer, b: integer) {}
           a: auto = foo(foo1(1,1), foo1(2,2)) ;
           b: boolean = foo1(1,2) ;
           foo1: function auto (e: auto, b: auto) inherit foo {
               
           }
        
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo1, [IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_func_prototype6(self):
        input = """
           foo: function integer(inherit a: integer, b: integer) {}
                a: auto = foo(foo1(1,1.1), foo1(2,true)) ;
                b: boolean = foo1(1,2) ;
           foo1: function auto (e: auto, b: auto) inherit foo {
               
           }
        
           main: function void() {}
        """
        expect = """Type mismatch in expression: FuncCall(foo1, [IntegerLit(2), BooleanLit(True)])"""
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_func_prototype7(self):
        input = """
           foo: function integer(inherit a: integer, b: integer) {}
           a: auto = foo(foo1(1,1.1), foo1(2,2)) ;
           b: boolean = foo1(1,2) ;
           foo1: function auto (e: auto, b: auto) inherit foo {
               
           }
        
           main: function void() {}
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo1, [IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_func_firststmt1(self):
        input = """
        foo: function integer(inherit a: integer, b: integer) {}
        foo1: function auto (e: auto, b: auto) inherit foo{
            super(1);
            a = a + 1 ; 
        }
    
        main: function void() {}
    """
        expect = """Type mismatch in expression: """
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_func_firststmt2(self):
        input = """
        foo: function integer(inherit a: integer, b: integer) {}
        foo1: function auto (e: auto, b: auto) inherit foo{
            super(1,2,3) ;
            a = a + 1 ; 
        }
    
        main: function void() {}
    """
        expect = """Type mismatch in expression: IntegerLit(3)"""
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_func_firststmt3(self):
        input = """
        foo: function integer(inherit a: integer, b: integer) {}
        foo1: function auto (e: auto, b: auto) inherit foo{
            super(2, 3.4) ;
            a = a + 1 ; 
        }
    
        main: function void() {}
    """
        expect = """Type mismatch in expression: FloatLit(3.4)"""
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_func_firststmt4(self):
        input = """
        foo: function void (inherit a: integer, a: float) inherit bar {
            
        }
        bar: function auto (e: auto, b: auto) {
        }
    
        main: function void() {}
    """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_func_firststmt5(self):
        input = """
        foo: function integer(inherit a: auto, b: auto) {}
        foo1: function auto (e: auto, b: auto) inherit foo{
            super(1,2.2);
            foo(1,true) ;
            a = a + 1 ; 
        }
    
        main: function void() {}
    """
        expect = """Type mismatch in statement: CallStmt(foo, IntegerLit(1), BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 435))
    
    def test_func_firststmt7(self):
        input = """
        foo: function integer(inherit a: integer, b: integer) {}
        foo1: function auto (e: auto, b: auto) inherit foo{
            super(1,2) ;
            a = a + 1 ; 
            b: auto = b ;  
        }
    
        main: function void() {}
    """
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    
    def test_stmts1(self):
        input = """
        main: function void() {
            while (true) {
                continue;
            }
            break ;
        }
        """ 
        expect = """Must in loop: BreakStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 437))
    
    def test_stmts2(self):
        input = """
        main: function void() {
            i: integer = 0 ;
            for (i = 0, i < 5 , i + 1) {
                break ;
            }
            continue ;
        }
        """
        expect = """Must in loop: ContinueStmt()"""
        self.assertTrue(TestChecker.test(input, expect, 438))
    
    def test_stmts3(self):
        input = """
        foo: function auto (x: auto, y: auto) {
            return 2 ;
        }
        
        goo: function auto(a: auto, b: auto) inherit foo {
            preventDefault();
            return 1.1;
        } 
        
        main: function void () {
            a: auto = {foo(1.1,2), goo(1.1,2)} ;
            b: array[2] of integer = a ;
        }
        """
        expect = """Illegal array literal: ArrayLit([FuncCall(foo, [FloatLit(1.1), IntegerLit(2)]), FuncCall(goo, [FloatLit(1.1), IntegerLit(2)])])"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_stmts4(self):
        input = """
        foo: function auto (x: auto, y: auto) {
            return goo({1,3},2);
        }
        
        goo: function auto(a: auto, b: auto) inherit foo {
            preventDefault();
            return foo(1,2);
        } 
        
        main: function void () {
            a: array[2] of integer = foo(1, 1) ;
            b: auto = goo({1,2}, 1) ;
            c: auto = foo(2,2) ;
            d: array[1] of integer = c ;
            
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(d, ArrayType([1], IntegerType), Id(c))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
        
    def test_stmts5(self):
        input = """
        main: function void () {
            a: array[2] of integer = foo(1, 1) ;
            b: float = goo({1,2}, 1) ;
            c: auto = foo(2,2) ;
            d: array[2] of integer = c ;
        }
        
        foo: function auto (x: auto, y: auto) {
            return {1,2};
            return goo({1,3},2); // dont' care
        }
        goo: function auto(a: auto, b: auto) inherit foo {
            preventDefault();
            return 1;
            a = foo(2,2) ;
        } 
        
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [IntegerLit(2), IntegerLit(2)]))"""
        # For an assignment statement, the left-hand side can be in any type except void type and array type
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_stmts6(self):
        input = """
        main: function void () {
            a: array[2] of integer = foo(1, 1) ;
            b: integer = goo({1,2}, 1) ;
            c: auto = foo(2,2) ;
            d: array[2] of integer = c ;
        }
        
        foo: function auto (x: auto, y: auto) {
            return {goo({1,3},2), goo({2,3},1)};
            return 1 ; // don't care
            return true ; // don't care
        }
        goo: function auto(a: auto, b: auto) inherit foo {
            preventDefault();
            return 1.1 ; 
        } 
        
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.1))"""
        self.assertTrue(TestChecker.test(input, expect, 442))
    
    def test_stmts7(self):
        input = """
        main: function void () {
            a: array[2] of integer = foo(1, 1) ;
            b: float = goo({1,2}, 1) ;
            c: auto = foo(2,2) ;
            d: array[2] of integer = c ;
        }
        
        foo: function auto (x: auto, y: auto) {
            return {1,2};
        }
        goo: function auto(a: auto, b: auto) inherit foo {
            preventDefault();
            return 1;
            return 1.1;
            return true ;
            a = foo(1,2) ;
        } 
        
        """
        expect = """Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_stmts33(self):
        input = """
        foo: function auto () {
            a: integer = 1 ;
            b: float = 1 ;
            if (a < b) {
                return b ;
            } else {
                return a ;
            } 
        } 
        
        goo: function auto() {
            a: integer = 1 ;
            b: float = 1 ;
            if (a < b)  return a ; else return b ;
        }
        main: function void() {
            a: integer = foo() ;
        }
        
        """
        expect = """Type mismatch in statement: ReturnStmt(Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 444))
    
    def test_stmts34(self):
        input = """
        foo: function auto () {
            a: integer = 1 ;
            b: float = 1 ;
            if (a < b) return b ; else return a ;
            return true ; 
            while (true) {
                if ((a == 1) && (a == 2)) 
                    return 2 ;
                else 
                    return false ; 
            }
            return 1.1 ;
        } 
       
        main: function void() {
            a: float = foo() ;
        }
        
        """
        expect = """Type mismatch in statement: ReturnStmt(BooleanLit(True))"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_stmts8(self):
        input = """
        foo: function auto () {
            a: integer = 1 ;
            if (true) return 2 ;
            if (a == 1) return a ;
            if ((a > 1) || (a < 3)) return a ;
            if (!(a == 1)) return a + 1.1 ;
        } 
       
        main: function void() {
            a: float = foo() ;
        }
        
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, Id(a), FloatLit(1.1)))"""
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_stmts9(self):
        input = """
        goo: function auto (inherit a: auto, inherit b: auto) {
            goo(1,2) ;
            c: boolean = foo(2,2) ;
        }
        foo: function auto (c: auto, d: auto) inherit goo {
            super(a,b) ;
            goo(c,d) ;
            if (c + d == a + b) return goo(a,c) ;
            else if (c > a) return 3 ;
            else return 4 ;
            return true;
        } 
       
        main: function void() {
            
        }
        
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(3))"""
        self.assertTrue(TestChecker.test(input, expect, 447))
    
    def test_stmts10(self):
        input = """
        foo: function auto (a: auto, b: auto) {
            if (foo(1,2)) {
                return (a + b);
            }
           
        } 
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(+, Id(a), Id(b)))"""
        self.assertTrue(TestChecker.test(input, expect, 448))
    
    def test_stmts11(self):
        input = """
        foo: function auto (a: auto, b: auto) {
            if (true) {
                if (foo(2,1) + 3 > 5)
                    return a + b ;
                else if (foo(2,1)) {
                    return foo(2,1) ;
                } 
                else return a + b ;
            } 
            else return true ;
            
            return true ;
        } 
        """
        expect = """Type mismatch in statement: IfStmt(FuncCall(foo, [IntegerLit(2), IntegerLit(1)]), BlockStmt([ReturnStmt(FuncCall(foo, [IntegerLit(2), IntegerLit(1)]))]), ReturnStmt(BinExpr(+, Id(a), Id(b))))"""
        self.assertTrue(TestChecker.test(input, expect, 449))
    
    def test_stmts12(self):
        input = """
        main: function void() {
            for (i = 1, i < 3,  i + 1) {}
        }
        """
        expect = """Undeclared Identifier: i"""
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_stmts13(self):
        input = """
        main: function void() {
            i: float = 0 ;
            for (i = 1, i < 3,  i + 1) {}
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_stmts14(self):
        input = """
        main: function void() {
            i: integer = 0 ;
            for (i = 1, i + 3 ,  i > 1) {}
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(+, Id(i), IntegerLit(3)), BinExpr(>, Id(i), IntegerLit(1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test_stmts15(self):
        input = """
        main: function void() {
            i: integer = 0 ;
            for (i = 1, i < 5 ,  i + 1.1) {}
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), FloatLit(1.1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_stmts16(self):
        input = """
        main: function void() {
            i: integer = 0 ;
            for (i = 1.1, i < 5 , i + 1.1) {}
        }
        """
        expect = """Type mismatch in statement: ForStmt(AssignStmt(Id(i), FloatLit(1.1)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), FloatLit(1.1)), BlockStmt([]))"""
        self.assertTrue(TestChecker.test(input, expect, 454))
        
    def test_stmts17(self):
        input = """
        foo: function auto() {}
        main: function void() {
            i: integer = 0 ;
            a: integer = 1 ;
            for (i = foo(), i < 5 , i + 1) {
                foo: integer = 1 ;
                printInteger: integer = 1 ;
                a: integer = 1 ;
                b: boolean = foo() ;
            }
        } 
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, BooleanType, FuncCall(foo, []))"""
        self.assertTrue(TestChecker.test(input, expect, 455))
        
    def test_stmts18(self):
        input = """
        main: function void() {
            i: integer = 0 ;
            for (i = 1, i < 5 , i + 1) {
                i: integer = 1 ;
            }
        }
        """
        expect = """Redeclared Variable: i"""
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test_stmts19(self):
        input = """
        main: function void() {
            i,j,k: integer = 0,0,0 ;
            for (i = 1, i < 5_000 , i + 1) {
               for (j = 1 , j < i , j + 1)  {
                   for (k = 1, k < j, k + 1) {
                       printInteger(i + j + k) ;
                       i: integer = 1 ;
                       j: integer = 1 ;
                       k: integer = 1 ;
                   }
               }
            }
        }
        """
        expect = """Redeclared Variable: k"""
        self.assertTrue(TestChecker.test(input, expect, 457))
    
    def test_stmts20(self):
        input = """
        main: function void() {
            while (1 + 1) {
                return 0 ;
            }
        }
        """
        expect = """Type mismatch in statement: WhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))]))"""
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_stmts21(self):
        input = """
        main: function void() {
            a: boolean ;
            while (a) {
               a: integer = 1 ;
               while (a > 1)
                  a = a + 1 ;
               a: boolean = 1 ;
            }
        }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_stmts22(self):
        input = """
        main: function void() {
            a: boolean ;
            while (a) {
               while(!a)
                 print(a) ;
            }
        }
        """
        expect = """Undeclared Function: print"""
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_stmts23(self):
        input = """
        foo: function auto(x: auto, y: auto) {
            // do something
        }
        main: function void() {
           while(foo(1,2)) {
               a: boolean = foo(1,4) ;
               b: integer = foo(1,2) ;
           }
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(b, IntegerType, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"""
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    def test_stmts24(self):
        input = """
        foo: function auto(x: auto, y: auto) {
           while (x) {
               y = y + 1 ;
               if (x) return 1 ;
               while(x || (y > 1)) {
                   if (x) 
                        return y + 1 ;
                   else return 1 ;
               }    
           }
           return 1.1 ;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.1))"""
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_stmts25(self):
        input = """
        foo: function auto(x: auto, y: auto) {
           while (x) {
               y = y + 1 ;
               if (x) return 1 ;
               while(x || (y > 1)) {
                   if (x) 
                        return y + 1 ;
                   else return 1 ;
               }    
           }
           return 1.1 ;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.1))"""
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    def test_stmts26(self):
        input = """
        foo: function auto(x: auto, y: auto) {
          do {
              a: integer = 1 ;
          } while(1 + 1);
          return 1.1 ;
        }
        """
        expect = """Type mismatch in statement: DoWhileStmt(BinExpr(+, IntegerLit(1), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType, IntegerLit(1))]))"""
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_stmts27(self):
        input = """
        foo: function auto(x: auto, y: auto) {
          do {
              a: integer = 1 ;
          } while(a > 2);
          return 1.1 ;
        }
        """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_stmts28(self):
        input = """
        foo: function auto(x: auto, y: auto) {
          a : boolean = foo(1,2) ;
          do {
              a: integer = 1 ;
          } while(a > 2);
          return 1.1 ;
        }
        """
        expect = """Type mismatch in expression: BinExpr(>, Id(a), IntegerLit(2))"""
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_stmts29(self):
        input = """
        foo: function auto(x: auto, y: auto) {
          a : boolean = foo(1,2) ;
          do {
              a: integer = 1 ;
              return 1; 
          } while(a > 2);
          return 1.1 ;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_stmts30(self):
        input = """
        foo: function auto(x: auto, y: auto) {
          do {
              a: integer = 1 ;
              x = true ;
          } while(x || foo(!x,2));
          return true ;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_stmts31(self):
        input = """
        foo: function auto(x: auto, y: auto) {
          do {
              y = !x ;
              x = 1 ;
          } while(x || foo(!x,2));
          return true ;
        }
        """
        expect = """Type mismatch in statement: AssignStmt(Id(x), IntegerLit(1))"""
        self.assertTrue(TestChecker.test(input, expect, 469))
        
    def test_stmts32(self):
        input = """
        abc: function void (a: string) {
            printString(a) ;
        }
        len: function integer (s: string) inherit printString {
            super(s);
            return 10 ;
        }
        find: function string (s: string , ch: string) inherit abc {
            super(s);
            i: integer = 0 ;
            result: integer = -1 ;
            while (i <= len(s) - 1) {
                break;
                while (i < 1) {
                    {
                        if (len(s) > 1) { 
                            result = i ;
                            break ; 
                        }
                        else {
                            i = i + 1 ; 
                            continue ;
                        } 
                    }
                    printInteger(i);
                }
            }
            return "abc"::"def" ;
        }
        main: function void() {
            result: integer = 0 ; 
            {
                a: integer = 1 ;
                a = 2 ;
                b: auto = a ;
                temp: array[2] of integer = {1,2};
                a = temp[1] ;
            }
            s: string = "Hello world!" ;
            substr: auto = find(s, "3") ;
            printInteger(substr) ;
        }
    

    """
        expect = """Type mismatch in statement: CallStmt(printInteger, Id(substr))"""
        self.assertTrue(TestChecker.test(input, expect, 470))
    
    def test1(self):
        input = """
       foo: function void () {}
       main: function void() {
            foo: integer = 1;
            x: integer = foo();
            x = foo;
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [])"""
        self.assertTrue(TestChecker.test(input, expect, 471))
    
    
    def test2(self):
        input = """
        foo: function void () {}
        printInteger: function void() {
            
        }
        main: function void() {
            printInteger() ;
        }
        """
        expect = """Redeclared Function: printInteger"""
        self.assertTrue(TestChecker.test(input, expect, 472))
    
    def test3(self):
        input = """
        foo: function void (inherit a: integer, inherit b: auto) {}
        print: function void() inherit foo {
            super(1, 2) ;
            a: integer = 1 ;
        }
        
        main: function void() {
            printInteger() ;
        }
        """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    def test4(self):
        input = """
        foo: function void (inherit a: integer, inherit b: auto) {}
        print: function void(a: auto) inherit foo {
            super(1, 2) ;
            a: integer = 1 ;
        }
        
        main: function void() {
            printInteger() ;
        }
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test5(self):
        input = """
        foo: function void (inherit a: integer, inherit b: auto) {}
        print: function void(c: auto, c: integer, a: integer) inherit foo {
            super(1, 2) ;
            a: integer = 1 ;
        }
        """
        expect = """Redeclared Parameter: c"""
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test6(self):
        input = """
        foo: function void (inherit a: integer, inherit b: auto) {}
        print: function void(c: auto, a: integer, c: integer) inherit foo {
            super(1, 2) ;
            a: integer = 1 ;
        }
        """
        expect = """Invalid Parameter: Param(a, IntegerType)"""
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test6(self):
        input = """
        foo: function void (inherit a: integer, inherit b: auto) {}
        print: function void(c: auto, a: integer, c: integer) inherit foo {
            super(1, 2) ;
            a: integer = 1 ;
        }
        """
        expect = """Invalid Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 476))
    
    def test7(self):
        input = """
        foo: function void (a: integer, inherit b: auto, c: auto, d: auto) {}
        print: function void(c: auto, a: integer, e: integer) inherit foo {
            super(1, 2, b, d) ;
            b: integer = 1 ;
        }
        main: function void() {
            
        }
        """
        expect = """Undeclared Identifier: d"""
        self.assertTrue(TestChecker.test(input, expect, 477)) 
    
    def test8(self):
        input = """
        foo: function void (a: integer, inherit b: auto, c: auto, inherit d: auto) {}
        print: function void(c: auto, a: integer, e: integer) inherit foo {
            super(1, 2, b, d) ;
            b: integer = 1 ;
        }
        """
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 478)) 
    
    def test9(self):
        input = """
        foo: function void (a: integer, inherit b: auto, c: auto, inherit d: auto) {}
        print: function void(c: auto, a: integer, e: integer) inherit foo {
            super(1, 2, b, d) ;
            super(1,2,3) ;
        }
        """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 479)) 
    
    def test10(self):
        input = """
        foo: function void (a: integer, inherit b: auto, c: auto, inherit d: auto) {}
        print: function void(c: auto, a: integer, e: integer) inherit foo {
            super(1, 2, b, d) ;
            preventDefault() ;
        }
        """
        expect = """Undeclared Function: preventDefault"""
        self.assertTrue(TestChecker.test(input, expect, 480)) 
    
    def test11(self):
        input = """
        foo: function void (a: integer, inherit b: auto, c: auto, inherit d: auto) {}
        print: function void(c: auto, a: integer, e: integer) inherit foo {
            super(1, 2, b, d) ;
        }
        main: function void() {
            super(1,2,3,4);
        }
        """
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 481)) 
    
    def test12(self):
        input = """
        foo: function auto(a: auto, inherit b: auto, c: auto, inherit d: auto) {
            e: auto = d + 1.1 ;
            b = c > 2 ;
        }
        print: function void (c: auto, a: integer, e: integer) inherit foo {
            super(a, b, c , 1_2.43) ;
        }
        
         goo: function auto () inherit foo {
            super(1,2,3,4) ;
        } 
        main: function void() {
           //foo(1,2,3,4);
        }
        """
        expect = """Type mismatch in expression: IntegerLit(2)"""
        self.assertTrue(TestChecker.test(input, expect, 482))
    
    def test13(self):
        input = """
        main: function void() {
           foo(1,2,3,4);
        }
        foo: function auto(a: auto, inherit b: auto, c: auto, inherit d: auto) {
            e: auto = d + 1.1 ;
            b = c > 2 ;
        }
        print: function void (c: auto, a: integer, e: integer) inherit foo {
            super(a, b, c , 1_2.43) ;
        }
        
         goo: function auto () inherit foo {
            super(1,2,3,4) ;
        } 
        """
        expect = """Type mismatch in statement: AssignStmt(Id(b), BinExpr(>, Id(c), IntegerLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 483))
    
    def test14(self):
        input = """
       a: float = --foo(1);
       foo: function auto(a: auto) {
           return a > 2 ;
       }
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(>, Id(a), IntegerLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 484)) 
    
    def test15(self):
        input = """
        foo: function void(a: auto, b: integer) {
            a = a + b; 
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 485)) 
    
    def test16(self):
        input = """
        main: function integer() {
            
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 486)) 
    
    def test17(self):
        input = """
        main: function integer(a: auto) {
            
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 487)) 
    def test18(self):
        input = """
        main: function void () inherit printInteger {
            
        }
        """
        expect = """Invalid statement in function: main"""
        self.assertTrue(TestChecker.test(input, expect, 488)) 
    
    def test19(self):
        input = """
        main: function auto() {
            
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 489)) 
    
    def test20(self):
        input = """
        main: function void () inherit printInteger {
            preventDefault() ;
        }
        """
        expect = """No entry point"""
        self.assertTrue(TestChecker.test(input, expect, 490)) 
    
    def test21(self):
        input = """
       foo: function auto(a: auto) {
           a = -foo(1) + 1.1 ;
           return a > 2 ;
       }
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(>, Id(a), IntegerLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 491)) 
    
    def test22(self):
        input = """
        a: array[4] of integer = {foo(1.1), foo(1), -foo(2), -foo(1.1)};
        foo: function auto(a: auto) {
            a = -foo(5) + 1.1 ;
            return a > 2 ;
        }
        """
        expect = """Type mismatch in statement: ReturnStmt(BinExpr(>, Id(a), IntegerLit(2)))"""
        self.assertTrue(TestChecker.test(input, expect, 492))
    
    def test23(self):
        input = """
        foo: function auto (a: auto) inherit goo {
           super(-goo(1, 2), -foo(1));
        }
        
        goo: function auto(a: float, b: auto) {
            
        }
        main: function void() {
            a: float = --------foo(1) ;
            b: float = ------goo(1,2) ;
            c: integer = --goo(1,2) + 1 / -goo(1,2) ;
        }
        """
        expect = """Type mismatch in Variable Declaration: VarDecl(c, IntegerType, BinExpr(+, UnExpr(-, UnExpr(-, FuncCall(goo, [IntegerLit(1), IntegerLit(2)]))), BinExpr(/, IntegerLit(1), UnExpr(-, FuncCall(goo, [IntegerLit(1), IntegerLit(2)])))))"""
        self.assertTrue(TestChecker.test(input, expect, 493))  
    
    def test24(self):
        input = """
        a: array [2,2] of integer ={ {1 , 2}, {1,1.5}} ;
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(1.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 494))  
    
    def test25(self):
        input = """
        foo: function auto () {
            a: integer = 1 ;
            if (true) return 2 ;
            if (a == 1) return a ;
            if ((a > 1) || (a < 3)) return a ;
            if (!(a == 1)) return a + 1 ;
            return 1.1 ;
        } 
       
        main: function void() {
            a: float = foo() ;
        }
        
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.1))"""
        self.assertTrue(TestChecker.test(input, expect, 495))
    
    
    def test26(self):
        input = """
           foo: function integer (a: auto) {
               if (a > 1) {
                   return 1 ;
                   return true ; // don't carte
                   return {1} ;
               } else {
                   return 1.1 ;
               }
           }
           
        """
        expect = """Type mismatch in statement: ReturnStmt(FloatLit(1.1))"""
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test27(self):
        input = """
        foo: function void (a: auto, b: auto) {
            a = foo(1,2);
        }
        """
        expect = """Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"""
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test28(self):
        input = """
           a: array[3] of integer = {1, 1_1, 11};
           b: array[3] of float = {1, 1.1, 1.1};
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), FloatLit(1.1), FloatLit(1.1)])"""
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test29(self):
        input = """
           a: array[2,3] of integer = {{1,2,3.5}, {3,4,5}};
           b: array[3] of float = {1, 1.1, 1.1};
        """
        expect = """Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), FloatLit(3.5)])"""
        self.assertTrue(TestChecker.test(input, expect, 499))
    
