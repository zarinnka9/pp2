import os

def delete_file(file_path):
    if os.path.exists(file_path):
        
        if os.access(file_path, os.W_OK):
            try:
            
                os.remove(file_path)
                print(f"File '{file_path}' has been deleted.")
            except OSError as e:
                print(f"Error: {e.strerror} - {e.filename}")
        else:
            print(f"Error: You do not have permission to delete the file '{file_path}'.")
    else:
        print(f"Error: The file '{file_path}' does not exist.")

file_path = r'C:\Users\zorma\Downloads\Новая папка (4)\lab6\A.txt' 
delete_file(file_path)
