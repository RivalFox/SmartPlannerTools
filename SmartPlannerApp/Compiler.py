import xlsxwriter
import sys
import datetime
import re


Semesters = ["Fall", "Spring", "Summer"]
CourseCells = ["A", "C", "E"]
CreditCells = ["B", "D", "F"]

row = 3
column = 0
today = datetime.date.today()
year = today.year

keyList = []

cellList = []
addedList = []
ScheduleDict = {}
Schedules = []
InputDict = {}

def compileData(InputList, InputDict1, name, id, crHrs):
    global InputDict, ScheduleDict, row, column, year

    InputDict = InputDict1

    Schedules = InputList

    if crHrs == "Full-time":
        creditLimit = 15
        summerCreditLimit = 9
    if crHrs == "Three quarter-time":
        creditLimit = 12
        summerCreditLimit = 6
    if crHrs == "Half-time":
        creditLimit = 9
        summerCreditLimit = 6
    if crHrs == "Less than half-time":
        creditLimit = 6
        summerCreditLimit = 3

    for x in range(len(Schedules)):
        workbook = xlsxwriter.Workbook(".\ExcelFiles\Path to Graduation " + str(x + 1) + ".xlsx")
        worksheet = workbook.add_worksheet("Schedule")

        ptg_format = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 50})

        worksheet.write(0, 2, name)
        worksheet.write(0, 4, id)
        worksheet.merge_range(1, 0, 1, 5, "Path To Graduation", ptg_format)

        row = 3
        column = 0

        addSemesters(1, worksheet)

        for f in range(len(Schedules[x])):
            Fall = InputDict[Schedules[x][f]]["Semester"].get("Fall")
            Spring = InputDict[Schedules[x][f]]["Semester"].get("Spring")
            Summer = InputDict[Schedules[x][f]]["Semester"].get("Summer")

            if Fall == False and Spring == False and Summer == False:
                break
            addtoExcel(Fall, Spring, Summer, creditLimit, summerCreditLimit, Schedules[x][f], worksheet)

        
        for key1, value1 in ScheduleDict.items():
            print(key1, ":", value1)
        print("-------------------------------------------------------")
        

        worksheet.set_column(0, 2, 25)
        worksheet.set_column(0, 4, 25)  
        worksheet.set_column('A:A', 25)
        worksheet.set_column('C:C', 25)
        worksheet.set_column('E:E', 25)

        row = 3
        column = 0
        year = today.year
        cellList.clear()
        addedList.clear()

        workbook.close()

    sys.exit()

def addSemesters(years, worksheet):
    global row, column, year
    for y in range(years):
        for z in range(len(Semesters)):

            worksheet.write(CourseCells[z] + str(row), Semesters[z] + " " + str(year))
            Semester = Semesters[z] + " " + str(year)

            ScheduleDict[Semester] = {}
            ScheduleDict[Semester]["SemesterRow"] = CourseCells[z] + str(row+1)
            ScheduleDict[Semester]["SemesterColumn"] = CreditCells[z] + str(column+1)

            row += 8
            worksheet.write(CourseCells[z] + str(row), "Total")
            row -= 8

            column += 1

            worksheet.write(CreditCells[z] + str(row), "Credits")
            ScheduleDict[Semester]["Credits"] = 0

            row += 8
            worksheet.write_formula(CreditCells[z] + str(row), '=SUM(' + CreditCells[z] + str(row-7) + ':' + CreditCells[z] + str(row-1) + ')')
            ScheduleDict[Semester]["CreditStart"] = CreditCells[z] + str(row-7)
            ScheduleDict[Semester]["CreditEnd"] = CreditCells[z] + str(row-1)

            ScheduleDict[Semester]["Courses"] = {}
            row -= 8
            column += 1

        row += 9
        year +=1
        column = 0

    for key, value in ScheduleDict.items():
        keyList.append(key)

def addtoExcel(Fall, Spring, Summer, creditLimit, summerCreditLimit, CourseName, worksheet):

    print(CourseName)
    tempList = []
    prereqList = []
    credits = 0

    loop = True
    loop2 = False

    b = ""
    o = ""
    temp = ""
    l = 1

    addCourses = False
    addCredits = False
    addSemester = False
    lastSemester = False

    if InputDict[CourseName].get("Prerequisite") != None:
        for key, value in InputDict[CourseName].get("Prerequisite").items():
            prereqList.append(key)

    while loop:

        for i in range(len(keyList)):
            if Fall == True and keyList[i][0:4] == "Fall":
                tempList.append(keyList[i])
            if Spring == True and keyList[i][0:4] == "Spri":
                tempList.append(keyList[i])
            if Summer == True and keyList[i][0:4] == "Summ":
                tempList.append(keyList[i])


        for i in range(len(tempList)):
            
            temp = tempList[i]

            cs = ScheduleDict[temp].get("CreditStart")
            cs = re.split('(\d+)', cs)
            ce = ScheduleDict[temp].get("CreditEnd")
            ce = re.split('(\d+)', ce)

            if ScheduleDict[temp]["Courses"].get(CourseName) == None:
                cell = cs[0] + cs[1]
                addCourses = True

            o = int(cs[1])

            if cs[0] == "B":
                b = "A"
                cell = b + cs[1]
            elif cs[0] == "D":
                b = "C"
                cell = b + cs[1]
            elif cs[0] == "F":
                b = "E"
                cell = b + cs[1]

            while cell in cellList:
                o += 1
                cell = b + str(o)
                if o > int(ce[1]):
                    addCourses = False
                    break

            credits = int(ScheduleDict[temp].get("Credits"))
            credits = credits + int(InputDict[CourseName].get("Credits"))

            if credits <= creditLimit:
                addCredits = True

            if temp[0:4] == "Summ":
                if credits <= summerCreditLimit:
                    addCredits = True
                else:
                    addCredits = False

            if addCourses == True and addCredits == True:
                ScheduleDict[temp]["Courses"][CourseName] = cell
                worksheet.write(cell, CourseName)
                ScheduleDict[temp]["Credits"] = credits
                m = re.split('(\d+)', cell)
                worksheet.write(cs[0] + m[1], int(InputDict[CourseName].get("Credits")))
                addedList.append(CourseName)
                cellList.append(cell)
                loop = False
                break
            else:
                continue