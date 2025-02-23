import re
import os

def replace(string):
    pattern = r'[ ,.]' 
    return re.sub(pattern, ':', string) 

filename = "row.txt"

if os.path.exists(filename):  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file:
            line = line.strip()
            print(f"before: {line}")
            print(f"after:  {replace(line)}\n")
else:
    print(f"error: file '{filename}' not found!")
