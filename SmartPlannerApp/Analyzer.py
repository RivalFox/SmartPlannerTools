import os

InputDict = {}
Schedule = []
ScheduleList = []
    
def analyzeData(Schedules, DatabaseDict):

    for x in range(len(Schedules)):
        InputDict[Schedules[x]] = {}
        InputDict[Schedules[x]]["Name"] = Schedules[x]

    InputDict["CPSC 1302"] = {}
    InputDict["CPSC 1302"]["Name"] = "CPSC 1302"
    InputDict["CPSC 1301K"] = {} 
    InputDict["CPSC 1301K"]["Name"] = "CPSC 1301K"
    InputDict["CPSC 2108"] = {}
    InputDict["CPSC 2108"]["Name"] = "CPSC 2108"
    InputDict["CPSC 4115"] = {}
    InputDict["CPSC 4115"]["Name"] = "CPSC 4115"
    InputDict["CPSC 4111"] = {}
    InputDict["CPSC 4111"]["Name"] = "CPSC 4111"
    InputDict["CPSC 6180"] = {}
    InputDict["CPSC 6180"]["Name"] = "CPSC 6180"
    InputDict["CPSC 6185"] = {}
    InputDict["CPSC 6185"]["Name"] = "CPSC 6185"
    InputDict["CPSC 6985"] = {}
    InputDict["CPSC 6985"]["Name"] = "CPSC 6985"
    InputDict["CYBR 2159"] = {}
    InputDict["CYBR 2159"]["Name"] = "CYBR 2159"
    InputDict["CYBR 2160"] = {}
    InputDict["CYBR 2160"]["Name"] = "CYBR 2160"
    InputDict["CYBR 3106"] = {}
    InputDict["CYBR 3106"]["Name"] = "CYBR 3106"
    InputDict["CYBR 3108"] = {}
    InputDict["CYBR 3108"]["Name"] = "CYBR 3108"
    InputDict["CYBR 3115"] = {}
    InputDict["CYBR 3115"]["Name"] = "CYBR 3115"
    InputDict["CYBR 3119"] = {}
    InputDict["CYBR 3119"]["Name"] = "CYBR 3119"

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

    ScheduleList.append(Schedule)

def getInputDict():
    return InputDict

def getScheduleList():
    return ScheduleList