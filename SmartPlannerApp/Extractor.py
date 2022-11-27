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
		#print(pdfData)
	#The extracted data should be saved in text file
	txtFile = open(os.path.join(".\Input","inputText.txt"), "w", encoding = 'utf-8')	
	txtFile.writelines(contents)
	txtFile.close()
	inputFile.close()

	return createList(".\Input","inputText.txt")


def createList(path, filename):
	classList = []
	classes = []
	classes2 = []
	classes3 = []
	inputFile = open(os.path.join(path, filename))
	phrase = "Needed"
	for line in inputFile:
		#Finds the line that contains the phrase "Needed"
		if line.find(phrase) != -1: 
			#Once found, moves onto the next line
			nextLine = next(inputFile)

			for word in nextLine.split():

				if word.isupper() and len(word) == 4:
					#print(word)

					for num in nextLine.split():
						if num[0].isdigit() and len(num) > 3:
							#print(word + " " + num[:4])
							classes.append(word + " " + num[:4])

	inputFile.close()

	classList.append(classes)

	classes2.append("CPSC 1302")
	classes2.append("CPSC 1301K")
	classes2.append("CPSC 2108")
	classes2.append("CPSC 4115")
	classes2.append("CPSC 4111")
	classes2.append("CPSC 6180")
	classes2.append("CPSC 6185")
	classes2.append("CPSC 6985")
	classes2.append("CYBR 2159")
	classes2.append("CYBR 2160")
	classes2.append("CYBR 3106")
	classes2.append("CYBR 3108")
	classes2.append("CYBR 3115")
	classes2.append("CYBR 3119")

	for t in range(len(classes)):
		classes3.append(classes[t])

	for l in range(len(classes2)):
		classes3.append(classes2[l])

	classList.append(classes2)
	classList.append(classes3)

	return classList