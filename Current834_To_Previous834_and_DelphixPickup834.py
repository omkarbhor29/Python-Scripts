import os
import shutil

source_dir = ""
destination_dir1 = ""
destination_dir2 = ""


src_files = os.listdir(source_dir)
for file_name in src_files:
    name = os.path.join(source_dir, file_name)
    if os.path.isfile(name):
        shutil.copy(name, destination_dir1)
        shutil.copy(name, destination_dir2)