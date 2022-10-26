import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer

# Requests lib
print("Requests")
page = requests.get("https://catalog.columbusstate.edu/course-descriptions/cpsc/")
print("Request Status Code(2 ... is good // 4 ... or 5 ... bad):", page.status_code)

DatabaseDict = {}
i = 0

def CourseDescrptions():
	#Course descriptions and Prerequesites
	#only_course_descriptions = SoupStrainer('strong')
	#only_course_descriptions = SoupStrainer(['strong', {'class':'bubblelink code'}])
	#all_course_prereqs = BeautifulSoup(page.content, 'html.parser', parse_only=only_course_descriptions)

	#printing all of the contents of the course descriptions\
	#list = []
	#for string in all_course_prereqs.stripped_strings:
	#	list.append(string)

	#for x in range(len(list)):
	#	print(list[x])



	only_course_descriptions = SoupStrainer(['strong', ['a', {'class':'bubblelink code'}]])
	
	#only_course_descriptions = SoupStrainer('a', {'class':'bubblelink code'})
	all_course_prereqs = BeautifulSoup(page.content, 'html.parser', parse_only = only_course_descriptions)
	list = []
	for string in all_course_prereqs.stripped_strings:
		#if string.startswith("Prereq") or string.startswith("Repeat") or string.startswith("Restric"):
		#	string += "~"
		list.append(string)
		#print(string)

	tempList = []
	i = 0
	loops = False
	temp = ""
	prereq = False
	tempNew = ""
	for x in range(len(list)):
		if loops == True:
			string = list[x]
			string = string.replace("\xa0", " ")
			if string.startswith("Columbus"):
				print(string)
				print("Removed Columbus")
				loops = False
			elif string.startswith("Repeat") or string.startswith("Restric"):
				print(string)
				print("Removed Repeat or Restrict")
				prereq = False
				continue
			elif string.startswith("Prereq") or prereq == True:
				#print(string)
				if string.startswith("Prereq"):
					print("Prereq Mode")
					prereq = True
				elif string[5:9].isdigit() == True:
					tempList.append(string)
				else:
					tempNew = tempList[-1]
					tempList = tempList[:-1]
					DatabaseDict[temp]["Prerequisite"] = {}
					for l in range(len(tempList)):
						print(tempList[l])
						print("added to prereq                  ", temp)
						DatabaseDict[temp]["Prerequisite"][tempList[l]] = ""
						print(DatabaseDict[temp])
						prereq = False
					print(tempNew)
					print("Added to name                  ", tempNew)
					DatabaseDict[tempNew] = {}
					DatabaseDict[tempNew]["Name"] = tempList[-1]
					print(string)
					print("Added to desc                  ", tempNew)
					DatabaseDict[tempNew]["Description"] = string
					i = 2
					tempList.clear()
					temp = tempNew
			elif i == 0 and DatabaseDict.get(string) == None and string[5:9].isdigit() == True:
				print(string)
				print("Added to name                  ", string)
				DatabaseDict[string] = {}
				DatabaseDict[string]["Name"] = string
				temp = string
				i = i + 1
			elif i == 1:
				print(string)
				print("Added to desc                  ", temp)
				DatabaseDict[temp]["Description"] = string
				i = i + 1
			elif i == 2:
				print(string)
				print("Added to credit                  ", temp)
				string = string.strip("(,)")		
				DatabaseDict[temp]["Credits"] = string[-1]		
				i = 0
			else: 
				print(string)
				print("Removed")
				continue
		if list[x] == "Home":
			temp = "Home"
		elif temp == "Home":
			temp = ""
			loops = True


	for key, values in DatabaseDict.items():
		print(key, ":", values)

	#i = 0
	#for x in range(len(list)):
	#	if i == 0:
	#		DatabaseDict[list[x]] = {}
	#		DatabaseDict[list[x]]["Name"] = list[x]
	#		temp = list[x]
	#		i = i + 1
	#	elif i == 1:
	#		DatabaseDict[temp]["Description"] = list[x]
	#		i = i + 1
	#	else:
	#		string = string.strip("(,)")		
	#		DatabaseDict[temp]["Credits"] = str(list[x])[-1]		
	#		i = 0




CourseDescrptions()
