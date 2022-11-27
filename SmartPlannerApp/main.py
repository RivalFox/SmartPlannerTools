import Analyzer
import Compiler
import Database
import Extractor
import userInterface

def main():

	name, stdID, crHrs, choice1, choice2, choice3, inputFile = userInterface.GUI()

	db = Database.getDatabase()

	classList = Extractor.extractData(inputFile)

	scheduleList, inputDict = Analyzer.analyzeData(classList, db)

	Compiler.compileData(scheduleList, inputDict, name, stdID, crHrs)

if __name__ == "__main__":
	main()



