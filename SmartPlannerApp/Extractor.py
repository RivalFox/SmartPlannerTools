#To open folder in the system
import os
#To read a pdf input file
import PyPDF2
#To save the prerequisite info
import networkx as nx

inputList= []

#Hard coded prerequisite information
graph = nx.DiGraph()
graph.add_edges_from([("MATH 1113","MATH 2125"),("CPSC 1301K","CPSC 1302"),("CPSC 1301K","CYBR 2159"),("CPSC 1301K","CYBR 2106"),("CPSC 1301K","CPSC 2105"),
					  ("MATH 2125","MATH 5125"),("MATH 2125","CPSC 2108"), ("CPSC 1302","CPSC 2108"),("CPSC 1302","CPSC 3131"),("CYBR 2159","CPSC 5157"),("CPSC 2105","CPSC 3121"),("CPSC 2105","CPSC 3125"),
					  ("MATH 5125","CPSC 5115"),("CPSC 2108","CPSC 5115"), ("CPSC 2108","CPSC 3175"),("CPSC 2108","CPSC 3125"),("CPSC 2108","CPSC 5175"),("CPSC 3121","CPSC 5155"),
					  ("CPSC 3175","CPSC 5135"),("CPSC 3175","CPSC 4175"),
					  ("CPSC 5115","CPSC 5128"),("CPSC 4175","CPSC 4176")])

class MainExtractor():

	def extractData(self, path, input, prereq):
		extractedData = ""
		extractedGData = ""
		#Sample Input            
		#Open file and read file
		inputFile = open(os.path.join(path, input), "rb")
		reader = PyPDF2.PdfFileReader(inputFile)
		#using a for loop go through all the pages in pdf file
		for i in range(len(reader.pages)):
			page1 = reader.getPage(i)                
			pdfData = page1.extractText()         
			extractedData += pdfData
			print(pdfData)
		#The extracted data should be saved in text file
		txtFile = open(os.path.join(path,"inputText.txt"), "w")
		txtFile.writelines(extractedData)
		txtFile.close

		#Save the prerequisite information in topological order in text file
		txtFile = open(os.path.join(path,"prerequisiteInfo.txt"), "w")
		txtFile.writelines(str(list(nx.topological_sort(graph))))
		txtFile.close
		#DAG graph            
		#Open file and read file
		#prereqFile = open(os.path.join(path, prereq), "rb")
		#reader = PyPDF2.PdfFileReader(prereqFile)
		#using a for loop go through all the pages in pdf file
		#for i in range(len(reader.pages)):
		#    page2 = reader.getPage(i)                
		#    pdfGData = page2.extractText()               
		#    extractedGData += pdfGData               
		#    print(pdfGData)
		#The extracted data should be saved in text file
		#txtGFile = open(os.path.join(path,"DAG.txt"), "w")
		#txtGFile.writelines(extractedGData)
		#txtGFile.close