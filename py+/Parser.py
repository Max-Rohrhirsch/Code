#######################################
# DOCUMENTATION
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
# from users.Grammar import *
from Lexer import *


#######################################
# SMALL CLASSES
#######################################

class R:
	def __init__(self, token):
		self.token = token

class S:
	def __init__(self, token):
		if (token in ['OR', 'AND', 'NOT', '.', '+', '?']):
			self.token = token
		else:
			raise Exception("nope")
		
class L:
	def __init__(self, token, index):
		self.token = token
		self.index = index

#######################################
# CONSTANTS
#######################################

syntax = [
	['CODE', [R('IF'), S('OR'), R('FOR')]],
	['IF', ['IF', L('IDENTIFIER'), 'DOBLEPOINT', R('CODE')]],
	['FOR', ['FOR', 'IDENTIFIER', 'IN', R('NUMBER'), 'DOBLEPOINT']],
	['NUMBER', ['NUMBER']]
]
# exec(open('./users/grammar.py').read()) # Includes the grammar


#######################################
# PARSER
#######################################

class Parser:

	################## HELPFULL FUNCTIONS ####################
	def __init__(self, tokens):
		self.tokens = tokens
		self.ast = []
		self.tokIdx = -1
		self.advance()

	def advance(self, step = 1):
		self.tokIdx += step
		self.curTok = self.tokens[self.tokIdx] if self.tokIdx < len(self.tokens) else None

	def pre(self, step = 1):
		self.tokIdx -= step
		self.curTok = self.tokens[self.tokIdx] if self.tokIdx < len(self.tokens) else None

	def get_match(self, TOKEN_ID):
		for index, el in syntax:
			if el[0] == TOKEN_ID:
				return syntax[index][1]
		return None

	################## MAIN FUNCTION ####################

	def parse(self):
		while self.tokens != None:
			self._match(self.get_match('CODE'))
			
	def _match(self, tokens):
			temp_ast = []
			for element in syntax[0][1]:
				if type(element) == '__main__.R':
					return self._match(self.get_match(element))

				elif type(element) == '__main__.S':
					pass

				elif type(element) == '__main__.L':
					if self.curTok == Token(element):
						temp_ast.append(self.curTok) 
						continue

				elif type(element) == 'list':
					pass
				
				elif type(element) == 'str':
					if self.curTok == Token(element):
						continue



#######################################
# RUN
#######################################

if __name__ == '__main__':
	# This is to test the script
	lexer = Lexer('if a : for a IN 3:')
	parser = Parser(lexer.makeTokens())
	print(parser.parse())
