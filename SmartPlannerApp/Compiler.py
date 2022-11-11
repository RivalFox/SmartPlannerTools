from heapq import merge
import xlsxwriter
import sys
import datetime
import re

addedList = []
InputDict = {}
ScheduleDict = {}
Schedules = []
keyList = []
creditLimit = 0
cell = ""
cellList = []


def compileData(InputList, InputDict1):
    global InputDict, ScheduleDict, Schedules, keyList, creditLimit
    Schedules.append(InputList)

    InputDict = InputDict1

    tempList = []

    Semesters = ["Fall", "Spring", "Summer"]
    CourseCells = ["A", "C", "E"]
    CreditCells = ["B", "D", "F"]

    today = datetime.date.today()
    year = today.year

    credits = 0
    creditLimit = 15

    i = 4

    Fall = False
    Spring = False
    Summer = False
    Check = False
    Loop = True

    for x in range(len(Schedules)):
        workbook = xlsxwriter.Workbook(".\ExcelFiles\Path to Graduation " + str(x + 1) + ".xlsx")
        worksheet = workbook.add_worksheet("Schedule")

        ptg_format = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 50})

        worksheet.write(0, 3, "Billy Bob")
        worksheet.write(0, 4, "909909909")
        worksheet.merge_range(1, 0, 1, 5, "Path To Graduation", ptg_format)

        r = 3

        for y in range(i):
            c = 0
            for z in range(len(Semesters)):

                worksheet.write(CourseCells[z] + str(r), Semesters[z] + " " + str(year))
                Semester = Semesters[z] + " " + str(year)

                ScheduleDict[Semester] = {}
                ScheduleDict[Semester]["SemesterRow"] = CourseCells[z] + str(r+1)
                ScheduleDict[Semester]["SemesterColumn"] = CreditCells[z] + str(c+1)

                r += 8
                worksheet.write(CourseCells[z] + str(r), "Total")
                r -= 8

                c += 1

                worksheet.write(CreditCells[z] + str(r), "Credits")
                ScheduleDict[Semester]["Credits"] = 0

                r += 8
                worksheet.write_formula(CreditCells[z] + str(r), '=SUM(' + CreditCells[z] + str(r-7) + ':' + CreditCells[z] + str(r-1) + ')')
                ScheduleDict[Semester]["CreditStart"] = CreditCells[z] + str(r-7)
                ScheduleDict[Semester]["CreditEnd"] = CreditCells[z] + str(r-1)

                ScheduleDict[Semester]["Courses"] = {}
                #for o in range(r-7, r):
                #    ScheduleDict[Semester]["Courses"][CreditCells[z] + str(o)] = None
                r -= 8
                c += 1

            r += 9
            year +=1
            c = 0

        for key, value in ScheduleDict.items():
            keyList.append(key)

        print("-----------------------")
        for f in range(len(Schedules[x])):
            Fall = InputDict[Schedules[x][f]]["Semester"].get("Fall")
            Spring = InputDict[Schedules[x][f]]["Semester"].get("Spring")
            Summer = InputDict[Schedules[x][f]]["Semester"].get("Summer")

            addtoExcel(Fall, Spring, Summer, Schedules[x][f], worksheet)
        print("------------------------")

        for key1, value1 in ScheduleDict.items():
            print(key1, ":", value1)

        worksheet.set_column(0, 2, 25)
        worksheet.set_column(0, 4, 25)  
        worksheet.set_column('A:A', 25)
        worksheet.set_column('C:C', 25)
        worksheet.set_column('E:E', 25)

        r = 2
        t = 0
        year = today.year

        workbook.close()

    sys.exit()

def addtoExcel(Fall, Spring, Summer, CourseName, worksheet):
    global addedList, cell
    tempList = []
    credits = 0
    forloop = True
    prereqList = []
    b = ""
    o = ""
    temp = ""
    Loop2 = False
    l = 1

    addCourses = False
    addCredits = False

    for x in range(len(keyList)):
        if Fall == True and keyList[x][0:4] == "Fall":
            tempList.append(keyList[x])
        if Spring == True and keyList[x][0:4] == "Spri":
            tempList.append(keyList[x])
        if Summer == True and keyList[x][0:4] == "Summ":
            tempList.append(keyList[x])
    
    for i in range(len(tempList)):
        if forloop == False:
            break
        
        temp = tempList[i]

        if InputDict[CourseName].get("Prerequisite") != None:
            for key, value in InputDict[CourseName].get("Prerequisite").items():
                prereqList.append(key)

        s = ScheduleDict[temp].get("CreditStart")
        s = re.split('(\d+)', s)
        e = ScheduleDict[temp].get("CreditEnd")
        e = re.split('(\d+)', e)
        
        if ScheduleDict[temp]["Courses"].get(CourseName) == None:
            cell = s[0] + s[1]
            addCourses = True

        for k in range(len(prereqList)):
            if prereqList[k] in addedList:
                Loop2 = True
            while Loop2:
                if ScheduleDict[temp]["Courses"].get(prereqList[k]) == None:
                    temp = tempList[i+l]
                    l +=1
                else:
                    temp = tempList[l]
                    Loop2 = False

        s = ScheduleDict[temp].get("CreditStart")
        s = re.split('(\d+)', s)
        e = ScheduleDict[temp].get("CreditEnd")
        e = re.split('(\d+)', e)

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

        if addCourses == True and addCredits == True:
            ScheduleDict[temp]["Courses"][CourseName] = cell
            worksheet.write(cell, CourseName)
            ScheduleDict[temp]["Credits"] = credits
            m = re.split('(\d+)', cell)
            worksheet.write(s[0] + m[1], int(InputDict[CourseName].get("Credits")))
            addedList.append(CourseName)
            cellList.append(cell)
            print(CourseName)
            print(prereqList)
            break
        else:
            continue