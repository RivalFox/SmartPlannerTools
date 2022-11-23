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
CourseSemester = {}
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
        ScheduleDict.clear()
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

    keyList.clear()

    for key, value in ScheduleDict.items():
        keyList.append(key)

def addtoExcel(Fall, Spring, Summer, creditLimit, summerCreditLimit, CourseName, worksheet):

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

    if InputDict[CourseName].get("Prerequisite") != None:
        for key, value in InputDict[CourseName].get("Prerequisite").items():
            prereqList.append(key)

    while loop:
          
        x = 0
        
        for x in range(len(keyList)):
            if Fall == True and keyList[x][0:4] == "Fall":
                tempList.append(keyList[x])
            if Spring == True and keyList[x][0:4] == "Spri":
                tempList.append(keyList[x])
            if Summer == True and keyList[x][0:4] == "Summ":
                tempList.append(keyList[x])

        i = 0
    
        for i in range(len(tempList)):

            temp = tempList[i]

            if i > len(tempList) - 3:
                addSemesters(1, worksheet)
                tempList.clear()
                break

            for k in range(len(prereqList)):
                if prereqList[k] in addedList:
                    loop2 = True
                while loop2:
                    if ScheduleDict[temp]["Courses"].get(prereqList[k]) == None:
                        if i+l >= 0 and i+l < len(tempList):
                            temp = tempList[i+l]
                            l +=1
                        else:
                            loop2 = False
                            break
                    if l >= 0 and l < len(tempList):
                        temp = tempList[l]
                        loop2 = False
                    else:
                        loop2 = False 
                        break

            l = 1
            
            while CourseName[-3:] == "000":

                if ScheduleDict[temp]["Courses"].get(addedList[-1]) == None:
                    temp = tempList[i + l]
                    l += 1
                else:
                    temp = tempList[l-1]
                    break      
            
            s = ScheduleDict[temp].get("CreditStart")
            s = re.split('(\d+)', s)
            e = ScheduleDict[temp].get("CreditEnd")
            e = re.split('(\d+)', e)

            if ScheduleDict[temp]["Courses"].get(CourseName) == None:
                cell = s[0] + s[1]
                addCourses = True

            o = int(s[1])

            if s[0] == "B":
                b = "A"
                cell = b + s[1]
            elif s[0] == "D":
                b = "C"
                cell = b + s[1]
            elif s[0] == "F":
                b = "E"
                cell = b + s[1]

            while cell in cellList:
                o += 1
                cell = b + str(o)
                if o > int(e[1]):
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
                worksheet.write(s[0] + m[1], int(InputDict[CourseName].get("Credits")))
                CourseSemester[CourseName] = temp
                addedList.append(CourseName)
                cellList.append(cell)
                prereqList.clear()
                loop = False
                break
            else:
                continue