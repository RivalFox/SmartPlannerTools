import os
import pickle
import sys

DatabaseDict = {}

def setDatabase():
    global DatabaseDict

    if os.path.isfile('.\Database\saved_dictionary.pkl') == False:
        print("##########################################################################################################")
        print("saved_dictionary.pkl is missing from Database folder, run WebExtraction.py to generate saved_dictionary.pk")
        print("##########################################################################################################")
        sys.exit()
    
    with open('.\Database\saved_dictionary.pkl', 'rb') as f:
        Database = pickle.load(f)

    DatabaseDict = Database
            
def getDatabase():
    return DatabaseDict