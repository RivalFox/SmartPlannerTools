import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer

# Requests lib
print("Requests")
page = requests.get("https://catalog.columbusstate.edu/course-descriptions/cybr/")
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

	i = 0
	loops = False
	temp = ""
	prereq = False
	for x in range(len(list)):
		if loops == True:
			string = list[x]
			string = string.replace("\xa0", " ")
			print(string)
			if string.startswith("Columbus"):
				print("Columbus")
				loops = False
			elif string.startswith("Repeat") or string.startswith("Restric"):
				print("Removed Repeat or Restrict")
				prereq = False
				continue
			elif string.startswith("Prereq") or prereq == True:
				if string.startswith("Prereq"):
					print("Prereq Mode")
					prereq = True
				#elif DatabaseDict.get(string) != None:
				#	print("Added to prereq", temp)
				#	DatabaseDict[temp]["Prerequisite"] = {}
				#	DatabaseDict[temp]["Prerequisite"][string] = ""
				#	print(DatabaseDict[temp])
				elif DatabaseDict.get(string) == None:
					if temp[0:4] == str(string)[0:4]:
						print("Break out of prereq")
						DatabaseDict[string] = {}
						DatabaseDict[string]["Name"] = string
						print("Added to name")
						temp = string
						i = i + 1
						prereq = False
					elif temp[0:4] != string[0:4]:
						print("Added to prereq" , temp)
						DatabaseDict[temp]["Prerequisite"] = {}
						DatabaseDict[temp]["Prerequisite"][string] = ""
						print(DatabaseDict[temp])
						continue
				else:
					print("Added to prereq", temp)
					DatabaseDict[temp]["Prerequisite"] = {}
					DatabaseDict[temp]["Prerequisite"][string] = ""
					print(DatabaseDict[temp])
			elif i == 0 and DatabaseDict.get(string) == None and string != "not":
				print("Added to name")
				DatabaseDict[string] = {}
				DatabaseDict[string]["Name"] = string
				temp = string
				i = i + 1
			elif i == 1:
				print("Added to desc")
				DatabaseDict[temp]["Description"] = string
				i = i + 1
			elif i == 2:
				print("Added to credit")
				string = string.strip("(,)")		
				DatabaseDict[temp]["Credits"] = string[-1]		
				i = 0
			else: 
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
