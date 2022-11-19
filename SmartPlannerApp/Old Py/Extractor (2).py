#To open folder in the system
from distutils.text_file import TextFile
import os
#To read a pdf input file
import PyPDF2

def extractData(path):
	extractedInput =[]
	#Sample Input            
	#Open file and read file
	inputFile = open(os.path.join(os.path.split(path)[0], os.path.split(path)[1]), "rb")
	#inputFile = open(os.path.join(path, input), "rb")
	reader = PyPDF2.PdfFileReader(inputFile)
	#using a for loop go through all the pages in pdf file
	for i in range(len(reader.pages)):
		page1 = reader.getPage(i)                
		pdfData = page1.extractText()         
		extractedInput.append(pdfData)
		#print(pdfData)
	#The extracted data should be saved in text file
	txtFile = open(os.path.join(".\Input","inputText.txt"), "w", encoding = 'utf-8')
	contents = '\n'.join(extractedInput)
	txtFile.writelines(contents)
	txtFile.close

def getInputFileName():
	return "inputText.txt"