from Analyzer import analyzeData
#from Compiler import compileData
from Extractor import extractData, getInputFileName
from ArgumentParser import argParser, getPath, getInput, getPathName
from Database import setDatabase, getDatabase
from WebExtraction import extractHTML, getDictionary
import sys
import os
import re

def main():

	# Accepts the path of the input folder 
	cpscList = {}
	argParser()
	extractData(getPath(), getInput())
	extractHTML()
	setDatabase(getDictionary())
	for key, value in getDatabase().items():
		print(key, ':', value)

	analyzeData(getPathName(), getInputFileName(), getDatabase())
	#compileData(getPathName(), getClassSchedule())

if __name__ == "__main__":
	main()



