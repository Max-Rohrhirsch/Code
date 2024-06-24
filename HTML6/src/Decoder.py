from Parser import generate_ast, Tag, ONE_TAGS
from Style import *
from Backend import make_backend

####################################
###### SETUP/ VAR-DECLARATION
####################################
ast = []
BUILD_PATH = "../build/"

html_code = ""
css = ""
js_code = ""

tab_count = 2
id_count = 0

header = ""
code_higlighting = False
used_elements = []
is_last_nl = True
slideshow_ids = []



####################################
###### SETUP/ VAR-DECLARATION
####################################
'''
############ HOW TO ###########
# better tables

# python in code 
# secure
# 	- Host on port
# 	- form with functions
# 	- Database


############ FEATURES #########
# ng for/ if {{  }}


############# BUGS ##########
# Text + tags as value
'''


####################################
###### MAIN FUNCTIONS
####################################
def generate_html5(_ast, file_name="test"):
    global ast, html_code, css, js_code, slideshow_ids
    footer_html = ""
    ast = _ast

    for element in ast:
        html_code += decode(element)

    for el in used_elements:
        if el not in known_elements:
            print(f"ERROR: {el} is used but not a known_element")
        footer_html += known_elements[el][0] if known_elements[el][0] else ""
        css += known_elements[el][1] if known_elements[el][1] else ""
        js_code += known_elements[el][2] if known_elements[el][2] else ""

    result = "<!DOCTYPE html>\n<html>\n\t<head>\n" + roboto_html + header
    slideshow_id_css = ""

    for i, el in enumerate(slideshow_ids):
        slideshow_id_css += f".{el}"
        if i < len(slideshow_ids)-1:
            slideshow_ids += ", "

    if slideshow_id_css:
        slideshow_id_css += " {display: none}\n"
    result += "\t\t<style>\n" + slideshow_id_css + body_css + css + "\n\t\t</style>\n"
    result += "\t</head>\n\t<body>" + html_code + footer_html.replace("\n", "\n\t\t") 
    
    if js_code:
        slideshow_id_js = ""
        if slideshow_ids:
            slideshow_id_js += f"let slideId = {str(slideshow_ids)}\n"
            slideshow_id_js += f"let slideIndex = ["
            slideshow_id_js += ", ".join(["1" for _ in range(len(slideshow_ids))])
            slideshow_id_js += "]\n"
            for i, el in enumerate(slideshow_ids):
                slideshow_id_js += f"showSlides(1, {i})\n"
        result += "\t\t<script>\n" + slideshow_id_js + js_code + "\n\t\t</script>\n"
    result += "\t</body>\n</html>"

    file = open(f"{BUILD_PATH}{file_name}.html", 'w+')
    file.write(result)
    file.close()


def generate_columns_string(ratio_str):
    ratios = ratio_str.split()
    columns = " ".join([f"{ratio}fr" if ratio != "_" else "1fr" for ratio in ratios])
    return columns


def decode(sup_element: Tag or str or list, tab: bool = True, addedClass: str = "", addedStyle:str = ""): # type: ignore
    global tab_count, header, css, js_code, id_count, code_higlighting, is_last_nl
    tempcode = ""

    if type(sup_element) == str:
        return sup_element

    if type(sup_element) == list:
        for element in sup_element:
            tempcode += decode(element)
        return tempcode

    if addedClass:
        if "class" in sup_element.params:
            sup_element.params["class"] += f" {addedClass}"
        else:
            sup_element.params["class"] = addedClass

    if addedStyle:
        if "style" in sup_element.params:
            sup_element.params["style"] += f"; {addedStyle}"
        else:
            sup_element.params["style"] = addedStyle

    # for and if param
    if "for" in sup_element.params:
        count: int = int(sup_element.params["for"])
        sup_element.params.pop("for")
        for i in range(count):
            tempcode += decode(sup_element)
        return tempcode

    ####################################
    ###### MAIN TAGS
    ####################################
    if sup_element.name == "head":
        for element in sup_element.value:
            header += decode(element)
        return ""


    elif sup_element.name == "favicon":
        if "src" not in sup_element.params:
            print("ERROR: Favicon needs a src")
        else:
            tempcode += tabs(tempcode) + f'<link rel="icon" type="image/x-icon" href="{sup_element.params["src"]}">'


    elif sup_element.name == "dropdown":
        tempcode += tabs(tempcode) + f'<div class="dropdown"{make_params(sup_element)}>'
        tempcode += tabs(tempcode, 1) + f'<button class="dropbtn" onclick="dorpdown_click()">{sup_element.params["text"]}</button>'
        tempcode += tabs(tempcode, 1) + f'<div class="dropdown-content">'
        tempcode += make_sub_tags(sup_element, 2)
        tempcode += tabs(tempcode, 1) + f'</div>'
        tempcode += tabs(tempcode) + f'</div>'
        if "dropdown_hover" not in used_elements:
            used_elements.append("dropdown_hover")


    elif sup_element.name == "backend":
        make_backend(sup_element)


    elif sup_element.name == "slideshow":
        if (sup_element.name not in used_elements) and (sup_element.name in known_elements):
            used_elements.append(sup_element.name)
        tempcode += tabs(tempcode) + f'<div class="slideshow-container"{make_params(sup_element)}>'
        tempcode += make_sub_tags(sup_element, 1, f"mySlides_{id_count}")
        slideshow_ids.append(f"mySlides_{id_count-1}")
        tempcode += tabs(tempcode) + f'\t<a class="prev" onclick="plusSlides(-1, {len(slideshow_ids)-1})">&#10094;</a>'
        tempcode += tabs(tempcode) + f'\t<a class="next" onclick="plusSlides(1, {len(slideshow_ids)-1})">&#10095;</a>'
        tempcode += tabs(tempcode) + f'</div>'
        id_count += 1


    elif sup_element.name in ["css", "style"]:
        if sup_element.params:
            tempcode += tabs(tempcode) + f'<style{make_params(sup_element)}>'
            if type(sup_element.value) == list:
                print("ERROR: css needs a text not a list")
                return ""
            tempcode += sup_element.value
            tempcode += tabs(tempcode) + f'</style>'
        else:
            css += sup_element.value


    elif sup_element.name in ["js", "script"]:
        if sup_element.params:
            tempcode += tabs(tempcode) + f'<script{make_params(sup_element)}>'
            if type(sup_element.value) == list:
                print("ERROR: js needs a text not a list")
                return ""
            tempcode += sup_element.value
            tempcode += tabs(tempcode) + f'</script>'
        else:
            js_code += sup_element.value


    elif sup_element.name == "parallax":
        if (sup_element.name not in used_elements) and (sup_element.name in known_elements):
            used_elements.append(sup_element.name)
        tempcode += tabs(tempcode) + f'<div class="parallax"{make_params(sup_element)}>'
        if sup_element.value:
            if "center" in known_elements:
                used_elements.append("center")
            tempcode += tabs(tempcode, 1) + f'<div class="center">'
            tempcode += make_sub_tags(sup_element, 2)
            tempcode += tabs(tempcode, 1) + f'</div>'
        else:
            tempcode += make_sub_tags(sup_element)
        tempcode += tabs(tempcode)+ f'</div>'


    elif sup_element.name == "code":
        if not code_higlighting:
            code_higlighting = True
            header += code_highlight_header
        if "language" not in sup_element.params:
            print("ERROR: Code needs a language")
            return ""
        tempcode += tabs(tempcode) + f'<pre><code class="language-{sup_element.params["language"]}">'
        tempcode += decode(sup_element.value)
        tempcode += tabs(tempcode) + f'</code></pre>'


    elif sup_element.name == "center":
        if (sup_element.name not in used_elements) and (sup_element.name in known_elements):
            used_elements.append(sup_element.name)
        temp = ""
        if "format" in sup_element.params:
            if sup_element.params["format"] == "both":
                temp = ""
            elif sup_element.params["format"] == "vertical":
                temp = " vertical"
                if "vertical" not in used_elements:
                    used_elements.append("vertical")
            elif sup_element.params["format"] == "horizontal":
                temp = " horizontal"
                if "horizontal" not in used_elements:
                    used_elements.append("horizontal")
            else:
                print("ERROR: center format must be both, vertical or horizontal")
                return ""
        tempcode += tabs(tempcode) + f'<div class="center{temp}"{make_params(sup_element)}>'
        tempcode += make_sub_tags(sup_element)
        tempcode += tabs(tempcode) + f'</div>'
        css += center_css


    elif sup_element.name == "fullscreen":
        if (sup_element.name not in used_elements) and (sup_element.name in known_elements):
            used_elements.append(sup_element.name)
        if "center" not in used_elements:
            used_elements.append("center")
        tempcode += tabs(tempcode) + f'<div class="fullscreen"{make_params(sup_element)}>'
        tempcode += tabs(tempcode, 1) + f'<div class="center">'
        tempcode += make_sub_tags(sup_element, 2)
        tempcode += tabs(tempcode, 1) + f'</div>'
        tempcode += tabs(tempcode) + f'</div>'
        css += fullscreen_css


    elif sup_element.name == "to_the_top":
        if not "button" in used_elements:
            used_elements.append("button")
        if not "to_the_top" in used_elements:
            used_elements.append("to_the_top")
        tempcode += tabs(tempcode) + f'<button class="to_the_top" onclick="to_the_top()"{make_params(sup_element)}>' + decode(
            sup_element.value) + '</button>'


    elif sup_element.name == "icon":
        if "value" in sup_element.params:
            tempcode += f'<i class="fa fa-{sup_element.params["value"]}"{make_params(sup_element)}></i>'
        else:
            print("ERROR: Icon needs a value")


    elif sup_element.name == "img":
        # <img resize="true" src="...">
        if "resize" in sup_element.params and sup_element.params["resize"] == "true":
            tempcode += tabs(tempcode) + f'<img class="modal-target"{make_params(sup_element)}>'
            if "img_modal" not in used_elements:
                used_elements.append("img_modal")
        else:
            tempcode += tabs(tempcode) + f'<img{make_params(sup_element)}>'


    elif sup_element.name == "load":
        if "src" not in sup_element.params:
            print("ERROR: Load needs a value")
            return ""
        file = open(sup_element.params["src"], 'r')
        tempcode += decode(file.read())
        file.close()


    elif sup_element.name == "split":
        if "split" not in used_elements:
            used_elements.append("split")
        tempcode += tabs(tempcode) + f'<div class="outer-container"{make_params(sup_element)}>'

        print("split: ",sup_element)
        tab_count += 1
        param = sup_element.params.get("format","horizontal")
        for element in sup_element.value:
            print(param, type(param))
            if param == "horizontal":
                temp = "width"
            elif param == "vertical":
                temp = "height"
            temp += f': {element.params.get("ratio", f"{int((100/len(sup_element.value)))}%")};'
            tempcode += decode(element, True, addedStyle=temp)
        tab_count -= 1


        tempcode += tabs(tempcode) + f'</div>\n'
        

    ####################################
    ###### ELSE TAGS
    ####################################
    else:
        if (sup_element.name not in used_elements) and (sup_element.name in known_elements):
            used_elements.append(sup_element.name)
        tempcode += tabs(tempcode) + f"<{sup_element.name}"
        if sup_element.params:
            for key, value in sup_element.params.items():
                tempcode += f' {key}="{value}"'
        tempcode += ">"

        # not a value: <p></p>
        if not sup_element.value:
            if sup_element.name in ONE_TAGS:
                return tempcode

        # Elements inside: <footer> <p>some Text</p> </footer>
        elif (len(sup_element.value) > 1) or (type(sup_element.value[0]) != str):
            tab_count += 1
            for element in sup_element.value:
                tempcode += decode(element, False)
            tab_count -= 1

            tempcode += tabs(tempcode) + f"</{sup_element.name}>"
            return tempcode

        # Text: <p>html</p>
        else:
            tempcode += sup_element.value[0]
        tempcode += f"</{sup_element.name}>"
    eval_nl(tempcode)
    return tempcode


####################################
###### BACKEND
####################################
def make_backend(sup_element: Tag):
    ...


####################################
###### HELPER FUNCTIONS
####################################

def make_sub_tags(sup_element: Tag, step=1, addedClass="", addedStyle=""):
    global id_count, tab_count
    temp_code = ""
    if (len(sup_element.value) == 1) and (type(sup_element.value[0]) == str):
        return sup_element.value[0]

    id_count += 1
    tab_count += step
    for element in sup_element.value:
        temp_code += decode(element, True, addedClass, addedStyle)
    tab_count -= step
    return temp_code


def make_str_value(sup_element):
    if len(sup_element.value) > 1:
        print(f"ERROR: The {sup_element} needs only a String but got {sup_element.value}")
        return ""
    if  type(sup_element.value[0]) != str:
        print(f"ERROR: The {sup_element} needs only a String but got {sup_element.value}! (2)")
        return ""
    return sup_element.value[0]


def make_params(sup_element: Tag):
    if not sup_element.params:
        return ""
    temp_code = " "

    for element in sup_element.params:
        temp_code += f'{element}="{sup_element.params[element]}" '
    return temp_code


def tabs(tempcode: str, steps: int = 0):
    global tab_count, is_last_nl
    tabs_str = ""
    if ((len(tempcode) > 1) and (tempcode[-1] != "\n")) or not is_last_nl:
        tabs_str += "\n"
    tabs_str += "\t" * (tab_count + steps)
    return tabs_str


def eval_nl(temp_code):
    global is_last_nl
    if len(temp_code) > 1 and temp_code[-1] == "\n":
        is_last_nl = True
    else:
        is_last_nl = False


####################################
###### RUN
####################################
if __name__ == "__main__":
    ast = generate_ast()
    print(ast)
    print("-------------")
    generate_html5(ast)
