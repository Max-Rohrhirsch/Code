
# Lehrtaste + tabs bis \n


if self.current_char in ' ':
    







        while self.current_char != None:
            if self.current_char in ' ':              # Skip Whitespace ---------------------------------------
                if self.check(-1) in " \n" or self.index == 1:
                    self.advance()
                    self.tokens.append(Token(TAB))
                    while self.current_char != '\n':
                        self.advance()
                else:
                    self.advance()


            elif self.current_char == '\t':              # Tabs ----------------
                self.tokens.append(Token(TAB))


            elif self.current_char in ';\n':            # New Line -------------------------
                self.tokens.append(Token(NEWLINE))
                self.advance()
                while self.current_char != None and self.current_char in ' \n':
                    self.advance()
                self.tokens.append(Token(TAB))








# .
