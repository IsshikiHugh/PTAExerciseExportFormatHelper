import os
import sys
from bs4 import BeautifulSoup

def disabled_input_filter(tag):
    # <input ... disabled>
    return tag.name == "input" and tag.has_attr("disabled")

def result_class_div_filter(tag):
    # <div class="result" ...>
    type1:bool = tag.name == "div" and tag.has_attr("class") and ("result" in tag["class"] or "longField" in tag["class"])
    type2:bool = tag.name == "div" and tag.has_attr("style") and ("solid" in tag["style"])
    return type1 or type2

# Information desensitivity
def specific_div_filter(tag):
    if tag.name == "div" and tag.has_attr("class"):
        class_list = tag["class"]
        # Delete username and icon
        condition1 = " ".join(class_list) == "flex gap-x-4 relative"                         
        # Delete the left sidebar
        condition2 = " ".join(class_list) == "sb_KfyKY bg-bg-base transition-[left]"        
        # Delete states of answers for questions
        condition3 = " ".join(class_list) == "space-y-4 text-sm bg-bg-light p-4 rounded-lg"
        return condition1 or condition2 or condition3
    return False

def process(file):
    soup = BeautifulSoup(file, features="html.parser")
    
    # Options or blanks.
    options = soup.find_all(disabled_input_filter)
    for op in options:
        del op["disabled"]
        # Clear the options.
        if op.has_attr("checked"):
            del op["checked"]
        # Clear the filled blanks.
        if op.has_attr("value"):
            op["value"] = ""
    
    # Tips and codes.
    results = soup.find_all(result_class_div_filter)
    for res in results:
        res.decompose()
    
    # Remove specific div elements.
    specific_divs = soup.find_all(specific_div_filter)
    for div in specific_divs:
        div.decompose()
    
    return str(soup)

def save(data, file_path):
    file_path = file_path[:-5] + '_clean.html'
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(data)

if __name__ == "__main__":
    # Read in args.
    if len(sys.argv) != 2:
        print("Please using 'python format.py <path to xxx.html>'!")
        exit(0)
    file_path = sys.argv[1]
    print("Read file path: ", file_path)
    with open(file_path, encoding="utf-8") as file:
        data = process(file)
        save(data, file_path)