import openpyxl as oxl

wb = oxl.load_workbook('SBER.xlsx')
sheet = wb.sheetnames[0]
ws = wb.active
data = []
for i in ws.values:
    if i == 0:
        break
    else:
        data.append(i[1])
