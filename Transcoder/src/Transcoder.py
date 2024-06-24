#######################################
#           DOCUMENTATION
#######################################
"""
    This is the main Script to combine all the Components.

    # raise NameError('HiThere')
    #
    #

    TODO: translateTo + toGrammar

    TODO: libarys and libary converter
    TODO: optimzer with vars
"""
#######################################
#              IMPORTS
#######################################
from Frontend.optimizer import optimize
from Backend.translateTo import translate

#######################################
#            CONSTS/VARS
#######################################
BUILD_URL = "../build/"
CODE_URL = "../code/"


#######################################
#          HELPER FUNCTIONS
#######################################

def to_file(text: str, name: str = "NoName.txt"):
    f = open(name, "a")
    f.write(text)
    f.close()


#######################################
#           MAIN FUNCTION
#######################################
def Translate(fileName: str = "test.txt", fromLanguage: str = "python", toLanguage: str = "c"):
    o_ast = optimize(CODE_URL + fileName, fromLanguage)
    print(o_ast)
    finished_code = translate(o_ast, toLanguage)
    print(finished_code)
    to_file(finished_code, fileName)


#######################################
#                RUN
#######################################
if __name__ == '__main__':
    Translate("test.txt", "python", "c")
