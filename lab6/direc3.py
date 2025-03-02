import os

def check_path(path):
    
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory = os.path.dirname(path)
        print(f"Directory portion: {directory}")
        
        filename = os.path.basename(path)
        print(f"Filename portion: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = r'C:\Users\zorma\Downloads\Новая папка (4)\lab6\direc3.py'  
check_path(path)
