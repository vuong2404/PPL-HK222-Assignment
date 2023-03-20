// id: 2015108
grammar MT22;

@lexer::header {
from lexererr import *
}


options {
	language=Python3;
}


program: decllist EOF ;
decllist: decl decllist | decl ; 
decl: vardecl | vardeclfull | funcdecl; 
vardecl: idlist COLON typ SM ;
vardeclfull: vardeclrec SM ;
basecase: ID COLON typ ASSIGN expr ;
vardeclrec: ID CM vardeclrec CM expr | basecase ;
idlist: (ID CM idlist | ID) ; 
typ: BOOLEAN | INTEGER | STRING | FLOAT | arraytyp | AUTO | VOID ;
arraytyp: ARRAY LSB dimenlist RSB OF typ ; 
dimenlist: INTLIT CM dimenlist | INTLIT ;


funcdecl: (ID | MAIN) COLON FUNCTION typ LB paramlist RB (INHERIT ID)? blockstmt ;
paramlist: paramprime | ; 
paramprime: param CM paramprime | param ; 
param: INHERIT? OUT? ID COLON typ ;

expr: expr1 CONCAT expr1 | expr1 ; 
expr1: expr2 ( EQ | NEQ | GT | GEQ | LT | LEQ) expr2 | expr2; 
expr2: expr2 (AND | OR) expr3 | expr3 ; 
expr3: expr3 (PLUS | SUB) expr4 | expr4 ;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5 ;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7 ; 
expr7: expr_index | expr8;
expr_index: ID LSB exprlist RSB ;
expr8: ID | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | arraylit | callexpr | subexpr  ;
arraylit: LCB exprlist RCB ;
callexpr: ID LB exprlist RB ;  
subexpr: LB expr RB ; 
exprlist: exprprime |  ; 
exprprime:  (expr CM exprprime  | expr) ;  

exprlistdecl: (exprdeclprime |)   ;
exprdeclprime: (expr CM exprdeclprime | expr) ;



stmt: assignstmt  SM
	| ifstmt 
	| forstmt 
	| whilestmt 
	| dowhilestmt 
	| breakstmt 
	| continuestmt 
	| returnstmt 
	| callstmt
	| blockstmt ;
assignstmt: (expr_index | ID) ASSIGN expr;
ifstmt: IF LB expr RB stmt (ELSE stmt)? ;
forstmt: FOR LB ID ASSIGN expr CM expr CM expr RB stmt;
whilestmt: WHILE LB expr RB stmt;
dowhilestmt: DO blockstmt WHILE LB expr RB SM;  
breakstmt: BREAK SM ;
continuestmt: CONTINUE SM; 
returnstmt:  RETURN expr? SM;
callstmt: ID LB exprlist RB SM ; 
blockstmt: LCB (stmtlist) RCB ;
stmtlist: stmtprime |  ;
stmtprime: stmtblocks stmtprime | stmtblocks; 
stmtblocks: stmt | vardecl | vardeclfull ;


fragment Digit: [0-9] ;
fragment Digits: Digit+ ;
fragment Letter: [a-zA-Z] | '_' ; 
fragment StringChar: ~[\b\t\n\f\r"\\] | Escape_Seq ;
fragment Escape_Seq: '\\' [btnfr"'\\] ;

fragment DECPART: DOT Digit*  ;
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
FLOATLIT: (INTLIT (DECPART | EXPART) | INTLIT? DECPART EXPART) {self.text = self.text.replace("_", "")}  ;
STRINGLIT: '"'  (StringChar)*? '"' {t = str(self.text) ; self.text = t[1:-1]};
//identifiers
ID: Letter (Letter | Digit)* ;

// OPERATORS
PLUS: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
NEQ: '!=';
LT: '<';
LEQ: '<=';
GEQ: '>=';
GT: '>';
EQ: '==';
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
CM: ','; 
DOT: '.' ; 
SM:  ';' ;

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