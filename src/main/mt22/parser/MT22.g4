grammar MT22;

@lexer::header {
from lexererr import *
}

@members {
	def check_vardecl_full_format(self, idlist, exprlist):
		return len(idlist.split(',')) == len(exprlist.split(','))
}

options{
	language=Python3;
}

program: decllist EOF ;
decllist: decl decllist | decl ; 
decl: vardecl | funcdecl ; 
vardecl: idlist COLON typ (ASSIGN exprlist {check_vardecl_full_format($idlist.text, $exprlist.text)}?)? SEMI ;  
idlist: ID COMMA idlist | ID ; 
typ: BOOLEAN | INTEGER | STRING | FLOAT | arraytyp | AUTO ;
arraytyp: ARRAY LSB INTLIT RSB OF (BOOLEAN | INTEGER | STRING | FLOAT) ; 


funcdecl: (ID | MAIN) COLON FUNCTION returntype LB paramlist RB (INHERIT ID)? body  ;
returntype: BOOLEAN | INTEGER | STRING | FLOAT | VOID ;
paramlist: paramprime | ; 
paramprime: param COMMA paramprime | param ; 
param: INHERIT? OUT? ID COLON typ ;

expr: expr1 CONCAT expr1 | expr1 ; 
expr1: expr2 ( EQUAL | NOT_EQUAL | GREATER | GREATER_EQUAL | LESS | LESS_EQUAL) expr2 | expr2; 
expr2: expr2 (AND | OR) expr3 | expr3 ; 
expr3: expr3 (PLUS | MINUS) expr4 | expr4 ;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5 ;
expr5: NOT expr6 | expr6;
expr6: MINUS expr7 | expr7 ; 
expr7: expr8 LSB expr8 RSB | expr8;
expr8: ID | INTLIT | FLOATLIT | STRINGLIT | arraylit | callexpr | subexpr  ;
arraylit: LCB exprlist RCB ;
callexpr: ID LB exprlist RB ;  
subexpr: LB expr RB ; 
exprlist: exprprime | ; 
exprprime: expr COMMA exprprime  | expr ;  


stmt: vardecl | assignstmt | ifstmt | forstmt | whilestmt | dowhilestmt | breakstmt | continuestmt | returnstmt | callstmt | blockstmt ;
assignstmt: expr7 | ID ASSIGN expr SEMI ;
ifstmt: IF LB expr RB (stmt | blockstmt) (ELSE stmt | blockstmt)? ;
forstmt: FOR LB ID ASSIGN expr COMMA expr1 COMMA expr RB (stmt | blockstmt);
whilestmt: WHILE LB expr1 RB (stmt | blockstmt);
dowhilestmt: DO blockstmt WHILE LB expr1 RB  SEMI;  
breakstmt: BREAK SEMI ;
continuestmt: CONTINUE SEMI; 
returnstmt:  RETURN expr SEMI;
callstmt: ID LB exprlist RB SEMI ; 
blockstmt: LCB stmtlist RCB ;
stmtlist: stmtprime |  ;
stmtprime: stmt stmtprime | stmt; 

body: blockstmt ; 



//common
fragment Digit: [0-9] ;
fragment Digits: Digit* ;
fragment Letter: [a-zA-Z] | '_' ; 

// fragment of FLOAT
fragment DECPART: '.' Digits  ;
fragment EXPART: ('.' Digits)? [eE] '-'? Digits  ; 

//Comment
COMMENT_LINE: ('//' (~[\n])*) ;
COMMENT_MULTYLINE: '/*' .*? '*/' ;
 
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
INTLIT: '0' | '-'? [1-9] Digits ('_' ([1-9] Digits))* {self.text = self.text.replace("_", "")} ;
FLOATLIT: INTLIT (DECPART | EXPART) {self.text = self.text.replace("_", "")}  ;
STRINGLIT: '"'  ('\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' |'\\\\' | '\\"' | ~["])* '"' {self.text = self.text[1:-1]};
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
INCREMENT: '++';
CONCAT: '::' ; 
DECREMENT: '--';


//Separators
LB: '(' ; 
RB: ')' ;
LSB: '[' ;
RSB: ']';  
LCB: '{';
RCB: '}';
COLON: ':';  
COMMA: ',';  
SEMI:  ';' ;



WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;