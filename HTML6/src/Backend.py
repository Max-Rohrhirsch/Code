####################################
###### IMPORTS
####################################
from Parser import Tag

import subprocess
import os


####################################
###### DECLARE VARS
####################################
BUILD_PATH = "../build/"

header = "const express = require('express');\nconst app = express();\n"
port = ""
js_code = ""
footer = """app.listen(port, () => {
\tconsole.log(`Server listening at http://localhost:${port}`);
});
"""


####################################
###### HELPER FUNCTIONS
####################################

def is_node_installed():
    try:
        subprocess.run(["node", "--version"], check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def install_node():
    print("Node.js is not installed. Installing...")
    subprocess.run(["npm", "install", "-g", "n"])
    subprocess.run(["n", "latest"])


def initialize_express_project(build_path, js_code):
    print(f"Initializing Express project in {build_path}...")
    subprocess.run(["npx", "express-generator", build_path, "--no-view"])
    
    # Write custom JS code to app.js
    app_js_path = os.path.join(build_path, 'app.js')
    with open(app_js_path, 'w') as app_js_file:
        app_js_file.write(js_code)


####################################
###### MAIN FUNCTION
####################################
    
def make_backend(sup_element: Tag):
    if not is_node_installed():
        install_node()

    project_path = os.path.join(BUILD_PATH, "my-express-app")

    js_code = make_js_code(sup_element)
    if os.path.exists(project_path):
        print(f"Express project already exists in {project_path}. Overwriting...")
        file = open(project_path + "/app.js", 'w')
        file.write(js_code)
        file.close()
    else:
        initialize_express_project(project_path, js_code)
    print("Server setup completed!")


def make_js_code(tag: Tag) -> str:
    js_code = decode_backend(tag.value)
    result = header + "\n" 
    result += f"const port = {port};\n\n"
    result += js_code + "\n\n"
    result += footer 
    return result


def make_string(tag: Tag, tab=True) -> str:
    if type(tag.value) == str:
        result = ""
        if tab:
            result = "\t"
        result += tag.value.replace("\n", "\n\t")
        return result
    else:
        print("Error: Tag is not a string")
        return ""


def decode_backend(tag: Tag) -> str:
    tempCode = ""
    if type(tag) == list:
        for subTag in tag:
            tempCode += decode_backend(subTag)
        return tempCode

    if type(tag) == str:
        return tag
    
    ####################################
    ###### Spezial Tags
    ####################################

    if tag.name == "port":
        global port
        port = tag.value
    

    elif tag.name == "static":
        tempCode += f"\napp.use(express.static('{make_string(tag, False)}'))"
    

    elif tag.name == "get":
        tempCode += f'app.get("{tag.params.get("url", "/")}", (req, res) => {{\n'
        if "sendFile" in tag.params:
            tempCode += f'\tres.sendFile("{make_string(tag.params.get("sendFile"))})\n'
        elif "send" in tag.params:
            tempCode += f'\tres.send("{make_string(tag.params.get("send"))})\n'
        else: 
            tempCode += make_string(tag)
        tempCode += "\n})\n"


    elif tag.name == "post":
        tempCode += f'app.post("{tag.params.get("url", "/")}", (req, res) => {{\n'
        if "sendFile" in tag.params:
            tempCode += f"\tres.sendFile('{make_string(tag.params.get('sendFile'))}')\n"
        elif "send" in tag.params:
            tempCode += f"\tres.send('{make_string(tag.params.get('send'))}')\n"
        else:
            tempCode += make_string(tag)
        tempCode += "\n})\n"


    elif tag.name == "script":
        tempCode += make_string(tag)

    
    else:
        print(f"Error: Tag '{tag.name}' not found")
        return ""
    return tempCode


####################################
###### RUN
####################################
    
if __name__ == '__main__':
    tag = Tag("backend", None, [Tag("port", None, "3000"), Tag("get", {"url": "/"}, "res.send('Hello World')"), Tag("post", {"url": "/post/"}, "console.log('hi')"), Tag("static", None, "public/")])
    make_backend(tag)