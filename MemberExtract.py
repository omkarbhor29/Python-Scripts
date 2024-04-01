import pyodbc
import win32com.client

ssn_file_path = "D:\\Test\\EDI834.xlsx"
outputFilePath = "D:\\Test\\Mastersheet.xlsx"

# Connection to SQL Server
conn_str = (r"Driver={SQL Server};"
        r"Server=VEGATST;"
        r"Database=EBM;"
        r"Trusted_Connection=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Read Data from Specific columns in Excel file
excel = win32com.client.Dispatch("Excel.Application")
ssn_workbook = excel.Workbooks.Open(ssn_file_path)
ssn_sheet = ssn_workbook.Sheets("Sheet1")
last_name = ssn_sheet.Range("A1").Value.strip()
first_name = ssn_sheet.Range("B1").Value.strip()
ssn = ssn_sheet.Range("C1").Value.strip()
ssn_workbook.Close(False)

Sql_query = f"""
SELECT MD.LastName + MD.FirstName + '.EDI' As FirstNameLastNameEDI, MI.MEMBERNUMBER
        FROM [EBM].[Member].[Identity] MI
        JOIN [EBM].[Member].[BenefitCoverage] BC ON MI.IdentityKey = BC.IdentityKey
        JOIN [EBM].[Member].[Demographic] MD ON MI.IdentityKey = MD.IdentityKey
        WHERE LineOfBusiness = 'CCA' AND ConfirmationIndicator = 'y'
        AND MD.LastName IN ('{last_name}')
        AND MD.FirstName IN ('{first_name}')
        AND MI.SSN IN ('{ssn}')
        ORDER BY BC.BenefitCoveragesLastUpdatedAt DESC

"""

# Execute SQL Query
cursor.execute(Sql_query)

# Create new Excel Workbook
output_workbook = excel.Workbooks.Open(outputFilePath)
output_sheet = output_workbook.Sheets(1)

# Write Column header to excel sheet
output_sheet.Cells(1,1).Value = "MEMBERNUMBER"
output_sheet.Cells(1,2).Value = "FirstNameLastNameEDI"

# Looping through all row
row_number = 2
for row in cursor:
        output_sheet.Cells(row_number, 1).Value = row.FirstNameLastNameEDI
        output_sheet.Cells(row_number, 2).Value = row.MEMBERNUMBER
        row_number += 1

# Save Excel Workbook and close
output_workbook.Save()
output_workbook.Close()

# Quit Excel
excel.quit()

# Close Cursor and connection
cursor.close()
conn.close()




