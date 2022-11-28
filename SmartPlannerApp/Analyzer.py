import os
import random

def analyzeData(stdInterest, generalElectives, cpscElectives, classList, database):

    scheduleDatabase = {}
    scheduledList = []

    #add copies of the original schedule by the amount of interest selected
    for x in range(len(stdInterest)):
        if stdInterest[x] != "None":
            classList.append(classList[0].copy())

    generalElectivesList = []
    generalElectivesWeight = []

    #takes the keys from generalElectives to create a list of the classes and their weights
    for key, value in generalElectives.items():
        generalElectivesList.append(key)
        generalElectivesWeight.append(float(generalElectives[key].get("weight")))

    cpscElectivesList = []
    cpscElectivesWeight = []

    #takes the keys from cpscElectives to create a list of the classes and their weights
    for key, value in cpscElectives.items():
        cpscElectivesList.append(key)
        cpscElectivesWeight.append(float(cpscElectives[key].get("weight")))
            
    credits = 0

    generalCreditsLimit = 6
    cpscCreditLimit = 9

    weight = 0.0
    scheduleWeights = [0.0]

    loop = True

    for x in range(len(classList)):

        #if the classList has only 1 schedule, the weight is set to 1 meaning it is high recommended
        if len(classList) == 1:
            scheduleWeights[x] = 1.0

        #avoids the first schedule since no changes need to be done to it, adds electives to the second schedule and so on
        if x > 0:
            i = 0
            credits = 0
            #adds cpsc electives which contains electives starting with CPSC and CYBR
            while loop:
                cpscElective = random.choices(cpscElectivesList, weights = cpscElectivesWeight, k=1)
                if cpscElective not in classList[x]:
                    credits += int(database[cpscElective[0]].get("Credits"))
                    if credits <= cpscCreditLimit:
                        classList[x].append(cpscElective[0])
                        weight += float(cpscElectives[cpscElective[0]].get("weight"))
                        i += 1
                    else:
                        break
            credits = 0
            #adds general electives which contains electives that the user has interest in
            while loop:
                generalElective = random.choices(generalElectivesList, weights = generalElectivesWeight, k=1)
                if generalElective not in classList[x]:
                    credits += int(database[generalElective[0]].get("Credits"))
                    if credits <= generalCreditsLimit:
                        classList[x].append(generalElective[0])
                        weight += float(generalElectives[generalElective[0]].get("weight"))
                        i += 1
                    else:
                        break
            weight = weight / i
            scheduleWeights.append(weight)

        Available = []
        Available = list(set(classList[x]))

        #sorts the schedule by their 4 digit number
        Available.sort(key = lambda x: int("".join([i for i in x if i.isdigit()])))

        Unavailable = []

        #creates a small database of classes that are in the schedules
        for i in range(len(classList[x])):
            scheduleDatabase[classList[x][i]] = {}
            scheduleDatabase[classList[x][i]]["Name"] = classList[x][i]

        #checks if the class is available in the database, if it isn't, it gets removed
        for key, value in scheduleDatabase.items():
            if key not in database:
                Unavailable.append(key)

        for i in range(len(Unavailable)):
            scheduleDatabase.pop(Unavailable[i])
            Available.remove(Unavailable[i])

        #gets the credits, time the class is available, the prerequisite, course description 
        for key, value in database.items():
            if scheduleDatabase.get(key) != None:
                scheduleDatabase[key] = value
            else:
                continue

        '''
        Temp = []
        Temp = Available
        for i in range(len(Temp)):
            if "000" in Temp[i]:
                Available.append(Temp[i])
                Available.remove(Temp[i])
        '''

        Temp = []
        Temp = Available

        #sorts the classes by prerequisites
        for i in range(len(Temp)):
            prereq = False
            if scheduleDatabase[Temp[i]].get("Prerequisite") != None:
                prereq = True
            if prereq == True:
                for key, value in scheduleDatabase[Temp[i]]["Prerequisite"].items():
                    if key in Available:
                        index1 = Available.index(Temp[i])
                        index2 = Available.index(key)
                        if index1 < index2:
                            Available.remove(Temp[i])
                            Available.insert(index2, Temp[i])
                        else:
                            continue
                    else:
                        continue
            else:
                continue

        scheduledList.append(Available)

    return scheduledList, scheduleDatabase, scheduleWeights