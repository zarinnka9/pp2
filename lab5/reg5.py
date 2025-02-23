import re
import os

def match(string):
    pattern = r'^a.*b$' 
    return "yes" if re.fullmatch(pattern, string) else "no"

filename = "row.txt"

if os.path.exists(filename):  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file: 
            line = line.strip()
            print(f"{line} -> {match(line)}")
else:
    print(f"error: file '{filename}' not found!")
