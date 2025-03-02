import os

def list_files(path):
    files = [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]
    return files

path = r'C:\\Users\\zorma\\Downloads\\Новая папка (4)\\lab6'
files = list_files(path)
print("Files:", files)
