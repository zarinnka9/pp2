import os

def list_directories(path):
    
    directories = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
    return directories

path = r'C:\\Users\\zorma\\Downloads\\Новая папка (4)\\lab6'
directories = list_directories(path)
print("Directories:", directories)
