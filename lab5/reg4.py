import re
text = "row.txt"
with open(text, "r") as file:
    string = file.read().strip()
pattern = "[A-Z][a-z]"
result = re.findall(pattern, string)
if result:
    print(result)
else:
    print("Not found") 

