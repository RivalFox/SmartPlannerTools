from Analyzer import analyzeData, getInputDatabase
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

	#with open('.\Input\saved_dictionary.pkl', 'rb') as f:
	#	Database = pickle.load(f)
	#setDatabase(Database)

	extractHTML()
	setDatabase(getDictionary())
	analyzeData(getPathName(), getInputFileName(), getDatabase())
	compileData(getInputDatabase())

if __name__ == "__main__":
	main()



