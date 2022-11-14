from Analyzer import analyzeData, getInputDict, getScheduleList
from Compiler import compileData
from Extractor import extractData, getInputFileName
from ArgumentParser import argParser, getPath, getInput, getPathName
from Database import setDatabase, getDatabase
from WebExtraction import extractHTML, getDictionary
import pickle

def main():

	# Accepts the path of the input folder 
	cpscList = {}
	argParser()
	extractData(getPath(), getInput())
	#extractHTML()
	#setDatabase(getDictionary())

	with open('.\Input\saved_dictionary.pkl', 'rb') as f:
		Database = pickle.load(f)

	#setDatabase(getDictionary())
	setDatabase(Database)

	analyzeData(getPathName(), getInputFileName(), getDatabase())
	compileData(getScheduleList(), getInputDict())

if __name__ == "__main__":
	main()



