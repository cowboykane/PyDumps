import os, shutil

os.makedirs("6-19-prac/python", exist_ok=True)

source = "6-19-prac/okay.py"
destination = "6-19-prac/python"

dest = shutil.copy(source, destination)

print(f"{source} copied to {destination}")