from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))

    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())

    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if (ctx.vardecl()):
            return self.visit(ctx.vardecl())
        return self.visit(ctx.vardeclfull()) if (ctx.vardeclfull()) else self.visit(ctx.funcdecl())

    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        idlist = self.visit(ctx.idlist())
        typ = self.visit(ctx.typ())
        return [VarDecl(id, typ) for id in idlist]

    # Visit a parse tree produced by MT22Parser#vardeclfull.
    def visitVardeclfull(self, ctx: MT22Parser.VardeclfullContext):
        triple = self.visit(ctx.vardeclrec())
        typ = triple[-1][1]
        temp = [x[-1] for x in triple]
        temp.reverse()
        i = 0
        while i < len(temp):
            y = list(triple[i])
            y[-1] = temp[i]
            triple[i] = tuple(y)
            i = i + 1
        return [VarDecl(x[0], typ, x[-1]) for x in triple]

    # Visit a parse tree produced by MT22Parser#basecase.
    def visitBasecase(self, ctx: MT22Parser.BasecaseContext):
        return (ctx.ID().getText(), self.visit(ctx.typ()), self.visit(ctx.expr()))

    # Visit a parse tree produced by MT22Parser#vardeclrec.
    def visitVardeclrec(self, ctx: MT22Parser.VardeclrecContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.basecase())]

        return [(ctx.ID().getText(),  self.visit(ctx.expr()))] + self.visit(ctx.vardeclrec())

    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        name = ctx.MAIN().getText() if ctx.MAIN() else ctx.ID(0).getText()
        typ = self.visit(ctx.typ())
        params = self.visit(ctx.paramlist())
        inherit = ""
        if ctx.INHERIT():
            inherit = ctx.ID(0).getText() if ctx.MAIN() else ctx.ID(1).getText()
        body = self.visit(ctx.blockstmt()) 
        
        return [FuncDecl(name, typ, params, inherit,body)]
        
            
    # Visit a parse tree produced by MT22Parser#paramlist.

    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramprime())
        

    # Visit a parse tree produced by MT22Parser#paramprime.
    def visitParamprime(self, ctx: MT22Parser.ParamprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.paramprime())

    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx: MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typ =  self.visit(ctx.typ())
        return ParamDecl(name,typ, True if ctx.OUT() else False, True if ctx.INHERIT() else False)
   
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())

    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if (ctx.BOOLEAN()):
            return BooleanType()
        if (ctx.INTEGER()):
            return IntegerType()
        if (ctx.FLOAT()):
            return FloatType()
        if (ctx.STRING()):
            return StringType()
        if (ctx.VOID()):
            return VoidType()
        if (ctx.AUTO()):
            return AutoType()
        return self.visit(ctx.arraytyp())

    # Visit a parse tree produced by MT22Parser#arraytyp.
    def visitArraytyp(self, ctx: MT22Parser.ArraytypContext):
        dimensions = self.visit(ctx.dimenlist())
        typ = self.visit(ctx.typ())
        return ArrayType(dimensions, typ)

    # Visit a parse tree produced by MT22Parser#dimenlist.
    def visitDimenlist(self, ctx: MT22Parser.DimenlistContext):
        if ctx.getChildCount() == 1:
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimenlist())

    # Visit a parse tree produced by MT22Parser#funcdecl.

    # Visit a parse tree produced by MT22Parser#expr.

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.CONCAT():
            return BinExpr(ctx.CONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))
        return self.visit(ctx.expr1(0))

    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx: MT22Parser.Expr1Context):
        if ctx.EQ():
            return BinExpr(ctx.EQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.NEQ():
            return BinExpr(ctx.NEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.LT():
            return BinExpr(ctx.LT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.LEQ():
            return BinExpr(ctx.LEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.GT():
            return BinExpr(ctx.GT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        if ctx.GEQ():
            return BinExpr(ctx.GEQ().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))

    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx: MT22Parser.Expr2Context):
        if ctx.AND() or ctx.OR():
            return BinExpr(ctx.AND().getText() if ctx.AND() else ctx.OR().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        return self.visit(ctx.expr3())

    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx: MT22Parser.Expr3Context):
        if ctx.PLUS() or ctx.SUB():
            return BinExpr(ctx.PLUS().getText() if ctx.PLUS() else ctx.SUB().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())

    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx: MT22Parser.Expr4Context):
        if ctx.MUL():
            return BinExpr(ctx.MUL().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.DIV():
            return BinExpr(ctx.DIV().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        if ctx.MOD():
            return BinExpr(ctx.MOD().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())

    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx: MT22Parser.Expr5Context):
        if ctx.NOT():
            return UnExpr(ctx.NOT().getText(), self.visit(ctx.expr5()))
        return self.visit(ctx.expr6())

    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx: MT22Parser.Expr6Context):
        if ctx.SUB():
            return UnExpr(ctx.SUB().getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())

    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx: MT22Parser.Expr7Context):
        if ctx.expr_index():
            return self.visit(ctx.expr_index())
        return self.visit(ctx.expr8())

     # Visit a parse tree produced by MT22Parser#expr_index.
    def visitExpr_index(self, ctx: MT22Parser.Expr_indexContext):
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.exprlist()))
    # Visit a parse tree produced by MT22Parser#expr8.

    def visitExpr8(self, ctx: MT22Parser.Expr8Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            floatlit = "0" + ctx.FLOATLIT().getText() if ctx.FLOATLIT().getText().startswith('.') else ctx.FLOATLIT().getText()
            return FloatLit(float(floatlit) )
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        if ctx.BOOLLIT():
            return BooleanLit(True if ctx.BOOLLIT().getText() == "true" else False)
        if ctx.arraylit():
            return self.visit(ctx.arraylit())
        if ctx.callexpr():
            return self.visit(ctx.callexpr())
        return self.visit(ctx.subexpr())

    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        return ArrayLit(self.visit(ctx.exprlist()))

    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx: MT22Parser.CallexprContext):
        return FuncCall(ctx.ID().getText(),self.visit(ctx.exprlist()))

    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by MT22Parser#exprlist.
    def visitExprlist(self, ctx: MT22Parser.ExprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.exprprime())

    # Visit a parse tree produced by MT22Parser#exprprime.
    def visitExprprime(self, ctx: MT22Parser.ExprprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprprime())

    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstmt(): return self.visit(ctx.assignstmt())
        if ctx.ifstmt(): return self.visit(ctx.ifstmt())
        if ctx.forstmt(): return self.visit(ctx.forstmt())
        if ctx.whilestmt(): return self.visit(ctx.whilestmt())
        if ctx.dowhilestmt(): return self.visit(ctx.dowhilestmt())
        if ctx.breakstmt(): return self.visit(ctx.breakstmt())
        if ctx.continuestmt(): return self.visit(ctx.continuestmt())
        if ctx.returnstmt(): return self.visit(ctx.returnstmt())
        if ctx.callstmt(): return self.visit(ctx.callstmt())
        if ctx.blockstmt(): return self.visit(ctx.blockstmt())
        return []

    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        lhs = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.expr_index())
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs,rhs)

    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        if ctx.ELSE():
            return IfStmt(cond, tstmt, self.visit(ctx.stmt(1)))
        return IfStmt(cond, tstmt)
        
    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        init = AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr(0)))
        cond = self.visit(ctx.expr(1))
        update = self.visit(ctx.expr(2))
        stmt = self.visit(ctx.stmt())
        return ForStmt(init,cond,update,stmt)

    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return WhileStmt(expr, stmt)

    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        bstmt = self.visit(ctx.blockstmt())
        cond = self.visit(ctx.expr())
        return DoWhileStmt(cond, bstmt)

    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        return ReturnStmt(self.visit(ctx.expr())) if ctx.expr() else ReturnStmt()

    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.exprlist()))

    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return BlockStmt(self.visit(ctx.stmtlist()))

    # Visit a parse tree produced by MT22Parser#stmtlist.
    def visitStmtlist(self, ctx: MT22Parser.StmtlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.stmtprime())

    # Visit a parse tree produced by MT22Parser#stmtprime.
    def visitStmtprime(self, ctx: MT22Parser.StmtprimeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.stmtblocks()) # return ctx.stmt() list
        return self.visit(ctx.stmtblocks()) + self.visit(ctx.stmtprime())

     # Visit a parse tree produced by MT22Parser#stmtblocks.
    def visitStmtblocks(self, ctx:MT22Parser.StmtblocksContext):
        if ctx.vardecl(): return self.visit(ctx.vardecl())
        if ctx.vardeclfull(): return self.visit(ctx.vardeclfull())
        if ctx.stmt(): return [self.visit(ctx.stmt())]

