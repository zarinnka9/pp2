import re
import os

def s_to_c(snake_str):
    words = snake_str.split('_') 
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case
filename = "row.txt"
if os.path.exists(filename):  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file: 
            line = line.strip()  
            print(f"before: {line}")
            print(f"after:  {s_to_c(line)}\n")
else:
    print(f"error: file '{filename}' not found!")
