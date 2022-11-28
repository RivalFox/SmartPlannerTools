import os

def analyzeData(stdInterest, generalElectives, cpscElectives, classList, database):

    scheduleDatabase = {}
    scheduledList = []

    for x in range(3):
        classList.append(classList[0])

    l = 0

    for x in range(len(classList)):

        if x > 0:
            classList[x].extend(cpscElectives)
            for key, value in generalElectives.items():
                if l >= 0 and l < len(stdInterest):
                    if stdInterest[l] == key[0:4]:
                        print(key)
                        print(classList[x])
                        classList[x].append(key)
                else:
                    break
            l += 1

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

    return scheduledList, scheduleDatabase