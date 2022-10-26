#To open folder in the system
from distutils.text_file import TextFile
import os
#To read a pdf input file
import PyPDF2
#To save the prerequisite info
import networkx as nx

def extractData(path, input):
	extractedInput =[]
	#Sample Input            
	#Open file and read file
	inputFile = open(os.path.join(path, input), "rb")
	reader = PyPDF2.PdfFileReader(inputFile)
	#using a for loop go through all the pages in pdf file
	for i in range(len(reader.pages)):
		page1 = reader.getPage(i)                
		pdfData = page1.extractText()         
		extractedInput.append(pdfData)
		#print(pdfData)
	#The extracted data should be saved in text file
	txtFile = open(os.path.join(path,"inputText.txt"), "w", encoding = 'utf-8')
	contents = '\n'.join(extractedInput)
	txtFile.writelines(contents)
	txtFile.close


def getInputFileName():
	return "inputText.txt"