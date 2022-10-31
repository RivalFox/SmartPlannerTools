InputDict = {}
Schedule = []
    
def analyzeData(path, filename, database):
    global InputDict, Schedule
    # Open and Read File
    inputFile = open(path + "\\" + filename)
    DatabaseDict = database
    InputDict = {}
    #classList = []
    phrase = "Needed"
    #count = 0
    for line in inputFile:
        #Finds the line that contains the phrase "Needed"
        if line.find(phrase) != -1: 
            #Once found, moves onto the next line
            nextLine = next(inputFile)
            for word in nextLine.split():

                if word.isupper() and len(word) == 4:
                    #print(word)

                    for num in nextLine.split():
                        if num[0].isdigit() and len(num) > 3:
                         #print(word + " " + num[:4])
                         #classList.append(word + " " + num[:4])
                         className = word + " " + num[:4]

                         InputDict[className] = {}
                         InputDict[className]["Name"] = className
                         #Dictionary[word + " " + num[:4]]["Name"] = {}

    for key, value in DatabaseDict.items():
        t = InputDict.get(key)
        if t != None:
            InputDict[key] = value
        else:
            continue

    Temp = []
    for key, value in InputDict.items():
        if InputDict[key].get("Credits") == None:
            Temp.append(key)
        else:
            continue

    for i in range(len(Temp)):
        InputDict.pop(Temp[i])

    Schedule = []
    InputList = []
    for key, value in InputDict.items():
        InputList.append(InputDict.get(key).get("Name"))
        Schedule.append(InputDict.get(key).get("Name"))

    Schedule.sort(key = lambda x: int("".join([i for i in x if i.isdigit()])))

    for x in range(len(InputList)):
        if InputDict[InputList[x]].get("Prerequisite") == None:
            continue
        else:
            for key, value in InputDict[InputList[x]]["Prerequisite"].items():
                if key in Schedule:
                    index = Schedule.index(key)
                    Schedule.remove(InputList[x])
                    Schedule.insert(index+1, InputList[x])

    for x in range(len(Schedule)):
        if "000" in InputList[x]:
            Schedule.append(InputList[x])
            Schedule.remove(InputList[x])

def getInputDict():
    return InputDict

def getScheduleList():
    return Schedule