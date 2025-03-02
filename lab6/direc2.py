import os

def check_access(path):
    
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        
        if os.access(path, os.R_OK):
            print("The path is readable.")
        else:
            print("The path is not readable.")
        
        if os.access(path, os.W_OK):
            print("The path is writable.")
        else:
            print("The path is not writable.")
        
        if os.access(path, os.X_OK):
            print("The path is executable.")
        else:
            print("The path is not executable.")
    
    else:
        print(f"Path '{path}' does not exist.")

path = r'C:\Users\zorma\Downloads\Новая папка (4)\lab6'  
check_access(path)
