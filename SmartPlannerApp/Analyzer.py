import os
import random

def analyzeData(stdInterest, generalElectives, cpscElectives, classList, database):

    scheduleDatabase = {}
    scheduledList = []

    for x in range(len(stdInterest)):
        if stdInterest[x] != "None":
            classList.append(classList[0].copy())

    generalElectivesList = []
    generalElectivesWeight = []

    for key, value in generalElectives.items():
        generalElectivesList.append(key)
        generalElectivesWeight.append(float(generalElectives[key].get("weight")))

    cpscElectivesList = []
    cpscElectivesWeight = []

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

        if len(classList) == 1:
            scheduleWeights[x] = 1.0

        if x > 0:
            i = 0
            credits = 0
            while loop:
                cpscElective = random.choices(cpscElectivesList, weights = cpscElectivesWeight, k=1)
                if cpscElective not in classList[x]:
                    credits += int(database[cpscElective[0]].get("Credits"))
                    if credits <= cpscCreditLimit:
                        classList[x].append(cpscElective[0])
                        weight += float(cpscElectives[cpscElective[0]].get("weight"))
                        i += 1
                        #print("schedule #", x, " has added ", cpscElective[0])
                    else:
                        break
            credits = 0
            while loop:
                generalElective = random.choices(generalElectivesList, weights = generalElectivesWeight, k=1)
                if generalElective not in classList[x]:
                    credits += int(database[generalElective[0]].get("Credits"))
                    if credits <= generalCreditsLimit:
                        classList[x].append(generalElective[0])
                        weight += float(generalElectives[generalElective[0]].get("weight"))
                        i += 1
                        #print("schedule #", x, " has added ", generalElective[0])
                    else:
                        break
            weight = weight / i
            scheduleWeights.append(weight)

        Available = []
        Available = list(set(classList[x]))

        Available.sort(key = lambda x: int("".join([i for i in x if i.isdigit()])))

        Unavailable = []

        for i in range(len(classList[x])):
            scheduleDatabase[classList[x][i]] = {}
            scheduleDatabase[classList[x][i]]["Name"] = classList[x][i]

        for key, value in scheduleDatabase.items():
            if key not in database:
                Unavailable.append(key)

        for i in range(len(Unavailable)):
            scheduleDatabase.pop(Unavailable[i])
            Available.remove(Unavailable[i])

        for key, value in database.items():
            if scheduleDatabase.get(key) != None:
                scheduleDatabase[key] = value
            else:
                continue

        Temp = []
        Temp = Available

        for i in range(len(Temp)):
            if "000" in Temp[i]:
                Available.append(Temp[i])
                Available.remove(Temp[i])
        
        Temp = Available

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