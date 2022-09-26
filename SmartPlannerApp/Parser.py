#import argparse
#import os
#from pathlib import Path
#from stat import FILE_ATTRIBUTE_INTEGRITY_STREAM

import os
from pathlib import Path

path = ""
inputFile = ""
prereqFile = ""


class MainParser():

	def parseData(self, dirPath):
		global inputFile, prereqFile, path
		path = Path(dirPath)

		if path.exists() == False:
			print("The directory does not exist")
			exit()
		else:
			print("The directory does exist")

		for file in os.listdir(path):
			if "Input" in file:
				inputFile = file
			if "Prerequisite" in file:
				prereqFile = file

	def getPath(self):
		   return path
	
	def getInput(self):
		return inputFile

	def getPrereq(self):
		return prereqFile


