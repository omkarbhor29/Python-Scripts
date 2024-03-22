import os
import re
import shutil

input_folder = r"D:\\Test\\834 File"
output_folder = r"D:\\Test\\processed"

obj_regex = re.compile(r'NM1\*IL\*1\*([^*]+)\*([^*]+)\*')

# Check If input folder exists
if not os.path.exists(input_folder):
    print("Input folder does not exist")
    exit()

# Check if the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder,filename)
    if os.path.isfile(file_path):
        with open(file_path,'r') as file:
            file_content = file.read()
            match = obj_regex.search(file_content)
            if match:
                str_first_name = match.group(1).replace("","")
                str_last_name = match.group(2).replace("","")
                str_new_name = str_first_name + str_last_name + os.path.splitext(filename)[1]

                print(f"Renamed file '{filename}' to '{str_new_name}'")
                new_file_path = os.path.join(output_folder, str_new_name)
                shutil.copy(file_path, new_file_path)

            else:
                print(f"No match found:{filename}")

print("File Renamed and moved Sucessfully")






