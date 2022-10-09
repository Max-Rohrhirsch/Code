#######################################
# DOKUMENTATION
#######################################
'''
You can edit Grammar.py and Tokens.py

USAGE:
from Lexer import Lexer
from Parser import Parser
from Transformer import transformer

lexer = Lexer(File)               # "File" is the code/ text/ file (string) you want to transform into a token array
tokens = lexer.makeTokens()       # "tokens" is an array with all tokens

parser = Parser(tokens)
ast = parser.parse()			  # "ast" is a nested Array

transformer = Transformer(ast)
cppCode = transformer.translate() # "cppCode" is the end result of everything. It is the finished c++ code.

# Aditional
file = open('translatedPythonCode.cpp', 'w')
file.write(cppCode)
file.close()

'''
#######################################
# IMPORTS
#######################################

from users.Tokens import *
exec(open("transcoder/users/Grammar.py").read())
from Lexer import *
import math


#######################################
# CONSTANTS
#######################################

NUMBER = [INT, FLOAT]
VALUE = [INT, FLOAT, STRING]
# exec(open('./users/Grammar.py').read()) # Includes the grammar

syntax = [
	["FOR", IDENTIFIER, "IN", INT, ":"],
	["IF", IDENTIFIER, '==', INT]
]


#######################################
# Transformer
#######################################
class Transformer:
	def __init__(self, ast):
		self.before = ''
		self.code = ''

		self.ast = ast



	def flatten(self, _array):
		if isinstance(_array, list):
			res = ''
			for element in _array:
				res += str(self.flatten(element))
			return res
		return str(_array)

	#############################


	# ast: [["FOR", IDENTIFIER, INT, [...]]   //Tokens
	# "FOR": 			[[],["FOR", param[1], "in", param[2], ":", "\n", param[3]]]


	def transform(self, _ast = None):
		if not _ast:
			_ast = self.ast
		for structure in _ast: 								# Goes trough all statements [[],[]]
			for element in trans[structure[0]][0]:			# bauplan id = for ... durch jedes element im bauplan
				if isinstance(element, str):
					self.before += element
				elif isinstance(element, int):
					for structure_element in structure[element]:
						self.before += f'{self.flatten(element)}'
			for element in trans[structure[0]][1]:
				if isinstance(element, str):
					self.code += element
				elif isinstance(element, int):
					if element < 0:
						element *= -1

					else:
						for structure_element in structure[element]:
							self.code += f'{self.flatten(structure_element)}'
		return self.before, self.code





#######################################
# RUN
#######################################
if __name__ == '__main__':
	# This is to test the script
	# lexer = Lexer("if a == 8")
	# pseudo = encoder(lexer.makeTokens())
	code = Transformer([["FOR", "a", "3 + 3", ["4", "5", ["6"]]]])
	print(code.transform()[1])
