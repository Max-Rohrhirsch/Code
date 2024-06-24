#######################################
#           DOCUMENTATION
#######################################
"""
    This code takes the PAth and Language as input
    and gives it to the Parser and takes back the ast.
    The Function "optimize" will return the optimized ast.

    TODO: vars analyzing
"""
#######################################
#              IMPORTS
#######################################
from src.Frontend._parser import myParse


#######################################
#           MAIN FUNCTIONS
#######################################
def optimize(path: str, fromLanguage: str = "python"):
    try:
        txt = open(path, "r").read()
    except Exception as e:
        raise print(f"ERROR: The File '{path}' does not exist!")

    ast = myParse(txt, fromLanguage)
    return ast


class Optimizer:
    def __init__(self, _ast):
        self.ast = _ast


#######################################
#                 RUN
#######################################
if __name__ == "__main__":
    o_ast = optimize("../../code/test.txt")
    print(o_ast)
