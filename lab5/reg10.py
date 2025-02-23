
import re
import os
def camel_to_snake(camel_str):
    snake_case = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
    if snake_case.startswith('_'):
        snake_case = snake_case[1:] 
    return snake_case
filename = "row.txt"

if os.path.exists(filename):  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file:  
            line = line.strip() 
            print(f"before: {line}")
            print(f"after:  {camel_to_snake(line)}\n")
else:
    print(f"error: file '{filename}' not found!")
