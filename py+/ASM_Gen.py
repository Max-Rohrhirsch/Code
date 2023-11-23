#######################################
# DOKUMENTATION
#######################################
'''
You can edit grammar.py

USAGE:
from Lexer import Lexer
from Parser import Parser

lexer = Lexer(File)             # 'File' is the code/ text/ file (string) you want to transform into a token array
tokens = lexer.makeTokens()     # 'tokens' is an array with all tokens
parser = Parser(tokens)
ast = parser.parse()			# 'ast' is a nested Array

'''
#######################################
# IMPORTS
#######################################

from users.Tokens import *
from Lexer import *



#######################################
# CONSTANTS
#######################################

# exec(open('./users/grammar.py').read()) # Includes the grammar


#######################################
# BYTECODE GENERATOR
#######################################



#######################################
# RUN
#######################################

if __name__ == '__main__':
	# This is to test the script
	lexer = Lexer('if a : for a IN 3:')
	parser = Parser(lexer.makeTokens())
	print(parser.parse())
