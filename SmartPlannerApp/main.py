import Analyzer
import Compiler
import Database
import Extractor
import userInterface
import InferenceEngine
import sys
#import cProfile

def main():

	name, stdID, crHrs, choice1, choice2, choice3, inputFile = userInterface.GUI()

	stdInterest = []
	stdInterest.append(choice1)
	stdInterest.append(choice2)
	stdInterest.append(choice3)

	db = Database.getDatabase()

	classList = Extractor.extractData(inputFile)

	generalElectives, cpscElectives = InferenceEngine.InferenceEngine(stdInterest, db)
	
	scheduleList, inputDict, scheduleWeights = Analyzer.analyzeData(stdInterest, generalElectives, cpscElectives, classList, db)

	Compiler.compileData(scheduleList, inputDict, name, stdID, crHrs, scheduleWeights)

	sys.exit()
	

if __name__ == "__main__":
	main()
	
	#cProfile.run('main()')



