import os

import pandas as pd
input_file = "D:\\Test\\Sample"
excel_file = 'D:\\Test\\PolicyNo.xlsx'
df = pd.read_excel(excel_file)
# replacement_number = df.loc[0,'Policy No']
files = os.listdir(input_file)
for i,filename in enumerate(files):
    file_path = os.path.join(input_file,filename)

    policy_number = df.loc[i,'Policy No']
    # split the lines end with ~
    with open(file_path, 'r') as file:
        lines = file.read()
    multi_line = '\n'.join(lines.split('~'))
    with open(file_path, 'w') as file:
        file.writelines(multi_line)

    if os.path.isfile(file_path):
        with open(file_path,'r') as file:
            file_content = file.read()
            print(file_content)
            lines = file_content.splitlines()
            modified_line = []
            for line in lines:
                if line.startswith('ISA'):
                    parts = line.split('*')
                    if len(parts)>13:
                        parts[13] = policy_number
                        line = "*".join(str(parts) for parts in parts)
                    print("Policy no in ISA Segment replaced sucessfully")

                elif line.startswith('GS*HC'):
                    parts = line.split('*')
                    if len(parts) > 6:
                        parts[6] = policy_number
                        line = "*".join(str(parts) for parts in parts)
                    print("Policy no in GS Segment replaced sucessfully")

                elif line.startswith('GE*1'):
                    parts = line.split('*')
                    if len(parts) > 1:
                        parts[2] = policy_number
                        line = "*".join(str(parts) for parts in parts)
                    print("Policy no in GE Segment replaced sucessfully")

                elif line.startswith('IEA*1'):
                    parts = line.split('*')
                    if len(parts) > 1:
                        parts[2] = policy_number
                        line = "*".join(str(parts) for parts in parts)
                    print("Policy no in IEA Segment replaced sucessfully")

                modified_line.append(line)

            with open(file_path,'w') as file:
                file.write('\n'.join(modified_line))

    # After replacement add ~ at end of each line
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines_with_tilde = [line.rstrip('\n') + '~' for line in lines]
    with open(file_path, 'w') as file:
        file.writelines(lines_with_tilde)

    # convert multiple lines into single line
    with open(file_path, 'r') as file:
        lines = file.readlines()
    single_line = ' '.join(line.strip() for line in lines)
    with open(file_path, 'w') as file:
        file.writelines(single_line)
