import re
import os

def split(string):
    return re.findall(r'[A-Z]?[a-z]+', string)  
filename = "row.txt"

if os.path.exists(filename):  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file:  
            line = line.strip() 
            print(f"before: {line}")
            print(f"after:  {split(line)}\n")
else:
    print(f"error: file '{filename}' not found!")
