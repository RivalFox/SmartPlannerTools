from Analyzer import analyzeData, getClassSchedule
from Compiler import compileData
from Extractor import extractData, getFileName, getCPSCName, getCYBRName
from ArgumentParser import argParser, getPath, getInput, getPathName, getCPSC, getCYBR
from Database import setDatabase, getDatabase
import sys
import os
import re

def main():

	# Accepts the path of the input folder 
	cpscList = {}
	argParser()
	extractData(getPath(), getInput(), getCPSC(), getCYBR())
	setDatabase(getPath(), getCPSCName())
	setDatabase(getPathName(), getCYBRName())
	print(getDatabase("CPSC 4000"))
	print(getDatabase("CPSC 1302"))
	print(getDatabase("CPSC 6190"))
	print(getDatabase("CYBR 4416"))
	print(getDatabase("CPSC 1301K"))

	analyzeData(getPathName(), getFileName())
	compileData(getPathName(), getClassSchedule())

if __name__ == "__main__":
	main()



