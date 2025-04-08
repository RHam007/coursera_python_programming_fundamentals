def read_file_contents(file_path, mode = 'r'):
    """
    Function to open a user defined path/file, read the content, and display the results.

    "with open()" closes the file as part of the open/read process

    Variables:
      - file path = user defined path and file to be opened
      - mode = operation mode (default: 'r')
      - contents = str of file content
    
    Exception(s)
    FileNotFound: will print error with file_path >>>  Error: File not found - /Users/Example/Documents/my_file.txt

    Example Input:
    read_file_contents("/Users/Example/Documents/my_file.txt")

    """
    try:
        with open(file_path,mode) as file:
            if mode == 'r':
                contents = file.read()
                print(contents)
        
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")

read_file_contents("/Users/Example/Documents/my_file.txt")