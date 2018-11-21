from openpyxl import load_workbook
wb = load_workbook(filename = '1.xlsx', data_only=True)
sheet_ranges = wb['Sheet1']
print ('hello')
#wb.get_sheet_by_name
#sheet_ranges
count=0;
for row in sheet_ranges.rows:
    for cell in row:
        if cell.column=='D' and cell.value != 'None':
            cell_address = 'E' + str(cell.row)
            print(cell_address)
            sheet_ranges[cell_address] = 'daffa'
        #print(cell.value)

wb.save(filename = '1.xlsx')