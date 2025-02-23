import re
text = "row.txt" 
with open(text, 'r', encoding="utf-8") as file: 
    string = file.read().strip()
pattern = r'ab*'
result = re.findall(pattern, string)
if result:
    print(result)
else:print("Not found")