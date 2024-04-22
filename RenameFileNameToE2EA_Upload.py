import os

folder_path = "D:\\Test"

# Iterate each file folder path
for file_name in os.listdir(folder_path):
    # Check if the file extension is 837
    if file_name.endswith(".837"):
        base_name, extension = os.path.splitext(file_name)
        # New File name
        new_file_name = f"{base_name}_E2EA{extension}"
        # New file path
        new_file_path = os.path.join(folder_path,new_file_name)
        os.rename(os.path.join(folder_path,file_name),new_file_path)
        print(f"File renamed:{new_file_name}")
