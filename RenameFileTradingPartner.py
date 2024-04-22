import os
import re

input_folder = r"D:\\Test"
if not os.path.exists(input_folder):
    print("Input folder does not exist")
pattern = re.compile(r'NM1\*41\*\d\*[^*]+\*[^*]+\*([^*]+)~',re.IGNORECASE)

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder,filename)

    if os.path.isfile(file_path):
        with open(file_path,'r',encoding="utf-8") as file:
            file_content = file.read()
            lines = file_content.split("~")
            print(lines)
            for line in lines:
                if line.startswith('NM1*41*'):
                    match = pattern.match(line)
                    print(match)
                    if match:
                        segment_content = match.group(1)
                        new_name = f"{os.path.splitext(filename)[0]}_{segment_content}.{os.path.splitext(filename)[1]}"
                        new_file_path = os.path.join(input_folder,new_name)
                        if not os.path.exists(new_file_path):
                            os.rename(file_path,new_file_path)
                            print(f"File Renamed:{filename} to {new_name}")
                        else:
                            print(f"New Filename already exist:{new_name}")