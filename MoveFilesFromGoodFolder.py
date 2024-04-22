import os
import shutil

source_folder = "D:\\Test\\abc"
destination_folder = "D:\\Test\\xyz"

# Check if source folder Exist
if not os.path.exists(source_folder):
    print("Source Folder does not exist")
    exit()

# Check if destination folder Exist
if not os.path.exists(destination_folder):
    print("Destination Folder does not exist")
    exit()

found_files = []
# Iterate through each file in source folder
for file_name in os.listdir(source_folder):
    # Check if the file name ends with "_E2EA.837"
    if file_name.endswith("_E2EA.837"):
        found_files.append(file_name)

        source_Path = os.path.join(source_folder,file_name)
        dest_path = os.path.join(destination_folder,file_name)

        # Move the file to the destination folder
        shutil.move(source_Path,dest_path)
        print("All Files Moved Sucessfully")

if found_files:
    print("Found the following files to move:")
    for file_name in found_files:
        print(file_name)
else:
    print("No files ending with '_E2EA.837' found in source folder")