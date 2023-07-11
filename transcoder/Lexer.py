#######################################
# DOKUMENTATION
#######################################
'''
You can change "Tokens" and "Keywords".

USAGE:
import Lexer
lexer = Lexer(File)             # "File" is the code/ text/ file (string) you want to transform into a token array
tokens = lexer.makeTokens()     # "tokens" is an array with all tokens

'''
#######################################
# IMPORTS
#######################################

from users.Tokens import *


#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'äüöÄÜÖß'
LETTERS_DIGITS = LETTERS + DIGITS


#######################################
# TOKENS
#######################################

class Token:
  def __init__(self, type_, value = None):
      self.type = type_
      self.value = value

  def matches(self, type_, value = None):
      return self.type == type_ and self.value == value

  def __repr__(self):
      if self.value: return f'{self.type}:{self.value}'
      return f'{self.type}'
  
class CustomError(Exception):
    Exception


#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, text):
        self.tokens = []
        self.index = -1
        self.text = text
        self.tabCount = 0
        self.current_char = None
        self.advance()

    def advance(self, step = 1):
        self.index += step
        self.current_char = self.text[self.index] if self.index < len(self.text) else None

    def pre(self, step = 1):
        self.index -= step
        self.current_char = self.text[self.index] if self.index >= 0 else None

    def check(self, _idx):
        idx = self.index + _idx
        return self.text[idx] if idx >= 0 and idx < len(self.text) else None

####################################

    def makeTokens(self):
        if self.index == 0 and self.current_char != None:
            self.make_Tab()
        while self.current_char != None:
            if self.current_char in '\n':              # Skip Whitespace ---------------------------------------
                self.make_Tab()
            elif self.current_char in ';\n':            # New Line -------------------------
                self.tokens.append(Token(NEWLINE))
                self.advance()
                while self.current_char != None and self.current_char in ' \n':
                    self.advance()
                self.tokens.append(Token(TAB))
            elif self.current_char in DIGITS:           # Numbers
                self.tokens.append(self.make_number())
            elif self.current_char in ["'",'"','`']:    # Normal String
                self.tokens.append(self.make_string(self.current_char))
            elif self.current_char in LETTERS:          # Identifier
                self.tokens.append(self.make_identifier())
            else:                                       # Normal Tokens from Tokens dict
                res = ""
                finished = False
                for token in Tokens:
                    for i, char in enumerate(token):
                        if char != self.check(i):
                            res = ""
                            break
                        res += char
                    if res != "":
                        self.tokens.append(Token(Tokens[res]))
                        self.advance(len(res))
                        finished = True
                        break
                if not finished:
                    print(f'Unknown token/ char at: {self.current_char}')      # Else Error
                    break
        return self.tokens


#######################################
# MAKE FUNCTIONS
#######################################

    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
            num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(INT, int(num_str))
        return Token(FLOAT, float(num_str))

    def make_string(self, escapeToken, fString = False):
        string = ''
        self.advance()
        while self.current_char != None and (((self.current_char != escapeToken) and (self.check(-1) != '\\')) or (self.current_char != escapeToken)):
            string += self.current_char
            self.advance()
            escape_character = False
        self.advance()
        if fString:
            return Token(F_STRING, string)
        return Token(STRING, string)

    def make_identifier(self):
        id_str = ''
        while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance()
        tok_type, str = [KEYWORD, id_str.upper()] if id_str.upper() in KEYWORDS else [IDENTIFIER, id_str]
        return Token(tok_type, str)


#######################################
# RUN
#######################################
if __name__ == '__main__':
    # This is to test the script
    lexer = Lexer(open("/home/max/Schreibtisch/Code-master/transcoder/test.txt", "r").read())
    print(lexer.makeTokens())
