import os
import pickle
import sys


def getDatabase():

    if os.path.isfile('.\Database\database.pkl') == False:
        print("##########################################################################################################")
        print("database.pkl is missing from Database folder, run WebExtraction.py to generate database.pk")
        print("Webextraction.py is located in " + os.path.abspath(__file__).strip("Database.py") + "Database")
        print("##########################################################################################################")
        sys.exit()
    
    with open('.\Database\database.pkl', 'rb') as f:
        database = pickle.load(f)

    return database