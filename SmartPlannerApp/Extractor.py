#To open folder in the system
from distutils.text_file import TextFile
import os
#To read a pdf input file
import PyPDF2

classList = []

def extractData(path):
	extractedInput =[]
	#Sample Input            
	#Open file and read file
	inputFile = open(os.path.join(os.path.split(path)[0], os.path.split(path)[1]), "rb")	
	reader = PyPDF2.PdfFileReader(inputFile)
	#using a for loop go through all the pages in pdf file
	for i in range(len(reader.pages)):
		page1 = reader.getPage(i)                
		pdfData = page1.extractText()         
		extractedInput.append(pdfData)
		contents = '\n'.join(extractedInput)
		#print(pdfData)
	#The extracted data should be saved in text file
	txtFile = open(os.path.join(".\Input","inputText.txt"), "w", encoding = 'utf-8')	
	txtFile.writelines(contents)
	txtFile.close()
	inputFile.close()
	createList(".\Input","inputText.txt")


def createList(path, filename):
	inputFile1 = open(os.path.join(path, filename))

	line = ""

	phrase = "Needed"
		#count = 0
	for line in inputFile1:
		#Finds the line that contains the phrase "Needed"
		if line.find(phrase) != -1: 
			#Once found, moves onto the next line
			nextLine = next(inputFile1)

			for word in nextLine.split():

				if word.isupper() and len(word) == 4:
					#print(word)

					for num in nextLine.split():
						if num[0].isdigit() and len(num) > 3:
							#print(word + " " + num[:4])
							classList.append(word + " " + num[:4])
	
	print(classList)
	

	inputFile1.close()

def getClassList():
	return classList