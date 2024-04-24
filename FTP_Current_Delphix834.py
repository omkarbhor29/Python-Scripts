import os
import shutil

# Source folder
source_path = ""
# Remote Server path
destination_path = ""

# Network credentials for destination path
username = ""
password = ""

# Check is source folder exist
if os.path.exists(source_path):
    # Iterate through all files in source folder
    for filename in os.listdir(source_path):
        destination_file = os.path.join(destination_path,os.path.basename(filename))

        # Copy files to dest folder
        shutil.copy(os.path.join(source_path,filename),destination_file)

    print(f"Files copied sucessfully from {source_path} to {destination_path}")
else:
    print(f"Source Folder does not exist")
