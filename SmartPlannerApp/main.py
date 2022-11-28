import Analyzer
import Compiler
import Database
import Extractor
import userInterface
import InferenceEngine
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

	stdInterest = []

	for key, value in generalElectives.items():
		stdInterest.append(key[0:4])
		stdInterest = list(set(stdInterest))
	
	scheduleList, inputDict = Analyzer.analyzeData(stdInterest, generalElectives, cpscElectives, classList, db)

	Compiler.compileData(scheduleList, inputDict, name, stdID, crHrs)
	

if __name__ == "__main__":
	main()
	
	#cProfile.run('main()')



