import os

DatabaseDict = {}

def setDatabase(dictionary):
    global DatabaseDict
    DatabaseDict = dictionary
            

def getDatabase():
    #for key, value in DatabaseDict.items():
    #    print(key, ':', value)
    return DatabaseDict
