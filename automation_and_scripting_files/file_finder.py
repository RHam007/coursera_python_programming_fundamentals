import glob

path_raw = r"C:\target\file\path" # Path as taken from Windows File Explorer (Use 'r' to signify this is a "raw" string for Windows)
path_escaped = "C:\\\\target\\\\file\\\\path" # Exploded path (add 3 additional back-slashes "\" for each sub-folder tree change)

returned_files = glob.glob(path_raw + "/*.pdf") # Select ther desired file type(s)

for file_path in returned_files:
    print(file_path)

