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

addedCells = []
addedCourses = []
Schedule = {}

def compileData(scheduleList, courseDatabase, name, id, crHrs, scheduleWeights):
    global row, column, year

    #depending on the user choice, they are able to decide how many credits they prefer to have
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

    for x in range(len(scheduleList)):
        workbook = xlsxwriter.Workbook(".\ExcelFiles\Path to Graduation " + str(x + 1) + ".xlsx")
        weight = scheduleWeights[x] * 100
        roundedWeight = round(weight, 2)
        print("Path to Graduation " + str(x + 1) + " | Recommendation Rate: " + str(roundedWeight) + "%")
        worksheet = workbook.add_worksheet("Schedule")

        ptg_format = workbook.add_format({'bold': True, 'align': 'center', 'font_size': 50})

        worksheet.write(0, 2, name)
        worksheet.write(0, 4, id)
        worksheet.merge_range(1, 0, 1, 5, "Path To Graduation", ptg_format)
        
        row = 3
        column = 0

        #function to add semesters
        addSemesters(1, worksheet)
        
        for f in range(len(scheduleList[x])):
            Fall = courseDatabase[scheduleList[x][f]]["Semester"].get("Fall")
            Spring = courseDatabase[scheduleList[x][f]]["Semester"].get("Spring")
            Summer = courseDatabase[scheduleList[x][f]]["Semester"].get("Summer")

            if Fall == False and Spring == False and Summer == False:
                break

            addtoExcel(Fall, Spring, Summer, creditLimit, summerCreditLimit, scheduleList[x][f], worksheet, courseDatabase)

        '''
        for key1, value1 in Schedule.items():
            print(key1, ":", value1)
        print("-------------------------------------------------------")
        '''

        Schedule.clear()
        
        #formating the columns width
        worksheet.set_column(0, 2, 25)
        worksheet.set_column(0, 4, 25)  
        worksheet.set_column('A:A', 25)
        worksheet.set_column('C:C', 25)
        worksheet.set_column('E:E', 25)

        row = 3
        column = 0
        year = today.year
        addedCells.clear()
        addedCourses.clear()

        workbook.close()

    sys.exit()

def addSemesters(amount, worksheet):
    global row, column, year
    for y in range(amount):
        for z in range(len(Semesters)):

            worksheet.write(CourseCells[z] + str(row), Semesters[z] + " " + str(year))
            Semester = Semesters[z] + " " + str(year)

            Schedule[Semester] = {}
            Schedule[Semester]["SemesterRow"] = CourseCells[z] + str(row+1)
            Schedule[Semester]["SemesterColumn"] = CreditCells[z] + str(column+1)

            row += 8
            worksheet.write(CourseCells[z] + str(row), "Total")
            row -= 8

            column += 1

            worksheet.write(CreditCells[z] + str(row), "Credits")
            Schedule[Semester]["Credits"] = 0

            row += 8
            worksheet.write_formula(CreditCells[z] + str(row), '=SUM(' + CreditCells[z] + str(row-7) + ':' + CreditCells[z] + str(row-1) + ')')
            Schedule[Semester]["CreditStart"] = CreditCells[z] + str(row-7)
            Schedule[Semester]["CreditEnd"] = CreditCells[z] + str(row-1)

            Schedule[Semester]["Courses"] = {}
            row -= 8
            column += 1

        row += 9
        year +=1
        column = 0

    keyList.clear()

    for key, value in Schedule.items():
        keyList.append(key)

def addtoExcel(fall, spring, summer, creditLimit, summerCreditLimit, courseName, worksheet, courseDatabase):

    semesterList = []
    prereqCourses = []

    credits = 0

    loop = True
    loop2 = False

    addCourses = False
    addCredits = False
    addSemester = False
    fixCredits = False

    #gets the courses prerequisites
    if courseDatabase[courseName].get("Prerequisite") != None:
        for key, value in courseDatabase[courseName].get("Prerequisite").items():
            prereqCourses.append(key)

    while loop:
        
        #get the semesters the course is available
        for x in range(len(keyList)):
            if fall == True and keyList[x][0:4] == "Fall":
                semesterList.append(keyList[x])
            if spring == True and keyList[x][0:4] == "Spri":
                semesterList.append(keyList[x])
            if summer == True and keyList[x][0:4] == "Summ":
                semesterList.append(keyList[x])\
    
        for i in range(len(semesterList)):

            semester = semesterList[i]

            #add more semesters if there is not enough space to add courses
            if i > len(semesterList) - 3:
                addSemesters(1, worksheet)
                semesterList.clear()
                break

            l = 1

            #checks if a prerequisite is added to the schedule
            for k in range(len(prereqCourses)):
                if prereqCourses[k] in addedCourses:
                    loop2 = True
                while loop2:
                    if Schedule[semester]["Courses"].get(prereqCourses[k]) == None:
                        if i+l >= 0 and i+l < len(semesterList):
                            semester = semesterList[i+l]
                            l +=1
                        else:
                            loop2 = False
                            #break
                    elif l >= 0 and l < len(semesterList):
                        semester = semesterList[l]
                        loop2 = False
                        credits = int(Schedule[semester].get("Credits")) + int(courseDatabase[courseName].get("Credits"))
                        if credits > creditLimit:
                            fixCredits = True
                        elif credits <= creditLimit:
                            fixCredits = False
                    else:
                        loop2 = False 

            #if a semester after the course prerequisite is already full, go to the available semester
            while fixCredits:
                credits = int(Schedule[semester].get("Credits")) + int(courseDatabase[courseName].get("Credits"))
                if semester[0:4] == "Summ":
                    if credits <= summerCreditLimit:
                        semester = semesterList[l+1]
                        l += 1
                    else:
                        fixCredits = False
                if credits > creditLimit:
                    if l+1 >= 0 and l+1 < len(semesterList):
                        semester = semesterList[l+1]
                        l += 1
                    else:
                        fixCredits = False
                        addSemester = True
                elif credits <= creditLimit:
                    fixCredits = False

            #add more semesters if there is not enough space to add courses
            if addSemester == True:
                addSemesters(1, worksheet)
                semesterList.clear()
                addSemester = False
                break

            l = 1
            
            #get the first cell and last cell that courses can be added in
            CreditStart = Schedule[semester].get("CreditStart")
            splitCreditStart = re.split('(\d+)', CreditStart)
            CreditEnd = Schedule[semester].get("CreditEnd")
            splitCreditEnd = re.split('(\d+)', CreditEnd)

            #check if the course is not in the current semester
            if Schedule[semester]["Courses"].get(courseName) == None:
                cell = CreditStart[0] + CreditStart[1]
                addCourses = True

            #B, D, F is where the credits are added, A, C, E is where the course name gets added
            if splitCreditStart[0] == "B":
                column = "A"
                cell = column + splitCreditStart[1]
            elif splitCreditStart[0] == "D":
                column = "C"
                cell = column + splitCreditStart[1]
            elif splitCreditStart[0] == "F":
                column = "E"
                cell = column + splitCreditStart[1]

            row = int(splitCreditStart[1])

            #checks in the cell that is assigned to the course has been used, if it has, go to the next available cell
            while cell in addedCells:
                row += 1
                cell = column + str(row)
                if row > int(splitCreditEnd[1]):
                    addCourses = False
                    break

            #check if the semester is summ or not, afterwards checks if there is space to add the course into that semester based on their credits
            if semester[0:4] != "Summ":
                credits = int(Schedule[semester].get("Credits")) + int(courseDatabase[courseName].get("Credits"))
                addCredits = checkCreditLimit(credits, creditLimit)
            else:
                credits = int(Schedule[semester].get("Credits")) + int(courseDatabase[courseName].get("Credits"))
                addCredits = checkSummerCreditLimit(credits, summerCreditLimit)

            #if addCourses is true and addCredits is true, the course will be added to the semester
            if addCourses == True and addCredits == True:

                Schedule[semester]["Courses"][courseName] = cell
                worksheet.write(cell, courseName)

                Schedule[semester]["Credits"] = credits
                SplitCell = re.split('(\d+)', cell)
                worksheet.write(splitCreditStart[0] + SplitCell[1], int(courseDatabase[courseName].get("Credits")))

                #when a course gets added, it gets saved in addedCourses and its location gets added to addedCells
                addedCourses.append(courseName)
                addedCells.append(cell)

                loop = False
                break
            else:
                continue

def checkCreditLimit(credits, creditLimit):
    if credits <= creditLimit:
        return True
    else:
        return False

def checkSummerCreditLimit(credits, summerCreditLimit):
    if credits <= summerCreditLimit:
        return True
    else:
        return False