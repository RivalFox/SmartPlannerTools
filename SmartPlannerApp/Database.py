import os
import pickle

DatabaseDict = {}

def setDatabase():
    global DatabaseDict
    
    with open('.\Database\saved_dictionary.pkl', 'rb') as f:
        Database = pickle.load(f)

    DatabaseDict = Database
            
def getDatabase():
    return DatabaseDict