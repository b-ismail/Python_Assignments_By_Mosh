import openpyxl as xl

xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']

cell = sheet['a1']
#  OR
cell = sheet.cell(1, 1)
print(cell.value)