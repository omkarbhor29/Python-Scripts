import ftplib
import os

# Fill Required Information
Hostname = ""
Username = ""
Password = ""

# Connect FTP Server
ftp_server = ftplib.FTP(Hostname, Username, Password)

# force UTF-8 encoding
ftp_server.encoding = "utf-8"

# Specify the folder containing the files
source_dir = r""
destination_dir = ""

# List all files in the folder
files = os.listdir(source_dir)

# Iterate through each file and upload to the FTP server
for filename in files:
    source_file = os.path.join(source_dir, filename)
    if os.path.isfile(source_file):
        with open(source_file, 'rb') as f:
            ftp_server.storbinary(f"STOR {filename}", f)

# Close the Connection
ftp_server.quit()

print("FTP transfer completed")