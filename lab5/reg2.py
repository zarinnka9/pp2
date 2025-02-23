import re
text = "row.txt"
with open(text, 'r') as file:
    string = file.read().strip()
pattern = r'ab[2-3]'
result = re.findall(pattern, string)
if result:
    print(result)
else:
    print("Not found") 


