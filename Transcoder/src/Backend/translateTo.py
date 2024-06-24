#######################################
#           DOCUMENTATION
#######################################
"""
    The translateTo is the Code that translates the AST into
    the other Language.
    he has to read the grammar sheet and translate your code.

    SYNTAX:


    TODO: experiment
    TODO: grammar lesen und als string importieren
    TODO: switch case für jedes durch iterieren

"""
#######################################
#              VARS/CONSTS
#######################################
code = ""
ast = {}
char_idx = -1
grammar = {}
cur_char = ""


#######################################
#           HELPER FUNCTIONS
#######################################
def make_text(appending=""):
    global code, char_idx, cur_char
    tmp_text = ""
    while cur_char.lower() in "abcdefghijklmnopqrstuvwxyz_" + appending:
        advance()
    return tmp_text


def make_string():
    global cur_char, char_idx
    if not check("'"): return False
    string = make_text(" ()")
    if not check("'"): print(f"UNKNOWN TOKEN: {cur_char}")
    return string


def advance(steps=1):
    global code, char_idx, cur_char
    if char_idx + steps < len(code):
        char_idx += steps
        cur_char = code[char_idx]
    else:
        cur_char = None


def skip():
    global code, char_idx
    while cur_char in "\t \n":
        advance()


def check(char):
    global cur_char
    if cur_char == char:
        return True
    return False


def checkAt(step, char):
    global cur_char, code, char_idx
    if char_idx + step < len(code) and code[char_idx + step] == char:
        return True
    return False


#######################################
#           MAIN FUNCTIONS
#######################################

def translate(_ast: dict, toLanguage: str = "c"):
    global code, ast, char_idx, grammar, cur_char
    ast = _ast

    toGrammar_text = open(f"../Languages/{toLanguage}/{toLanguage}.toGrammar", "r").read
    print(toGrammar_text)

    while cur_char is not None and char_idx < len(code) + 1:

        # Check for Selector
        skip()
        selector = make_text()
        if not check(":"): raise print(f"ERROR in toGrammar: the Selector '{selector}' must have a ':' after it!")
        advance()

        # For Collumn
        while True:
            skip()
            if not check("|"):
                raise print(f"ERROR in toGrammar: the Selector '{selector}' must have a '|' in every column!")
            advance()
            setting = " "
            if not check(" "):
                if not checkAt(1, "|"):
                    raise print("ERROR in toGrammar: In Setting after '|' must me a whitespace or a Char and '|'")

                # |A|
                advance(2)
                setting = cur_char
                if setting not in "ISVX ":  # Check if the Setting is correct
                    raise print("Setting must be one of these: ISVX or a whitespace!")

            # Text for each segment
            column_text = []
            while True:
                skip()
                tmp_text = ""
                if cur_char == "'":
                    advance()
                    tmp_text += make_text("\\")
                    if cur_char != "'": raise print("ERROR in toGrammar: Invalid character")


#######################################
#                 RUN
#######################################
if __name__ == "__main__":
    ast = {'type': 'Module', 'body': [{'type': 'If', 'test': {'type': 'Compare', 'left': {'type': 'Name', 'id': 'a',
                                                                                          'ctx': {'type': 'Load'}},
                                                              'ops': [{'type': 'Eq'}], 'comparators': [
            {'type': 'Constant', 'value': 7, 'kind': None}]}, 'body': [
        {'type': 'Assign', 'targets': [{'type': 'Name', 'id': 'b', 'ctx': {'type': 'Store'}}],
         'value': {'type': 'Constant', 'value': 3, 'kind': None}, 'type_comment': None}], 'orelse': []}],
           'type_ignores': []}

