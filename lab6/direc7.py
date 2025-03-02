import shutil

def copy_file(source_file, destination_file):
    try:
        
        shutil.copy(source_file, destination_file)
        print(f"Contents of '{source_file}' copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
    except IOError:
        print(f"Error: There was an issue copying from '{source_file}' to '{destination_file}'.")

source_file = r'C:\path\to\source\file.txt'  
destination_file = r'C:\path\to\destination\file.txt' 

copy_file(source_file, destination_file)
