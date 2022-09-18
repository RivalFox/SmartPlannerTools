#To read a pdf input file
import PyPDF2
#To open folder in the system
import os
from pathlib import Path

inputList= []

def extractData(path, input, prereq):
    extractedData = ""
    extractedGData = ""

    inputFile = open(os.path.join(path, input), "rb")
    reader = PyPDF2.PdfFileReader(inputFile)
    #using a for loop go through all the pages in pdf file
    for i in range(len(reader.pages)):
        page1 = reader.getPage(i)                
        pdfData=page1.extractText()         
        extractedData+=pdfData
        print(pdfData)
        #The extracted data should be saved in text file
    txtFile = open(os.path.join(path,"inputText.txt"), "w")
    txtFile.writelines(extractedData)
    txtFile.close
        
    #DAG graph            
    #Open file and read file
    prereqFile = open(os.path.join(path, prereq), "rb")
    reader = PyPDF2.PdfFileReader(prereqFile)
    #using a for loop go through all the pages in pdf file
    for i in range(len(reader.pages)):
        page2 = reader.getPage(i)                
        pdfGData=page2.extractText()               
        extractedGData+=pdfGData               
        print(pdfGData)
            #The extracted data should be saved in text file
    txtGFile = open(os.path.join(path,"DAG.txt"), "w")
    txtGFile.writelines(extractedGData)
    txtGFile.close
