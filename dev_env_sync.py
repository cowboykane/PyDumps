import os, shutil


# Task 1:
# TODO: print working directory, pick a file, use os.path.exists, find 
# absolute path of the file


print("Current directory:", os.getcwd())

file = os.path.exists("moreshutil.py")
print(file)

path = os.path.abspath("moreshutil.py")
print(path)

# Task 2:
# TODO: Check if sandbox/data_dump/ exists. If it Does not exist, 
# use os.makedirs to create it. Use os.listdir to print out the resulting list.

file = os.path.exists("sandbox/data_dump/")

if file is False:
    print("No directory exists. Creating directory now..")
    os.makedirs("sandbox/data_dump/")

print(os.listdir("sandbox"))

