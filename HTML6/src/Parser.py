####################################
###### SETUP/ VAR-DECLARATION
####################################
ABC = "abcdefghijklmnopqrstuvwxyzüäö_123456789."
ONE_TAGS = ["hr", "br", "favicon", "map", "calendar", "img", "icon", "link", "meta", "source", "track",
                        "wbr", "load"]

# Parsing vars
PATH = "../Code/index.html6"
TEMPLATE_PATH = "./Template.html6"
code = ""
char_idx = -1
cur_char = ""
ast = []


####################################
###### Tag Class
####################################
class Tag:
    def __init__(self, name: str, params: dict, value: str or list): # type: ignore
        self.name = name
        self.params = params
        self.value = value

    def __repr__(self):
        return f"[{self.name = }, {self.params = }, {self.value = }]"


####################################
###### HELPER FUNCTIONS
####################################

# Skip Whitespaces
def skip():
    global cur_char
    if cur_char is None:
        return
    while cur_char is not None and cur_char in " \n\t":
        advance()


# Is cur_char == tok else Error
def check(tok, sSkip=True, error=""):
    if cur_char not in tok:
        print_error(tok, error)
        return False
    advance()
    if sSkip:
        skip()
    return True


def print_error(tok, error=""):
    global char_idx, code, cur_char
    line_start = code.rfind('\n', 0, char_idx) + 1 if char_idx > 0 else 0
    line_end = code.find('\n', char_idx)
    current_line = code[line_start:line_end]
    line_number = code.count('\n', 0, char_idx) + 1
    print(f"\033[91mERROR: '{tok}' expected, but '{cur_char}' given.\n{error}In Line {line_number}: {current_line}\033[0m")





def make_str(add: str = "", escape: bool = False):
    myString = ""
    if escape:
        while cur_char is not None and cur_char not in add:
            myString += cur_char
            advance()
    else:
        while cur_char is not None and cur_char in ABC + add:
            myString += cur_char
            advance()
    return myString


def advance():
    global char_idx
    global cur_char
    char_idx += 1
    if char_idx < len(code):
        cur_char = code[char_idx]
        return cur_char
    else:
        cur_char = None
        return None


####################################
###### MAIN FUNCTION
####################################
def generate_ast():
    global code, ast
    code = open(PATH, "r").read()
    print(code)
    if code.strip() == r"\template":
        code = open(TEMPLATE_PATH, "r").read()
        open(PATH, 'w').write(code)
        print("DID IT, Tempalte")
    advance()
    ast = html()
    return ast


def html(escape=None):
    global name
    temp_ast = []
    while cur_char is not None:
        skip()
        if cur_char == "<":
            advance()
            skip()

            # </Sup_Tag>
            if cur_char == "/":
                advance()
                _name = make_str()
                if _name == escape:
                    if not check(">", f"Try to close the '{escape}' Tag. But got '{_name}'\n"): return False
                    return temp_ast
                else:
                    print("ERROR, unknown closing tag: ", _name)
                    return False

            # make comments
            if cur_char == "!":
                advance()
                if cur_char == "-":
                    advance()
                    if cur_char == "-":
                        advance()
                        while True:
                            if cur_char == "-":
                                advance()
                                if cur_char == "-":
                                    advance()
                                    if cur_char == ">":
                                        advance()
                                        break
                            advance()
                    else:
                        print_error("<!--", "Comments must start with <!--") 
                        return False
                else:
                    print_error("<!--", "Comments must start with <!--") 
                continue

            # <name>
            name = make_str("-.ABCDEFGHIJKLMNOP")
            skip()
            params = {}
            print("OPEN TAG: ", name)

            # <Tag param="value">
            while cur_char != ">":
                param = make_str("")
                if not check("=", "Tryed to make a vaule."): return False
                if not check(["'", '"'], False): return False
                params[param] = make_str(["'", '"'], True)
                if not check(["'", '"']): return False
            advance()
            skip()

            # br, hr, ...
            if name in ONE_TAGS:
                temp_ast.append(Tag(name, params, None))
                continue

            # <Tag>value</Tag>
            print("MAKE VALUE")
            if name in ["css", "style"]:
                value = scss()
            elif name in ["js", "script"]:
                value = js()

            elif cur_char == "<":
                value = html(name)
                if value == False: return False
                temp_ast.append(Tag(name, params, value))
                continue

            else:
                print("VLAUE IS A STRING")
                value: list = []
                while True:
                    value.append(make_str("<", True))
                    print("VLAUE:", value)
                    if (char_idx <= len(code)) and (code[char_idx+1] != "/"):
                        tem2 = html()
                        print("TEMP2: ", tem2)
                        value.append(tem2)
                    else:
                        break


            # </Tag>
            print("CLOSING TAG", name)
            if not check("<"): return False
            if not check("/"): return False
            if (a := make_str()) != name:
                print(f"ERROR, closing Tag should be {name} but is {a}")
                return False
            skip()
            if not check(">"): return False
            temp_ast.append(Tag(name, params, value))

        else:
            return temp_ast
    return temp_ast


def scss():
    css = make_str("<", True)
    return css


def js():
    js = ""
    while cur_char != "<":
        js += make_str("<", True)
        # Escape tokens
    return js


if __name__ == "__main__":
    print(generate_ast())
