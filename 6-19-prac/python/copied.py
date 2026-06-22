import os
import shutil
import time

source = "6-19-prac/okay.py"

# 1. Copy using copy()
dest_copy = shutil.copy(source, "6-19-prac/python/copied.py")

# 2. Copy using copy2()
dest_copy2 = shutil.copy2(source, "6-19-prac/python/copied2.py")

# Check the modification times
print("Original time:", os.path.getmtime(source))
print("copy() time:  ", os.path.getmtime(dest_copy))   # Will show right now
print("copy2() time: ", os.path.getmtime(dest_copy2))  # Will match the original
