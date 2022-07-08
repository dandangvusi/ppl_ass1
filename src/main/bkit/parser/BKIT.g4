grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options {
	language = Python3;
}

// DANG VU SI DAN - 2020017

program: EOF;

// ================================================================== LEXER ==================================================================

// FRAGMENTS
fragment DEGIT: [0-9];
fragment DEGIT_NO_ZERO: [1-9];
fragment OCT_DEGIT: [0-7];
fragment OCT_DEGIT_NO_ZERO: [1-7];
fragment HEX_CHAR: [A-F];
fragment HEX_PREFIX: ('0X' | '0x');
fragment OCT_PREFIX: ('0O' | '0o');
fragment FLT_INT_PART: ('0' | [1-9] [0-9]*);
fragment FLT_DEC_PART: '.' [0-9]*;
fragment FLT_EXP_PART: ('e' | 'E') ('+' | '-')? (
		'0'
		| [1-9][0-9]*
	);
fragment ESCAPE_CHAR: '\\' [bfrnt'\\];
fragment DOUBLE_QUOTE_CHAR: '\'"';

// LITERALS
DEC_INT_LIT: ('0' | DEGIT_NO_ZERO DEGIT*);
HEX_INT_LIT:
	HEX_PREFIX (DEGIT_NO_ZERO | HEX_CHAR) (DEGIT | HEX_CHAR)*;
OCT_INT_LIT: OCT_PREFIX OCT_DEGIT OCT_DEGIT_NO_ZERO*;
FLT_LIT:
	FLT_INT_PART (FLT_DEC_PART FLT_EXP_PART? | FLT_EXP_PART);
BOOL_LIT: (TRUE | FALSE);
STRLIT:
	'"' (DOUBLE_QUOTE_CHAR | ESCAPE_CHAR | ~["\\\n\r])* '"' {self.text = self.text[1:-1]};
ARRAY_LIT:
	'{' (
		DEC_INT_LIT
		| HEX_INT_LIT
		| OCT_INT_LIT
		| FLT_LIT
		| STRLIT
		| ARRAY_LIT
	) (
		',' (
			DEC_INT_LIT
			| HEX_INT_LIT
			| OCT_INT_LIT
			| FLT_LIT
			| STRLIT
			| ARRAY_LIT
		)
	)* '}';

// KEYWORDS
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSELF: 'Elself';
ENDBODY: 'Endbody';
ENDIF: 'Endif';
ENDFOR: 'Endfor';
ENDWHILE: 'Endwhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
TRUE: 'True';
FALSE: 'False';
ENDDO: 'Enddo';

// OPERATOR
ADD_I: '+';
SUB_I: '-';
MUL_I: '*';
DIV_I: '\\';
MOD_I: '%';
ADD_F: '+.';
SUB_F: '-.';
MUL_F: '*.';
DIV_F: '\\.';
EQ_I: '==';
NEQ_I: '!=';
LT_I: '<';
GT_I: '>';
LTE_I: '<=';
GTE_I: '>=';
NEQ_F: '=/=';
LT_F: '<.';
GT_F: '>.';
LTE_F: '<=.';
GTE_F: '>=.';
NOT: '!';
AND: '&&';
OR: '||';
ASSIGN: '=';

// SEPARATORS
LS: '[';
RS: ']';
LB: '(';
RB: ')';
LC: '{';
RC: '}';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

// IDENTIFIERS
ID: [_a-zA-Z][_a-zA-Z0-9]*;

// COMMENTS
COMMENT: ('**' .*? '**') -> skip;
// WHITE SPACE
WS: [ \t\r\n]+ -> skip;
ILLEGAL_ESCAPE:
	'"' (DOUBLE_QUOTE_CHAR | ESCAPE_CHAR | ~["\\\n\r])* '\\' ~[bfrnt'\\] {
    raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING:
	'"' (DOUBLE_QUOTE_CHAR | ESCAPE_CHAR | ~["\\\n\r])* {
	raise UncloseString(self.text[1:])
};
ERROR_CHAR:
	. {
	raise ErrorToken(self.text);
};