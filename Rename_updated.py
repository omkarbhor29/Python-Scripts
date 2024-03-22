import os
import re
import shutil

Source_folder = r"D:\\Test\\834 File"

obj_regex = re.compile(r'NM1\*IL\*1\*([^*]+)\*([^*]+)\*')

# Create renamed folder in source folder to store all renamed files
renamed_folder = os.path.join(Source_folder,'renamed files')
os.makedirs(renamed_folder,exist_ok=True)

# Check If input folder exists
if not os.path.exists(Source_folder):
    print("Input folder does not exist")
    exit()

for filename in os.listdir(Source_folder):
    Old_file_path = os.path.join(Source_folder,filename)
    if os.path.isfile(Old_file_path):
        with open(Old_file_path,'r') as file:
            file_content = file.read()
            match = obj_regex.search(file_content)
            if match:
                str_first_name = match.group(1).replace("","")
                str_last_name = match.group(2).replace("","")
                str_new_name = str_first_name + str_last_name + os.path.splitext(filename)[1]

                new_filepath = os.path.join(renamed_folder,str_new_name)
                shutil.copy(Old_file_path,new_filepath)
                print(f"Renamed file '{filename}' to '{str_new_name}'")
            else:
                print(f"No match found:{filename}")

# Remove all files from source folder
for filename in os.listdir(Source_folder):
    file_path = os.path.join(Source_folder,filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

# move all files from renamed folder to source folder
for filename in os.listdir(renamed_folder):
    Old_file_path = os.path.join(renamed_folder,filename)
    new_filepath = os.path.join(Source_folder,filename)
    shutil.copy(Old_file_path,new_filepath)

# Removed all files from Renamed Folder
for filename in os.listdir(renamed_folder):
    file_Path = os.path.join(renamed_folder,filename)
    if os.path.isfile(file_Path):
        os.remove(file_Path)

# Removed Renamed folder
os.rmdir(renamed_folder)

print("File Renamed Sucessfully")






