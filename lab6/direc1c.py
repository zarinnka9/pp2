import os

def list_all(path):
    
    all_items = os.listdir(path)
    return all_items

path = r'C:\\Users\\zorma\\Downloads\\Новая папка (4)\\lab6'
all_items = list_all(path)
print("All items (Directories and Files):", all_items)
