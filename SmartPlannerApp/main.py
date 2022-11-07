from Analyzer import analyzeData, getInputDict, getScheduleList
from Compiler import compileData
from Extractor import extractData, getInputFileName
from ArgumentParser import argParser, getPath, getInput, getPathName
from Database import setDatabase, getDatabase
from WebExtraction import extractHTML, getDictionary
import sys
import os
import re
import pickle

def main():

	# Accepts the path of the input folder 
	cpscList = {}
	argParser()
	extractData(getPath(), getInput())

	with open('.\Input\saved_dictionary.pkl', 'rb') as f:
		Database = pickle.load(f)
	setDatabase(Database)

	list = ["FINC", "CPSC", "GEOL"]
	for key, value in Database.items():
		if key[0:4] in list:
			print(key, ":", value)



	#extractHTML()
	#setDatabase(getDictionary())
	analyzeData(getPathName(), getInputFileName(), getDatabase())
	compileData(getScheduleList(), getInputDict())

if __name__ == "__main__":
	main()



