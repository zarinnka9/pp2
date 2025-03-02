def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"The file at '{file_path}' does not exist.")
        return 0
    except IOError:
        print(f"An error occurred while reading the file '{file_path}'.")
        return 0

file_path = r'C:\Users\zorma\Downloads\Новая папка (4)\lab6\file.txt'  
line_count = count_lines(file_path)
print(f"Number of lines in the file: {line_count}")
