"""
# You're reading a config file that may or may not exist.
# The file contains a single number on the first line.
# Write a script that:
# 1. Tries to open "config.txt" and read the number
# 2. Handles the case where the file doesn't exist
# 3. Handles the case where the contents aren't a valid number
# 4. Uses finally to print "Done." regardless of what happened
# 5. If successful, print "Config value: <number>"

# Hint: the exception for a missing file is FileNotFoundError
# Hint: use int() to convert the string to a number



try:
    with open("config.txt", "r") as file:
        content = file.read()
        number = int(content)
        
except FileNotFoundError:
    print("File does not exist.")
    
except ValueError:
    print("Not a valid or existing number.")

else:
    print(f"Config value: {content}") 

finally:
    print("Done")
"""

import os 

"""
try:
    folder_name = input("Please input a folder name: ")
    files = os.listdir(folder_name)
except FileNotFoundError:
    print("That directory was not found.")
else:
    for file in files:
        print(file)
    """
"""
try:
    with open("server.log", "a") as file:
        file.write("SYSTEM CHECK: OK\n")
except PermissionError:
    print("Access Denied: Cannot write log.")
else:
    print("Log entry added successfully.")

"""
from pathlib import Path
import shutil

# Define source and destination directories
source_dir = Path("6-17-prac")
destination_dir = Path("D:\VSCODE\paytocum\6-17-prac\log_files")

# Ensure the destination folder exists before moving files
destination_dir.mkdir(parents=True, exist_ok=True)

# Loop through the files inside the source directory
for file_path in source_dir.iterdir():
    # Check if it's a file and matches the extensions
    if file_path.is_file() and (file_path.suffix == ".log" or file_path.suffix == ".txt"):
        # Move the file using its full path
        shutil.move(str(file_path), str(destination_dir))
        print(f"Moved: {file_path.name}")

    