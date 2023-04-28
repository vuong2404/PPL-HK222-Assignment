from Visitor import Visitor
from AST import *
from StaticError import *

class Symbol:
    def __init__(self,name, parent_name, mtype, value = None):
        self.name = name 
        self.parent_name = parent_name
        self.mtype = mtype
        self.value = value
    def  __str__(self):
        return  "({},{},{})".format(self.name, self.parent_name,self.mtype.return_type)
        
class MType:
    def __init__(self,params,rettype):
        self.params = params
        self.return_type = rettype    
    

class GetEnv(Visitor):
    def __init__(self, ast):
        self.ast = ast 
    def visitProgram(self, ast, o):
        env = []
        
        for decl in ast.decls:
            if type(decl) == FuncDecl:
                env = self.visit(decl,env)
        
        return o + env ;
    def visitVarDecl(self, ast, o): pass
    def visitParamDecl(self, ast, o): 
        return o + [Symbol(ast.name, None, MType(None, ast.typ))]
    def visitFuncDecl(self, ast, o): 
        return o + [Symbol(ast.name, ast.inherit, MType(ast.params, ast.return_type))]
            
    def visitIntegerType(self, ast, o): pass
    def visitFloatType(self, ast, o): pass
    def visitBooleanType(self, ast, o): pass
    def visitStringType(self, ast, o): pass
    def visitArrayType(self, ast, o): pass
    def visitAutoType(self, ast, o): pass
    def visitVoidType(self, ast, o): pass

    def visitBinExpr(self, ast, o): pass
    def visitUnExpr(self, ast, o): pass
    def visitId(self, ast, o): pass
    def visitArrayCell(self, ast, o): pass
    def visitIntegerLit(self, ast, o): pass
    def visitFloatLit(self, ast, o): pass
    def visitStringLit(self, ast, o): pass
    def visitBooleanLit(self, ast, o): pass
    def visitArrayLit(self, ast, o): pass
    def visitFuncCall(self, ast, o): pass

    def visitAssignStmt(self, ast, o): pass
    def visitBlockStmt(self, ast, o): pass
    def visitIfStmt(self, ast, o): pass
    def visitForStmt(self, ast, o): pass
    def visitWhileStmt(self, ast, o): pass
    def visitDoWhileStmt(self, ast, o): pass
    def visitBreakStmt(self, ast, o): pass
    def visitContinueStmt(self, ast, o): pass
    def visitReturnStmt(self, ast, o): pass
    def visitCallStmt(self, ast, o): pass

class StaticChecker(Visitor):
    global_env = [
        Symbol("readInteger",None, MType([], IntegerType())),
        Symbol("printInteger",None, MType([ParamDecl("",IntegerType(), False, False)], VoidType())),
        Symbol("readFloat",None, MType([], FloatType())),
        Symbol("writeFloat",None, MType([ParamDecl("",FloatType(), False, False)], VoidType())),
        Symbol("readBoolean",None, MType([], BooleanType())),
        Symbol("printBoolean",None, MType([ParamDecl("", BooleanType(), False, False)], VoidType())),
        Symbol("readString",None, MType([], StringType())),
        Symbol("printString",None, MType([ParamDecl("",StringType(), False, False)], VoidType())),
        # Symbol("super", None, MType([], VoidType())),
        # Symbol("preventDefault", None, MType([], VoidType()))
    ]
    
    inLoop = []
    temp_symbol = None
    is_first_retstmt = True ;
    
    
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visit(self.ast, self.global_env)
        
    def lookup(self, name, o):
        for env in o:
            for symbol in env:
                if symbol.name == name:
                    return symbol
        return None 
    
    def lookupAll(self, name, o):
        for env in o:
            for symbol in env:
                if symbol.name == name:
                    return symbol
        
        for symbol in self.global_env:
            if symbol.name == name:
                return symbol
        return None 
    def inferType(self, expr, typ, o):
        while type(expr) == UnExpr:
            expr = expr.val
        name = expr.name if type(expr) != str else expr
        for env in o:
            for symbol in env:
                if symbol.name == name:
                    symbol.mtype.return_type = typ
                    return typ
        # function was declared behind
        for symbol in self.global_env:
            if symbol.name == name:
                if self.temp_symbol and self.temp_symbol.name == name:
                    self.temp_symbol.mtype.typ = typ 
                symbol.mtype.return_type = typ
                return typ
    
    def inferParamType(self, name, i, typ, o):
        for env in o:
            for symbol in env:
                if symbol.name == name:
                    symbol.mtype.params[i].typ = typ
                    return typ
        
        # function was declared behind
        for symbol in self.global_env:
            if symbol.name == name:
                if self.temp_symbol and self.temp_symbol.name == name:
                    self.temp_symbol.mtype.params[i].typ = typ 
                symbol.mtype.params[i].typ = typ
                return typ

    def visitProgram(self, ast, o): 
        o = [self.global_env]
        # Duyệt sơ bộ -> lưu vào global_env
        self.global_env = GetEnv(ast).visit(ast, self.global_env) ;
        
        has_mainfunc = False
        #check program has main function
        for decl in ast.decls:
            if isinstance(decl, FuncDecl) and decl.name == 'main' and type(decl.return_type) == VoidType and len(decl.params) == 0 and (decl.inherit == None or decl.inherit == ""):
                has_mainfunc = True
                break 
        
        #visit decl
        for decl in ast.decls:
            o = self.visit(decl, o)
            
        if not has_mainfunc:
            raise NoEntryPoint()
        return [str(y) for x in o for y in x] 
    def visitVarDecl(self, ast, o):
        #check redeclared varible
        ltype = ast.typ
        rtype = None
        for symbol in o[0]:
            if symbol.name == ast.name:
                if len(o) == 1:
                    raise Redeclared(Variable(), ast.name)
                elif symbol.mtype.params == None:
                    raise Redeclared(Variable(), ast.name)
                    
        if type(ltype) is VoidType:
            raise Invalid(Variable(), ast.name)
        if type(ltype) is AutoType:
            if not ast.init:
                raise Invalid(Variable(), ast.name) 
            rtype = self.visit(ast.init,o)
            o[0] = o[0] + [Symbol(ast.name, None, MType(None, rtype))]
        
        else:
            if ast.init:
                rtype = self.visit(ast.init,o)
                if type(rtype) is VoidType:
                    raise TypeMismatchInVarDecl(ast)
                elif type(rtype) is AutoType:
                    # init is certainly a function call or unaryExpr (-func or --func or ---...func)
                    self.inferType(ast.init, ltype, o)
                elif type(ltype) is FloatType:
                    if type(rtype) is not IntegerType and type(rtype) is not FloatType:
                        raise TypeMismatchInVarDecl(ast)
                elif type(ltype) is ArrayType:
                    if type(rtype) is not ArrayType:
                        raise TypeMismatchInVarDecl(ast)
                    if (ltype.dimensions != rtype.dimensions):
                        raise TypeMismatchInVarDecl(ast)
                    else:
                        if type(rtype.typ) == AutoType:
                            for expr in ast.init.explist:
                                self.inferType(expr, ltype.typ, o)
                        elif (type(ltype.typ) != type(rtype.typ)):
                            raise TypeMismatchInVarDecl(ast)
                elif type(ltype) != type(rtype):    
                    raise TypeMismatchInVarDecl(ast)
                    
            o[0] = o[0] + [Symbol(ast.name, None, MType(None, ltype))]
        
        return o
        
    def visitParamDecl(self, ast, o):
        for symbol in o[0]:
            if symbol.name == ast.name:
                raise Redeclared(Parameter(), ast.name)
        o[0] +=  [Symbol(ast.name, None, MType(None, ast.typ))]
        return o
        
    def visitFuncDecl(self, ast, o): 
        #ensure function is not declared
        if self.lookup(ast.name, o):
            raise Redeclared(Function(), ast.name)
        
        
        env = [[]] + o  # new scope
        
        # ensure parent function is declared (if it had inhehit)
        parent = None 
        if ast.inherit:
            for envi in o:
                for symbol in envi: 
                    if symbol.name == ast.inherit and symbol.mtype.params != None:
                        parent = symbol
                        break 
            if not parent:
                for symbol in self.global_env:
                    if symbol.name == ast.inherit and symbol.mtype.params != None:
                        parent = symbol
            if not parent:
                raise Undeclared(Function() ,ast.inherit)

            # #get params inherit from parent: 
            # for param in parent.mtype.params:
            #     if param.inherit:
            #         env[0] =  env[0] + [Symbol(param.name, None, MType(None, param.typ))]
        
        
        # consider params of function decl
        if parent:
            for param in ast.params:
                for parent_param in parent.mtype.params:
                    if param.name == parent_param.name and parent_param.inherit:
                        raise Invalid(Parameter(), param.name)
                env = self.visit(param, env)
        else:
            for param in ast.params:
                env = self.visit(param, env)
            
        
        # check first stmt in case function has inherit
        list_stmts = ast.body.body
        if (ast.inherit):
            if len(list_stmts) == 0:
                raise InvalidStatementInFunction(ast.name)
            stmt = list_stmts[0]
            if len(parent.mtype.params) > 0:
                #stmt must be a callstmt whose name is super or preventDefault
                if type(stmt) != CallStmt:
                    raise InvalidStatementInFunction(ast.name)
                
                if stmt.name != "super" and stmt.name != "preventDefault":
                    raise InvalidStatementInFunction(ast.name)
                
                if stmt.name == "super":
                    for param in parent.mtype.params:
                        if param.inherit:
                            env[0] =  env[0] + [Symbol(param.name, None, MType(None, param.typ))]
                    # ensure len(args  of callstmt) >= len(parent params)
                    if len(stmt.args) < len(parent.mtype.params):
                        raise TypeMismatchInExpression(None)
                    
                    #check params of callstmt suitable with parent params
                    for i in range(0,len(stmt.args)):
                        if i >= len(parent.mtype.params):
                            raise TypeMismatchInExpression(stmt.args[i])
                        
                        arg = self.visit(stmt.args[i], env)
                        par = parent.mtype.params[i] 
                        if type(par.typ) == AutoType:
                            self.inferParamType(parent.name, i, arg, env)
                        elif type(arg) == AutoType:
                            # arg must be a call fucntion or a param
                            # => infer the return type
                            self.inferType(stmt.args[i], par.typ, env)
                        elif type(par.typ) == FloatType:
                            if type(arg) != FloatType and type(arg) != IntegerType:
                                raise TypeMismatchInExpression(stmt.args[i])
                        elif type(arg) != type(par.typ):
                            raise TypeMismatchInExpression(stmt.args[i])
                    
                elif stmt.name == "preventDefault":
                    # len(params) must equal 0
                    if len(stmt.args) > 0:
                        raise TypeMismatchInStatement(stmt.args[0])
                list_stmts = list_stmts[1:] 
            else:
                #stmt can be a callstmt whose name is preventDefault or another one 
                if stmt.name == "preventDefault":
                    # len(params) must equal 0
                    if len(stmt.args) > 0:
                        raise TypeMismatchInStatement(ast)
                    list_stmts = list_stmts[1:] 
        else:
            if len(list_stmts) > 0:
                stmt = list_stmts[0]
                if type(stmt) is CallStmt and (stmt.name == "super" or stmt.name == "preventDefault"):
                    raise InvalidStatementInFunction(ast.name)
        
        for symbol in self.global_env:
            if (symbol.name == ast.name):
                self.temp_symbol = symbol
                break
        
        for stmt in list_stmts:
            if type(stmt) is BreakStmt or type(stmt) is ContinueStmt:
                raise MustInLoop(stmt)
            elif type(stmt) is ReturnStmt:
                # Case return is not into any stmt:
                # Don't care any return stmt after first return stmt
                if self.is_first_retstmt:
                    ret_type = self.visit(stmt.expr, env)
                    if type(self.temp_symbol.mtype.return_type) is AutoType:
                        self.temp_symbol.mtype.return_type = ret_type
                    elif type(ret_type) is AutoType:
                        # case 1: the expr of returnstmt is varaible -> it must be a auto params
                        # case 2: the expr of returnstmt is funccall
                        self.inferType(stmt.expr, self.temp_symbol.mtype.return_type, env) 
                    elif type(self.temp_symbol.mtype.return_type) == FloatType:
                        if type(ret_type) != IntegerType and type(ret_type) != FloatType:
                            raise TypeMismatchInStatement(stmt)
                    elif type(self.temp_symbol.mtype.return_type) != type(ret_type):
                        raise TypeMismatchInStatement(stmt)
                    self.is_first_retstmt = False ;
            else:
                env = self.visit(stmt, env)
                
        self.is_first_retstmt = True
        
        for param in self.temp_symbol.mtype.params:
            for symbol in env[0]:
                if symbol.name == param.name:
                    param.typ = symbol.mtype.return_type
                    break
        o[0] = o[0] + [self.temp_symbol]
        
        # for symbol in env[0]:
        #     print(symbol.name, symbol.mtype.return_type)
        
        # for param in self.temp_symbol.mtype.params:
        #     print(param.name, param.typ)
            
        
        self.temp_symbol = None
        return o

    def visitReturnStmt(self, ast, o): 
        ret_type = self.visit(ast.expr, o)
        if self.temp_symbol and self.is_first_retstmt: 
            if type(self.temp_symbol.mtype.return_type) is AutoType:
                self.temp_symbol.mtype.return_type = ret_type
            elif type(ret_type) is AutoType:
                # case 1: the expr of returnstmt is varaible -> it must be a auto params
                # case 2: the expr of returnstmt is funccall
                self.inferType(ast.expr, self.temp_symbol.mtype.return_type, o) 
            elif type(self.temp_symbol.mtype.return_type) == FloatType:
                if type(ret_type) != IntegerType and type(ret_type) != FloatType:
                    raise TypeMismatchInStatement(ast)
            elif type(self.temp_symbol.mtype.return_type) != type(ret_type):
                raise TypeMismatchInStatement(ast)
            
        return o
    def visitCallStmt(self, ast, o):
        func = None
        # check function have already declared and type it's really  a function
        for env in o:
            for symbol in env:
                if symbol.name == ast.name: 
                    if symbol.mtype.params == None:
                        raise TypeMismatchInStatement(ast)
                    func = symbol
                break
        # check function declaration if function was declared after used
        if not func:
            for symbol in self.global_env:
                if symbol.name == ast.name:
                    if symbol.mtype.params == None:
                        raise TypeMismatchInStatement(ast)
                    func = symbol
                    break
        
        if not func:
            raise Undeclared(Function(), ast.name)

        # #ensure function had return type and it's void type
        # if func.mtype.return_type is not VoidType
        #     raise TypeMismatchInStatement(ast)
        
        # ensure len(args) = len(o)
        if len(ast.args) != len(func.mtype.params):
            raise TypeMismatchInStatement(ast)
        
        #check compatible types
        for i in range(0,len(ast.args)):
            arg = self.visit(ast.args[i], o)
            if  i >= len(func.mtype.params):
                raise TypeMismatchInStatement(ast)
            par = func.mtype.params[i] 
            if type(par.typ) == AutoType:
                if self.temp_symbol and self.temp_symbol.name == func.name:
                    self.inferType(par, arg, o)
                self.inferParamType(func.name, i, arg, o)
            elif type(arg) == AutoType:
                # arg must be a call fucntion:
                # => infer the return type
                self.inferType(ast.args[i], par.typ, o)
            elif type(par.typ)  ==  FloatType:
                if type(arg) != IntegerType and type(arg) != FloatType:
                    raise TypeMismatchInStatement(ast)
            elif type(arg) is not type(par.typ):
                raise TypeMismatchInStatement(ast)
        
        return o
    def visitAssignStmt(self, ast, o):
        # ensure left hand side is varaiable or index operator
        if type(ast.lhs) != Id and type(ast.lhs) != ArrayCell:
            raise TypeMismatchInStatement(ast)
    
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        
        if type(lhs) is VoidType or type(lhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        
        if type(lhs) == AutoType:
            lhs = self.inferType(ast.lhs, rhs, o)
        elif type(rhs) == AutoType:
            rhs = self.inferType(ast.rhs, lhs, o)
        elif type(lhs) == FloatType:
            if type(rhs) != FloatType and type(rhs) != IntegerType:
                raise TypeMismatchInStatement(ast)
        elif type(lhs) != type(rhs):
            raise TypeMismatchInStatement(ast)
        
        return o
     
    def visitBlockStmt(self, ast, o):  
        env = [[]] + o  #new scope
        is_first_retstmt_inblock = True
        for ele in ast.body:
            if type(ele) is ReturnStmt:
                if self.temp_symbol and self.is_first_retstmt:
                    if is_first_retstmt_inblock:
                        o = self.visit(ele, o)
                        is_first_retstmt_inblock = False
            else: env = self.visit(ele, env)
        return o 
    
    def visitIfStmt(self, ast, o): 
        cond = self.visit(ast.cond, o)
        if type(cond) is AutoType:
            self.inferType(ast.cond, BooleanType(), o)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)
        o = self.visit(ast.tstmt, o)
        if ast.fstmt:
            o = self.visit(ast.fstmt, o)
        return o
    def visitForStmt(self, ast, o): 
        self.inLoop = self.inLoop + [1]
        if type(ast.init.lhs) != Id: 
            raise TypeMismatchInStatement(ast)

        scalar_variable = self.lookup(ast.init.lhs.name, o)
        if not scalar_variable:
            raise Undeclared(Identifier(), ast.init.lhs.name)
        
        rtype = self.visit(ast.init.rhs, o)
        if type(rtype) is AutoType:
            if type(scalar_variable.mtype.return_type) != IntegerType:
                raise TypeMismatchInStatement(ast)   
            else: self.inferType(ast.init.rhs, IntegerType(), o)
        elif type(rtype) != IntegerType:
            raise TypeMismatchInStatement(ast)
        elif type(scalar_variable.mtype.return_type) == AutoType:
            self.inferType(scalar_variable.name, IntegerType(), o)
        elif type(scalar_variable.mtype.return_type) != IntegerType:
            raise TypeMismatchInStatement(ast)
        
        cond = self.visit(ast.cond, o)
        if type(cond) == AutoType:
            cond = self.inferType(ast.cond, BooleanType, o)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)
        
        upd_expr = self.visit(ast.upd, o)
        if type(upd_expr) != IntegerType:
            raise TypeMismatchInStatement(ast)
        
        if type(ast.stmt) is BlockStmt:
            env = [[scalar_variable]] + o
            for stmt in ast.stmt.body:
                env = self.visit(stmt, env)
        else: 
            o = self.visit(ast.stmt, o)
        
        self.inLoop = self.inLoop[1:]
        return o
        
         
    def visitWhileStmt(self, ast, o):
        self.inLoop = self.inLoop + [1]
        cond = self.visit(ast.cond, o)
        if type(cond) == AutoType:
            cond = self.inferType(ast.cond, BooleanType(), o)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)
        
        o = self.visit(ast.stmt, o)
        self.inLoop = self.inLoop[1:]
        
        return o 

    def visitDoWhileStmt(self, ast, o): 
        self.inLoop = self.inLoop + [1]
        o = self.visit(ast.stmt, o) 
        
        cond = self.visit(ast.cond, o)
        if type(cond) == AutoType:
            cond = self.inferType(ast.cond, BooleanType(), o)
        elif type(cond) != BooleanType:
            raise TypeMismatchInStatement(ast)
        
        self.inLoop = self.inLoop[1:]
        
        return o

    def visitBreakStmt(self, ast, o): 
        if len(self.inLoop) == 0:
            raise MustInLoop(ast) 
        return o
    def visitContinueStmt(self, ast, o):
        if len(self.inLoop) == 0:
            raise MustInLoop(ast)
        return o 

    def visitIntegerType(self, ast, o): pass
    def visitFloatType(self, ast, o): pass
    def visitBooleanType(self, ast, o): pass
    def visitStringType(self, ast, o): pass
    def visitArrayType(self, ast, o): pass
    def visitAutoType(self, ast, o): pass
    def visitVoidType(self, ast, o): pass

    def visitBinExpr(self, ast, o):
        op = ast.op 
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o) 
        
        if type(left) == AutoType:
            # left must be a function call or a param in function decl:
            left = self.inferType(ast.left, right, o)
        elif type(right) == AutoType:
            right = self.inferType(ast.right, left, o)
            
        if op in ['+', '-', '*', '/']: 
            if (type(left) != IntegerType and type(left) != FloatType) or (type(right) != IntegerType and type(right) != FloatType):
                raise TypeMismatchInExpression(ast)
            if type(left) == FloatType or type(right) == FloatType:
                return FloatType()
            return IntegerType()
        elif op == '%':
            if type(left) != IntegerType or type(right) != IntegerType:
                raise TypeMismatchInExpression(ast)
            return IntegerType()
        elif op in ['>', '<', '<=', '>=']:
            if (type(left) != IntegerType and type(left) != FloatType) or (type(right) != IntegerType and type(right) != FloatType):
                raise TypeMismatchInExpression(ast)
            return BooleanType() 
        elif op in ['==', '!=']:
            if (type(left) != IntegerType and type(left) != BooleanType) or (type(right) != IntegerType and type(right) != BooleanType):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        elif op in ['||', '&&']:
            if type(left) != BooleanType or type(right) != BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        elif op == '::':
            if type(left) != StringType or type(right) != StringType:
                raise TypeMismatchInExpression(ast)
            return StringType()

    def visitUnExpr(self, ast, o): 
        op = ast.op 
        val = self.visit(ast.val, o)
        if op == '-':
            if type(val) != IntegerType and type(val) != FloatType and type(val) != AutoType:
                raise TypeMismatchInExpression(ast)
            return val
        elif op == '!':
            if type(val) == AutoType:
                val = self.inferType(ast.val, BooleanType(), o)
            if type(val) is not BooleanType:
                raise TypeMismatchInExpression(ast)
            return BooleanType()
    def visitId(self, ast, o): 
        for env in o:
            for symbol in env:
                if ast.name == symbol.name:
                    if symbol.mtype.params == None:
                        return symbol.mtype.return_type
        raise Undeclared(Identifier(), ast.name)
    def visitArrayCell(self, ast, o): 
        name = ast.name 
        cell = ast.cell 
        
        is_declared = False
        dest = None
        #ensure name is declared and type of name is arrayType:
        for env in o:
            for symbol in env:
                if symbol.name == name:
                    if type(symbol.mtype.return_type) != ArrayType:
                        raise TypeMismatchInExpression(ast) 
                    is_declared = True
                    dest = symbol.mtype.return_type
                    break
        
        if not is_declared:
            raise Undeclared(Identifier(), name)

        # ensure all expr in cell is integer:
        for expr in cell:
            typ = self.visit(expr, o)
            if type(typ) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        
        # ensure length cell <= len dimentions
        if len(cell) > len(dest.dimensions):
            raise  TypeMismatchInExpression(ast)
            
        #ensure all integer in cell < dimension corresponding
        #.........

        # return corresponding type
        if len(cell) < len(dest.dimensions):
            return ArrayType(dest.dimensions[len(cell):], dest.typ) 
        return dest.typ  
    
    def visitIntegerLit(self, ast, o): 
        return IntegerType()
    def visitFloatLit(self, ast, o): 
        return FloatType()
    def visitStringLit(self, ast, o): 
        return StringType()
    def visitBooleanLit(self, ast, o): 
        return BooleanType()
    def visitArrayLit(self, ast, o): 
        typ = None
        has_autotype = False
        for ele in ast.explist:
            eletype = self.visit(ele, o)
            if type(eletype) == VoidType:
                raise IllegalArrayLiteral(ast)
            if not typ:
                typ = eletype
                if type(typ) is AutoType:
                    has_autotype = True
            else:
                if type(eletype) is AutoType:
                    if type(typ) != AutoType:
                        self.inferType(ele, typ,o)
                    else:
                        has_autotype = True
                elif type(typ) == AutoType:
                    typ = eletype
                elif type(typ) != type(eletype):
                    raise IllegalArrayLiteral(ast)   
                
                if type(typ) is ArrayType:
                    if (typ.dimensions != eletype.dimensions) or type(typ.typ) != type(eletype.typ):
                        raise IllegalArrayLiteral(ast)
        
        if type(typ) == AutoType:
            return ArrayType([len(ast.explist)], typ)
        elif has_autotype:
            for ele in ast.explist:
                eletype = self.visit(ele, o)
                if type(eletype) == AutoType:
                    self.inferType(ele, typ, o)
                       
        if type(typ) in [IntegerType, FloatType, BooleanType, StringType]:
            return ArrayType([len(ast.explist)], typ)
        return ArrayType([len(ast.explist)] + typ.dimensions, typ.typ)
    def visitFuncCall(self, ast, o): 
        func = None
        
        # check function have already declared and type it's really  a function
        for env in o:
            for symbol in env:
                if symbol.name == ast.name:
                    if symbol.mtype.params != None:
                        func = symbol
                        break
        # check function declaration if function was declared after used
        if not func:
            for symbol in self.global_env:
                if symbol.name == ast.name:
                    if symbol.mtype.params != None:
                        func = symbol
                        break
        
        if not func:
            raise Undeclared(Function(), ast.name)

        #ensure function had return type and it's not void type
        if type(func.mtype.return_type) is VoidType:
            raise TypeMismatchInExpression(ast)
        
        # ensure len(args) = len(o)
        if len(ast.args) != len(func.mtype.params):
            raise TypeMismatchInExpression(ast)
        
        #check compatible types
        for i in range(0,len(ast.args)):
            arg = self.visit(ast.args[i], o)
            par = func.mtype.params[i] 
            if type(par.typ) == AutoType:
                if self.temp_symbol and self.temp_symbol.name == func.name:
                    self.inferType(par, arg, o)
                self.inferParamType(func.name, i, arg, o)
            elif type(arg) == AutoType:
                # arg must be a call fucntion:
                # => infer the return type
                self.inferType(ast.args[i], par.typ, o)
            elif type(par.typ) == FloatType:
                if type(arg) != IntegerType and type(arg) != FloatType:
                    raise TypeMismatchInExpression(ast)
            elif type(arg) != type(par.typ):
                raise TypeMismatchInExpression(ast)            
        
        return func.mtype.return_type
        
        
        
        
