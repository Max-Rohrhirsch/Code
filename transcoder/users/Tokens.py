#######################################
# DOCUMENTATION
#######################################
'''
KEYWORDS and Tokens are self explainable.
Everything under KEYWORDS are "special" Tokens
which are a bit more complicated.

IMPORTANT
Everything in Tokens must be sorted by the length of the keys.
The longest Tokens first and the shortest last

'''
#######################################
# TOKENS
#######################################
Tokens = {

    # Triple Tokens
	'<<='			: 'LS_EQAUL',
	'>>='			: 'RS_EQUAL',
	'//='			: 'DOUBLESLASH_EQUAL',
	'**='			: 'MUL_EQUAL',
	'...'			: 'ELLIPSIS',

    # Double Tokens
    '**'            : 'POW',
    '=>'            : 'PFEIL',
    '||'            : 'OR',
    '&&'            : 'AND',
    '=='            : 'EE',
	'@='			: 'AT_EQUAL',
	'|='			: 'OR_EQUAL',
	'^='			: 'XOR_EQUAL',
	'&='			: 'AND_EQUAL',
    '!='            : 'NE',
	':='			: 'DOUBLEPOINT_EQUAL',
    '<='            : 'LTE',
    '>='            : 'GTE',
    '+='            : 'PLUS_EQUAL',
    '-='            : 'MINUS_EQUAL',
    '*='            : 'MUL_EQUAL',
    '/='            : 'DIV_EQUAL',
	'//'			: 'SDIV EQUAL',
    '%='            : 'MOD_EQUAL',
    '>>'            : 'B_RR',
    '<<'            : 'B_RL',
	'->'			: 'RARROW',

    # Single Tokens
    '+'     	    : 'PLUS',
    '-'    	        : 'MINUS',
    '*'      	    : 'MUL',
    '/'      	    : 'DIV',
    '='			    : 'EQ',
    '%'             : 'MODULO',
    '|'             : 'B_OR',
    '&'             : 'B_AND',
    '!'             : 'NOT',
    '<'             : 'LT',
    '>'             : 'GT',
	'^'				: 'CIRCUMFLEX',
	'~'				: 'TILDE',
    '('          	: 'LPAREN',
    ')'   	        : 'RPAREN',
    '{'             : 'LSQUARE',
    '}'             : 'RSQUARE',
    '['             : 'RWPAREN',
    ']'             : 'LWPAREN',
	':'				: 'DOBLEPOINT',
    ';'             : 'SEMIKOLON',
    ','		        : 'COMMA',
    '.'             : 'DOT',
}


KEYWORDS = [
  'FALSE',
  'TRUE',
  'NONE',
  'NOT',
  'OR',
  'AND',
  'ELSE',
  'IF',
  'ELIF',
  'RETURN',
  'YIELD',
  'BREAK',
  'PASS',
  'CONTINUE',
  'IMPORT',
  'CLASS',
  'DEF',
  'FROM',
  'ASSERT'
  'AS',
  'DEL',
  'IS',
  'LAMBDA',
  'RAISE',
  'TRY',
  'EXCEPT',
  'FINAL',
  'GLOBAL',
  'FOR',
  'WHILE',
  'IN',
  'WITH'
]

TAB				= 'TAB'
F_STRING		= 'F_STRING'
INT		    	= 'INT'
FLOAT    	    = 'FLOAT'
STRING		    = 'STRING'
IDENTIFIER   	= 'IDENTIFIER'
KEYWORD		    = 'KEYWORD'
COMMENT         = 'COMMENT'
NEWLINE		    = 'NEWLINE'
EOF				= 'EOF'
