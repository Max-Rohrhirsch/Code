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

special = ['STRING', 'NUMBER', 'VALUE', 'CONDITION', 'STATEMENTS', 'FUNCTIONS']

syntax = [
	['FOR', IDENTIFIER, 'IN', INT, ':'],
	['IF', 'CONDITION', ':']
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
		self.preCalc()

	def advance(self, step = 1):
		self.tokIdx += step
		self.curTok = self.tokens[self.tokIdx] if self.tokIdx < len(self.tokens) else None

	def pre(self, step = 1):
		self.tokIdx -= step
		self.curTok = self.tokens[self.tokIdx] if self.tokIdx < len(self.tokens) else None

	def check(self, step = 1):
		Idx = self.tokIdx + step
		if Idx >= 0 and Idx < len(self.tokens):
			return self.tokens[Idx]
		return None

	def delWhite(self):
		while self.curTok in ' \t':
			self.advance()

	def matchE(self, token, value = None):
		if self.curTok.matches(token, value):
			return True
		raise CustomError(f'doesnt matches the following')

	def match(self, token, value = None):
		if self.curTok.matches(token, value):
			return True
		return False

	def ifMatch(self, _idx, _value, _val = None):
		if self.check(_idx) == Token(_value, _val):
			return True
		raise CustomError(f'doesn`t matches the following')

	def preCalc(self):
		for i, structure in enumerate(syntax):
			for j, token in enumerate(structure):
				if token.upper() in KEYWORDS:
					syntax[i][j] = Token(KEYWORD, token.upper())
				elif token in Tokens.keys():
					syntax[i][j] = Token(Tokens[token])
				elif token in special:
					pass
				else:
					syntax[i][j] = Token(token)


	################## MAIN FUNCTION ####################

	def parse(self):
		res = []
		finished = False
		while self.curTok != None:
			for structure in syntax:
				for i, token in enumerate(structure):
					# print(f'{self.check(i) = }  {token = }')
					if not (isinstance(token, str) or ((self.check(i).type == KEYWORD) and (self.check(i).value == token.value)) or (self.check(i).type == token.type)):
						res = []
						break
					elif isinstance(token, str):
						if token == 'NUMBER':
							res.append(self.make_check(i, ['INT', 'FLOAT'], [Tokens['+'], Tokens['*'], Tokens['-'], Tokens['**'], Tokens['/'], Tokens['%']]))
						elif token == 'STRING':
							res.append(self.make_check(i, ['STRING'], [Tokens['+'], Tokens['*']]))
						else:
							res.append(getattr(self, f'make_{token.lower()}')(i))
					else:
						res.append(token)
				if res:
					self.ast.append(res)
					self.advance(len(res))
					res = []
					finished = True
					break
			if not finished:
				print(f'Unknown token/ structure at: {self.curTok}')      # Else Error
				break
			finished = False
		return self.ast


#######################################
# MAKE FUNCTIONS
#######################################

	def make_condition(self, i):
		idx = i
		res = []
		if self.make_value(i):
			res.append(self.check(idx))
			idx += 1
			while self.check(i).type in ['<', '...']:
				res.append(self.check(idx))
				idx += 1
				if self.make_value(idx):
					res.append(self.check(idx))
					idx += 1
				else:
					raise CustomError(f'Expected: make contition 1')
			return res
		else:
			raise CustomError(f'Expected: make condition 2')

	def make_check(self, i, types, valTokens):
		idx = i
		res = []
		if self.check(i).type in types:
			res.append(self.check(idx))
			idx += 1
			while self.check(i).type in valTokens:
				res.append(self.check(idx))
				idx += 1
				if self.check(i).type in types:
					res.append(self.check(idx))
					idx += 1
				else:
					raise CustomError(f'Expected: {valTokens}')
			return res
		else:
			raise CustomError(f'Expected: {types}')

	def make_value(self, i):
		pass

	def make_statements(self, i):
		pass

	def make_function(self, i):
		idx = i
		res = []
		while self.check(idx) == Token('NEWLINE'):
			idx += 1
		while self.ifMatch(idx, "KEYWORD", "DEF"):
			if self.check(idx + 1) == Token('IDENTIFIER'):
				res.append([self.check(idx + 1).value])
			else:
				CustomError(f'doesn`t matches the following')

			self.ifMatch(idx + 2, Tokens["("])
			res[-1].append(self.make_value(idx + 3))
			self.ifMatch(idx + 4, Tokens[")"])
			self.ifMatch(idx + 5, Tokens[":"])

			res[-1].append(self.make_statements(idx + 6))


#######################################
# RUN
#######################################

if __name__ == '__main__':
	# This is to test the script
	lexer = Lexer('if a : for a IN 3:')
	parser = Parser(lexer.makeTokens())
	print(parser.parse())
