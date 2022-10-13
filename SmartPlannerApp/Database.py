import os

DatabaseDict = {}

def setDatabase(path, filename):
    global DatabaseDict
    x = open(os.path.join(path,filename), "r", encoding = 'utf-8')
    for line in x:
        if line.startswith("CPSC 1") or line.startswith("CPSC 2") or line.startswith("CPSC 3") or line.startswith("CPSC 4") or line.startswith("CPSC 5") or line.startswith("CPSC 6") or line.startswith("CYBR 1") or line.startswith("CYBR 2") or line.startswith("CYBR 3") or line.startswith("CYBR 4"):
            line = line[0:10].strip("\n")
            DatabaseDict[line] = {}
            if line == "CPSC 4000":
                DatabaseDict[line]["Name"] = line
                DatabaseDict[line]["Credits"] = 0.0
            else:
                DatabaseDict[line]["Name"] = line
                DatabaseDict[line]["Credits"] = 3.0

def getDatabase(courseName):
    return DatabaseDict[courseName]