import re
import pandas as pd
import os

# Load Exel file
excel_file = "D:\\Test\\Claims_Mastersheet.xlsx"
df = pd.read_excel(excel_file)

# Folder Containing 837 file
directory = "D:\\Test\\Current 837"
files_in_folder = os.listdir(directory)

# Function to extract member ID from file
def extract_member_id(line):
    match = re.search(r'NM1\*IL\*1\*.*?(\d{10}|0\d{9})~',line)
    if match:
        return match.group(1)
    else:
        return None

# Iterate through each row in excel and extract member Id
for index,row in df.iterrows():
    file_name = row["837 File Name"]
    if file_name in files_in_folder:
        df.loc[index, 'File Exist'] = "Yes"
    else:
        df.loc[index, 'File Exist'] = "No"
    file_path = os.path.join(directory,file_name)
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            lines = file.readlines()
            for line in lines:
                extract_number = extract_member_id(line)
                if extract_number:
                    df.loc[index,'Member ID'] = extract_number


# Save member ID in current Sheet
outputfile = "D:\\Test\\Claims_Mastersheet.xlsx"
df.to_excel(outputfile,index=False)