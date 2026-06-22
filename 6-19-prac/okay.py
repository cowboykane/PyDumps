import os, shutil

import os
import shutil

# 1. Setup a dummy folder structure to archive
source_dir = "6-19-prac/my_project"
os.makedirs(f"{source_dir}/code", exist_ok=True)

with open(f"{source_dir}/notes.txt", "w") as f:
    f.write("Important notes.")
with open(f"{source_dir}/code/app.py", "w") as f:
    f.write("# App logic")

# 2. ZIP THE FOLDER (Compression)
# This creates a file named 'project_backup.zip' in the '6-19-prac' folder
archive_path = "6-19-prac/project_backup"
shutil.make_archive(base_name=archive_path, format="zip", root_dir=source_dir)
print(f"Archive created: {archive_path}.zip")

# 3. UNPACK THE ZIP (Decompression)
# This extracts 'project_backup.zip' into a brand new folder
extract_to_dir = "6-19-prac/extracted_project"
shutil.unpack_archive(filename=f"{archive_path}.zip", extract_dir=extract_to_dir)
print(f"Archive unpacked to: {extract_to_dir}")
