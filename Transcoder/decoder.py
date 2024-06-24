#######################################
# DOCUMENTATION
#######################################
"""
Translates ast into another language.

USAGE:
txt = open("./test.txt", "r").read()

lexer = Lexer(txt)
parser = Parser(lexer.makeTokens())
optimizer = Optimizer(parser.parse())
decoder = Decoder(optimizer.optimize())

print(decoder.generate())
"""
#######################################
# IMPORTS
#######################################


#######################################
# Decoder
#######################################
operators: dict = {
    "Add": " + ",
    "Sub": " - ",
    "Mult": " * ",
    "Div": " / ",
    "Eq": " == ",
    "NotEq": " != ",
    "Lt": " < ",
    "LtE": " <= ",
    "Gt": " > ",
    "GtE": " >= ",
    "And": " && ",
    "Or": " || "
}


class Decoder:
    def __init__(self, _ast):
        self.ast = _ast
        self.code: str = ""

        self.vars: dict = {}
        self.imports: list = []
        self.alias: dict
        self.tab = 0

    def generate(self):
        self.code = self._generate(self.ast)

        myImport: str = ""
        for item in self.imports:
            myImport += f"#import <{item}.h>\n"
        if self.imports:
            self.code = myImport + "\n\n" + self.code

        return [self.code, self.imports]

    def _generate(self, _ast, parent_op=None, indent_level=0):
        tempCode: str = ""
        indent = "    " * indent_level  # Use four spaces for each level of indentation
        if type(_ast) == list:
            for el in _ast:
                tempCode += self._generate(el, parent_op, indent_level)
        else:
            match _ast["type"]:
                case "Module":
                    for el in _ast["body"]:
                        tempCode += self._generate(el, parent_op, indent_level)

                case "Expression":
                    tempCode += self._generate(_ast["body"], parent_op)

                case "BinOp":
                    left = self._generate(_ast["left"])
                    right = self._generate(_ast["right"])
                    op = operators[_ast["op"]["type"]]

                    # Check operator precedence and add parentheses if necessary
                    if _ast["left"]["type"] == "BinOp" and _ast["left"]["op"]["type"] != _ast["op"]["type"]:
                        left = f"({left})"

                    if _ast["right"]["type"] == "BinOp" and _ast["right"]["op"]["type"] != _ast["op"]["type"]:
                        right = f"({right})"

                    tempCode += f"{left}{op}{right}"

                case "Constant":
                    value = _ast["value"]
                    if isinstance(value, int):
                        return str(value)
                    elif isinstance(value, str):
                        return f'"{value}"'
                    elif isinstance(value, bool):
                        return "true" if value else "false"
                    else:
                        print(f"ERROR: Unsupported constant type: {type(value)}")

                case "Name":
                    tempCode += _ast["id"]

                case "Assign":
                    target = _ast["targets"][0]["id"]
                    value = self._generate(_ast["value"], indent_level=indent_level)
                    tempCode += f"{indent}{target} = {value};\n"

                case "Compare":
                    left = self._generate(_ast["left"])
                    tempCode += f"{left}"

                    for i, el in enumerate(_ast["ops"]):
                        op = operators[el["type"]]
                        right = self._generate(_ast["comparators"][i])
                        tempCode += f"{op}{right}"

                case "If":
                    cond = self._generate(_ast["test"], indent_level=indent_level)
                    tempCode += f"{indent}if ({cond}) {{\n"
                    tempCode += self._generate(_ast["body"], None, indent_level=indent_level + 1)
                    tempCode += f"{indent}" + "}"
                    if _ast["orelse"]:
                        tempCode += " else {\n"
                        tempCode += self._generate(_ast["orelse"], None, indent_level=indent_level + 1)
                        tempCode += f"{indent}" + "}"
                    tempCode += "\n"

                case "While":
                    cond = self._generate(_ast["test"], indent_level=indent_level)
                    tempCode += f"{indent}while ({cond}) {{\n"
                    tempCode += self._generate(_ast["body"], indent_level=indent_level + 1)
                    tempCode += f"{indent}" + "}\n"

                case "For":
                    target = _ast["target"]["id"]
                    # TODO TODO
                    tempCode += f"{indent}for (int {target} = 0; {target} < {_ast['iter']['args'][0]['value']}; {target}++) " + "{\n"
                    tempCode += self._generate(_ast["body"], indent_level=indent_level + 1)
                    tempCode += f"{indent}" + "}\n"

                case "Expr":
                    el = _ast["value"]
                    if "func" in el:
                        print(el)
                        function_name = el["func"]["id"]
                        if function_name == "print":
                            self.imports += "#import <std-lib>\n"
                            function_name = "printf"
                            tempCode += f"{indent}{function_name}("
                            for i, arg in enumerate(el["args"]):
                                if i > 0:
                                    tempCode += " + "
                                tempCode += arg["id"]
                            tempCode += ")\n"
                        elif function_name == "len":
                            ...

                        else:
                            tempCode += f"{indent}{function_name}("
                            for i, arg in enumerate(el["args"]):
                                if i > 0:
                                    tempCode += ", "
                                tempCode += arg["id"]
                            tempCode += ")"


                case "FunctionDef":
                    function_name = _ast["name"]
                    parameters = _ast["args"]["args"]
                    return_type = "void"  # You can modify this to handle other return types
                    tempCode += f"{indent}{return_type} {function_name}("
                    for i, param in enumerate(parameters):
                        if i > 0:
                            tempCode += ", "
                        param_name = param["arg"]
                        tempCode += f"int {param_name}"
                    tempCode += ") {\n"
                    tempCode += self._generate(_ast["body"], indent_level=indent_level + 1)
                    tempCode += f"{indent}" + "}\n"

                case "Return":
                    return_expr = self._generate(_ast["value"], indent_level=indent_level)
                    tempCode += f"{indent}return {return_expr};\n"

                case "Call":
                    function_name = self._generate(_ast["func"], indent_level=indent_level)
                    arguments = [self._generate(arg, indent_level=indent_level) for arg in _ast["args"]]
                    tempCode += f"{indent}{function_name}("
                    tempCode += ", ".join(arguments)
                    tempCode += ");\n"

                case "Import":
                    for a in _ast['names']:
                        self.imports += a['name']
                        # TODO: alias

                case "ImportFrom":
                    self.imports += _ast['module']


                case "SL-Comment":
                    tempCode += f"{indent}// {_ast['...']}\n"

                case "ML-Comment":
                    tempCode += f"{indent}/* {_ast['...']}*/\n"

                case _:
                    print(f"ERROR: type {_ast['type']} not found....")
        return tempCode


#######################################
# RUN
#######################################

if __name__ == '__main__':
    ...
