from heapq import merge
import xlsxwriter
import sys
import datetime

def compileData(InputList, InputDict):

    Schedules = []
    Schedules.append(InputList)

    today = datetime.date.today()
    credits = 0
    creditLimit = 15
    i = 4
    r = 2
    tempr = r
    year = today.year

    for x in range(len(Schedules)):
        workbook = xlsxwriter.Workbook(".\ExcelFiles\Path to Graduation " + str(x + 1) + ".xlsx")
        worksheet = workbook.add_worksheet("firstSheet")
        ptg_format = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 50})
        worksheet.write(0, 3, "Billy Bob")
        worksheet.write(0, 4, "909909909")
        worksheet.merge_range(1, 0, 1, 5, "Path To Graduation", ptg_format)
        for x in range(i):
            worksheet.write(r, 0, "Fall " + str(year))
            worksheet.write(r, 1, "Credits")
            worksheet.write(r, 2, "Spring " + str(year))
            worksheet.write(r, 3, "Credits")
            worksheet.write(r, 4, "Summer " + str(year))
            worksheet.write(r, 5, "Credits")
            r += 8
            worksheet.write(r, 0, "Total")
            worksheet.write_formula(r, 1, '=SUM(B' + str(r-6) + ':B' + str(r) + ')')
            worksheet.write(r, 2, "Total")
            worksheet.write_formula(r, 3, '=SUM(D' + str(r-6) + ':D' + str(r) + ')')
            worksheet.write(r, 4, "Total")
            worksheet.write_formula(r, 5, '=SUM(F' + str(r-6) + ':F' + str(r) + ')')
            r += 1
            year +=1

        worksheet.set_column(0, 2, 25)
        worksheet.set_column(0, 4, 25)
        worksheet.set_column('A:A', 25)
        worksheet.set_column('C:C', 25)
        worksheet.set_column('E:E', 25)

        credits = 0
        creditLimit = 15
        i = 4
        r = 2
        tempr = r
        year = 2022

        workbook.close()

    sys.exit()