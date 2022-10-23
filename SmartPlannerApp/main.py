from Analyzer import analyzeData, getInputDatabase
from Compiler import compileData
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
	analyzeData(getPathName(), getInputFileName(), getDatabase())
	compileData(getInputDatabase())

if __name__ == "__main__":
	main()



