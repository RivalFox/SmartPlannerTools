from Analyzer import analyzeData, getInputDict, getScheduleList
from Compiler import compileData
from Database import setDatabase, getDatabase
from Extractor import extractData, getClassList
from userInterface import GUI, getStdName, getStdID, getCrHrs, getChoiceList, getInputFile
import os

def main():
	GUI()
	setDatabase()

	extractData(getInputFile())

	analyzeData(getClassList(), getDatabase())

	compileData(getScheduleList(), getInputDict(), getStdName(), getStdID(), getCrHrs())

if __name__ == "__main__":
	main()



