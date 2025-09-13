from openpyxl import Workbook
import random

wb = Workbook()

sheets = ['Energy','Production','Weather1','Weather2']
facilities = ['Facility A','Facility B','Facility C','Facility D']

for idx, sheet_name in enumerate(sheets):
    if idx == 0:
        ws = wb.active
        ws.title = sheet_name
    else:
        ws = wb.create_sheet(sheet_name)
    
    # Header
    ws.append(['Facility'] + [f'Month {i}' for i in range(1,25)])
    
    # Fill data
    for f in facilities:
        row = [f] + [round(random.uniform(10,100),2) for _ in range(24)]
        ws.append(row)

wb.save('EPRA_Sample.xlsx')
print("Sample Excel created: EPRA_Sample.xlsx")
