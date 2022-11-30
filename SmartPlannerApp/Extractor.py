#To open folder in the system
from distutils.text_file import TextFile
import os
#To read a pdf input file
import PyPDF2

def extractData(path):	
	extractedInput =[]         
	#Open file and read file
	inputFile = open(os.path.join(os.path.split(path)[0], os.path.split(path)[1]), "rb")	
	reader = PyPDF2.PdfFileReader(inputFile)
	#using a for loop go through all the pages in pdf file
	for i in range(len(reader.pages)):
		page1 = reader.getPage(i)                
		pdfData = page1.extractText()         
		extractedInput.append(pdfData)
		contents = '\n'.join(extractedInput)
	#The extracted data should be saved in text file
	txtFile = open(os.path.join(".\Input","inputText.txt"), "w", encoding = 'utf-8')	
	txtFile.writelines(contents)
	txtFile.close()
	inputFile.close()

	return createList(".\Input","inputText.txt")


def createList(path, filename):
	classList = []
	classes = []
	inputFile = open(os.path.join(path, filename))
	phrase = "Needed"
	for line in inputFile:
		#Finds the line that contains the phrase "Needed"
		if line.find(phrase) != -1: 
			#Once found, moves onto the next line
			nextLine = next(inputFile)

			for word in nextLine.split():

				if word.isupper() and len(word) == 4:

					for num in nextLine.split():
						if num[0].isdigit() and len(num) > 3:
							classes.append(word + " " + num[:4])

	inputFile.close()

	classList.append(classes)

	return classList