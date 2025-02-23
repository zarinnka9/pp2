import re
import os
def insert_spaces(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)  
filename = "row.txt"
if os.path.exists(filename):  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file:  
            line = line.strip() 
            print(f"before: {line}")
            print(f"after:  {insert_spaces(line)}\n")
else:
    print(f"error: file '{filename}' not found!")
