import os # Module os Usage

if os.path.exists("sample.txt"):
    os.remove("sample.txt") # Remove Function Delete file
    print("File deleted successfully.")
else:
    print("File does not exist.")