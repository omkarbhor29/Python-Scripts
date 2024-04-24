import os
import shutil
from datetime import datetime

# Define Source and destination path
source_path = ""
destination_path = ""

# Get Current date and time in format ddmmyyyyhhmmss
current_date = datetime.now().strftime('%d%m%Y%H%M%S')

# Check if source folder exists
if os.path.exists(source_path):
    # Check if destination folder exists
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Iterate through all files in source folder
    for filename in os.listdir(source_path):
        # create destination file path with current date time
        destination_file = os.path.join(destination_path,f"{os.path.splitext(filename)[0]}_{current_date}EDI{os.path.splitext(filename)[1]}")

        # Copy files to destination folder
        shutil.copy(os.path.join(source_path, filename), destination_file)

        print(f"Files copied Sucessfully from {source_path} to {destination_path}")
else:
    print(f"Source Folder does not exist")