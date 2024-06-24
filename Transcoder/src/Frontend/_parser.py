#######################################
#           DOCUMENTATION
#######################################
"""
    This is the API for the Parsers in the Language Folder.
    Call myParse().
    In RUN is an example of how.
"""
#######################################
#              IMPORTS
#######################################
import ast
from src.Languages.python.build import parser


#######################################
#           MAIN FUNCTIONS
#######################################
def myParse(code_text: str, fromLanguage: str = "python"):
    try:
        exec(f"from src.Languages.{fromLanguage}.build.parser import parse_string")
    except Exception as e:
        raise print("ERROR: (_parser) Probably your Language does not exist!\n", e)

    parsed_result = parser.parse_string(code_text, "exec")
    return ast_to_json(parsed_result)


def ast_to_json(ast_node):
    if isinstance(ast_node, ast.AST):
        node_dict = {'type': type(ast_node).__name__}
        for field_name, field_value in ast.iter_fields(ast_node):
            node_dict[field_name] = ast_to_json(field_value)
        return node_dict
    elif isinstance(ast_node, list):
        return [ast_to_json(item) for item in ast_node]
    else:
        return ast_node


#######################################
#                RUN
#######################################
if __name__ == '__main__':
    # This is to test the script
    txt = open("../../code/test.txt", "r").read()
    ast = myParse(txt)
    print(ast)
