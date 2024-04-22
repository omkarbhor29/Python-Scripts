import os
import shutil

input_folder = ""
rlh_folder = ""
ssi_folder = ""

# Check input folder exist or not
if not os.path.exists(input_folder):
    print("Input folder does not exist")

# Create Destination Folder
for folder in [rlh_folder,ssi_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Process Files
for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder,filename)
    if os.path.isfile(file_path):
        with open(file_path,'r') as file:
            file_content = file.read()

        # Check if Filename Contains RLH or SSI
        if "_RLH_" in filename:
            # Copy File to RLH Folder
            shutil.copy(file_path,os.path.join(rlh_folder,filename))
            print(f"File copied to RLH folder:{filename}")
        elif "_SSI_" in filename:
            # Copy File to SSI Folder
            shutil.copy(file_path, os.path.join(ssi_folder, filename))
            print(f"File copied to SSI folder:{filename}")

print("Files Copied Sucessfully")
            