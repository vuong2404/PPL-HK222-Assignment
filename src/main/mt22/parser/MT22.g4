// id: 2015108
grammar MT22;

@lexer::header {
from lexererr import *
}

@parser::members {
countIDs = 0
countExprs = 0 ;
}

options {
	language=Python3;
}


program: decllist EOF ;
decllist: decl decllist | decl ; 
decl: vardecl | vardecl_fullformat | funcdecl; 
vardecl: idlist COLON typ SEMI ;
vardecl_fullformat: {self.countIDs = 0 ; self.countExprs = 0} idlist COLON typ ASSIGN  exprlistdecl {self.countIDs == self.countExprs}? SEMI   ;
idlist: (ID COMMA idlist | ID) {self.countIDs += 1} ; 
typ: BOOLEAN | INTEGER | STRING | FLOAT | arraytyp | AUTO ;
arraytyp: ARRAY LSB dimenlist RSB OF (BOOLEAN | INTEGER | STRING | FLOAT) ; 
dimenlist: INTLIT COMMA dimenlist | INTLIT ;


funcdecl: (ID | MAIN) COLON FUNCTION returntype LB paramlist RB (INHERIT ID)? funcbody ;
returntype: BOOLEAN | INTEGER | STRING | FLOAT | VOID | AUTO | arraytyp;
paramlist: paramprime | ; 
paramprime: param COMMA paramprime | param ; 
param: INHERIT? OUT? ID COLON typ ;
funcbody: LCB stmtlist RCB ;

expr: expr1 CONCAT expr1 | expr1 ; 
expr1: expr2 ( EQUAL | NOT_EQUAL | GREATER | GREATER_EQUAL | LESS | LESS_EQUAL) expr2 | expr2; 
expr2: expr2 (AND | OR) expr3 | expr3 ; 
expr3: expr3 (PLUS | MINUS) expr4 | expr4 ;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5 ;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7 ; 
expr7: expr_index | expr8;
expr8: ID | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | arraylit | callexpr | subexpr  ;
arraylit: LCB exprlist RCB ;
callexpr: ID LB exprlist RB ;  
subexpr: LB expr RB ; 
exprlist: exprprime |  ; 
exprprime:  (expr COMMA exprprime  | expr) ;  

expr_bool: expr1  ; 
expr_arith: expr3 ; 
expr_index: ID LSB indexlist RSB   ;
indexlist: index COMMA indexlist | index ;
index: ID | INTLIT | callexpr | subexpr | expr_index  ;

exprlistdecl: (exprdeclprime |)   ;
exprdeclprime: (expr COMMA exprdeclprime | expr) {self.countExprs += 1} ;


stmt: vardecl | vardecl_fullformat | assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt | blockstmt ;
assignstmt: (expr_index | ID) ASSIGN expr SEMI ;
ifstmt: IF LB expr RB stmt (ELSE stmt)? ;
forstmt: FOR LB ID ASSIGN expr COMMA expr COMMA expr RB stmt;
whilestmt: WHILE LB expr_bool RB (stmt);
dowhilestmt: DO blockstmt WHILE LB expr RB SEMI;  
breakstmt: BREAK SEMI ;
continuestmt: CONTINUE SEMI; 
returnstmt:  RETURN expr? SEMI;
callstmt: ID LB exprlist RB SEMI ; 
blockstmt: LCB stmtlist RCB ;
stmtlist: stmtprime |  ;
stmtprime: stmt stmtprime | stmt; 




fragment Digit: [0-9] ;
fragment Digits: Digit+ ;
fragment Letter: [a-zA-Z] | '_' ; 
fragment StringChar: ~[\b\t\n\f\r"\\] | Escape_Seq ;
fragment Escape_Seq: '\\' [btnfr"'\\] ;

fragment DECPART: DOT Digits  ;
fragment EXPART: (DOT Digits)? [eE] [+-]? Digits  ; 

BOOLLIT: TRUE | FALSE ;

 
//keyworks
MAIN: 'main'  ;
AUTO: 'auto' ; 
BREAK: 'break' ;
BOOLEAN: 'boolean' ; 
DO: 'do' ;  
ELSE: 'else' ;
FALSE: 'false';
FLOAT: 'float' ; 
FOR: 'for' ; 
FUNCTION: 'function'  ;
IF:  'if'  ; 
INTEGER:  'integer' ; 
RETURN:  'return' ; 
STRING: 'string'  ;
TRUE: 'true'  ;
WHILE: 'while'  ; 
VOID: 'void'  ;  
OUT:  'out'  ; 
CONTINUE: 'continue' ; 
OF:  'of'  ;
INHERIT: 'inherit' ;
ARRAY: 'array' ;  


// Number
INTLIT: '0' | [1-9] [0-9]* ('_' ([0-9] [0-9]*))* {self.text = self.text.replace("_", "")} ;
FLOATLIT: INTLIT (DECPART | EXPART) {self.text = self.text.replace("_", "")}  ;
STRINGLIT: '"'  (StringChar)*? '"' {t = str(self.text) ; self.text = t[1:-1]};
//identifiers
ID: Letter (Letter | Digit)* ;

// OPERATORS
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
NOT_EQUAL: '!=';
LESS: '<';
LESS_EQUAL: '<=';
GREATER_EQUAL: '>=';
GREATER: '>';
EQUAL: '==';
ASSIGN: '=';
CONCAT: '::' ; 


//Separators
LB: '(' ; 
RB: ')' ;
LSB: '[' ;
RSB: ']';  
LCB: '{';
RCB: '}';
COLON: ':';  
COMMA: ','; 
DOT: '.' ; 
SEMI:  ';' ;

//Comment
COMMENT_LINE: ('//' (~[\n])*) -> skip;
COMMENT_MULTYLINE: '/*' .*? '*/' ->skip;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment Esc_illigal: '\\' ~[btnrf"'\\] ;


ILLEGAL_ESCAPE: '"' StringChar* Esc_illigal 
{
	t = self.text
	raise IllegalEscape(t[1:])
};
UNCLOSE_STRING: '"' (StringChar | ~["])* EOF 
{
	t = self.text;
	raise UncloseString(t[1:]);
};
ERROR_CHAR: . {raise ErrorToken(self.text)};