#######################################
# DOCUMENTATION
#######################################
'''
With syntax you can this language into psoidocode and than in an other language.
Syntax is an Array with the first element beeing the ID and the rest the syntax.
All Keywords and Tokens are automaticly transformed into Tokens. Special things like identifier,
datatypes, value and more complex things aren't Strings.

EXAMPLE:
["FOR", IDENTIFIER, "IN", INT, ":"],

Trans is for translating the psoidocode into this language.
Trans is an Dictionary with the ID beeing the key and the rest the syntax.
The First ellement is the code that comes before everything.
The Second one is the real code. Everything is a string except the parameters.

EXAMPLE:
"FOR": 			["FOR",param[1], "in", param[2], ":", "\n", param[3]]

'''
#######################################
# TOKENS
#######################################

syntax = [
	["FOR", IDENTIFIER, "IN", INT, ":"],
	["IF", IDENTIFIER, '==', INT]
]

trans = {
	"FOR": 			[[], ["for ", 1, " in ", 2, ":", "\n", -3]],
	"WHILE": 		[],
	"IF": 			[],
	"ASSIGNTMENT": 	[],
	"RETURN": 		[],
	"FUNKTION": 	[],
	"CLASS": 		[]
}
