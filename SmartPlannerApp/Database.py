import os
import pickle

DatabaseDict = {}

def setDatabase(dictionary):
    global DatabaseDict
    DatabaseDict = dictionary
            

def getDatabase():
    return DatabaseDict
