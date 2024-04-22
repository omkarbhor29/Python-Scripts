import os
from datetime import datetime
import shutil

# Specify source and destination Folder
source_folder = r"D:\\Test\\834 File"
dest_folder = "D:\\Test\\834 Test Rename"

# Check if Source Folder Exist
if os.path.exists(source_folder):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Get Current TimeStamp
    current_timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Loop through each file in source folder
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)
        # check INDV pattern in filename
        if "_INDV_" in file_name:
            file_parts = file_name.split("_")
            if len(file_parts) >= 4:
                timestamp_part = file_parts[-2]
                if len(timestamp_part) == 12 and timestamp_part.isdigit():
                    new_timestamp = current_timestamp
                    new_file_name = file_name.replace(timestamp_part, new_timestamp)

                    print(f"Renamed File {file_name} to {new_file_name}")
                    new_file_path = os.path.join(dest_folder, new_file_name)
                    shutil.copy(file_path, new_file_path)

    print("Files rename completed")
else:
    print("Dest folder does not exist",dest_folder)