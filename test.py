import xlsxwriter
import xlrd
import time

    
path = "food_10.xls"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

outWorkbook = xlsxwriter.Workbook("Test1.xlsx")
outSheet = outWorkbook.add_worksheet()

spalten = inputWorksheet.ncols
zeilen = inputWorksheet.nrows

print(spalten)
print(zeilen)   
h = []
for x in range(100):
    mänge = inputWorksheet.cell_value(x, 10)
    if len(mänge) > 0: 
        print(mänge)
    else: 
        print("Nix")
    x += 1
