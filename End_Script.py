import pandas as pd

file1 = "D:\\Test\\RLH.xlsx"
df1 = pd.read_excel(file1)

file2 = "D:\\Test\\SSI.xlsx"
df2 = pd.read_excel(file2)

combined_data = pd.concat([df1,df2],ignore_index=True)

output_file = "D:\\Test\\Merge.xlsx"
combined_data.to_excel(output_file,index=False)

print("Completed")
