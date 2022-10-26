import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer

DatabaseDict = {}
SwitchPrereqDict = {
				"Prerequisite(s):" : True,
				"Repeatability:" : False,
				"Restriction(s):" : False,
			 }

SwitchLoopDict = {
				"Home" : True,
				"Columbus State University" : False,
			 }
i = 0

def extractHTML():
	global DatabaseDict 
	#'''
	links = ["https://catalog.columbusstate.edu/course-descriptions/acct/", 
		  "https://catalog.columbusstate.edu/course-descriptions/anth/", 
		  "https://catalog.columbusstate.edu/course-descriptions/arab/", 
		  "https://catalog.columbusstate.edu/course-descriptions/arth/",
		  "https://catalog.columbusstate.edu/course-descriptions/arts/",
		  "https://catalog.columbusstate.edu/course-descriptions/astr/",
		  "https://catalog.columbusstate.edu/course-descriptions/atsc/",
		  "https://catalog.columbusstate.edu/course-descriptions/biol/",
		  "https://catalog.columbusstate.edu/course-descriptions/busa/",
		  "https://catalog.columbusstate.edu/course-descriptions/chem/",
		  "https://catalog.columbusstate.edu/course-descriptions/chin/",
		  "https://catalog.columbusstate.edu/course-descriptions/cied/",
		  "https://catalog.columbusstate.edu/course-descriptions/coep/",
		  "https://catalog.columbusstate.edu/course-descriptions/comm/",
		  "https://catalog.columbusstate.edu/course-descriptions/coun/",
		  "https://catalog.columbusstate.edu/course-descriptions/cpsc/",
		  "https://catalog.columbusstate.edu/course-descriptions/crju/",
		  "https://catalog.columbusstate.edu/course-descriptions/csci/",
		  "https://catalog.columbusstate.edu/course-descriptions/csmt/",
		  "https://catalog.columbusstate.edu/course-descriptions/csus/",
		  "https://catalog.columbusstate.edu/course-descriptions/cybr/",
		  "https://catalog.columbusstate.edu/course-descriptions/cynx/",
		  "https://catalog.columbusstate.edu/course-descriptions/danc/",
		  "https://catalog.columbusstate.edu/course-descriptions/data/",
		  "https://catalog.columbusstate.edu/course-descriptions/dsci/",
		  "https://catalog.columbusstate.edu/course-descriptions/econ/",
		  "https://catalog.columbusstate.edu/course-descriptions/edat/",
		  "https://catalog.columbusstate.edu/course-descriptions/edhe/",
		  "https://catalog.columbusstate.edu/course-descriptions/edma/",
		  "https://catalog.columbusstate.edu/course-descriptions/edms/",
		  "https://catalog.columbusstate.edu/course-descriptions/edmt/",
		  "https://catalog.columbusstate.edu/course-descriptions/edsc/",
		  "https://catalog.columbusstate.edu/course-descriptions/edse/",
		  "https://catalog.columbusstate.edu/course-descriptions/edsi/",
		  "https://catalog.columbusstate.edu/course-descriptions/edtl/",
		  "https://catalog.columbusstate.edu/course-descriptions/educ/",
		  "https://catalog.columbusstate.edu/course-descriptions/eduf/",
		  "https://catalog.columbusstate.edu/course-descriptions/edul/",
		  "https://catalog.columbusstate.edu/course-descriptions/edut/",
		  "https://catalog.columbusstate.edu/course-descriptions/engl/",
		  "https://catalog.columbusstate.edu/course-descriptions/engr/",
		  "https://catalog.columbusstate.edu/course-descriptions/envs/",
		  "https://catalog.columbusstate.edu/course-descriptions/euro/",
		  "https://catalog.columbusstate.edu/course-descriptions/exsc/",
		  "https://catalog.columbusstate.edu/course-descriptions/finc/",
		  "https://catalog.columbusstate.edu/course-descriptions/fren/",
		  "https://catalog.columbusstate.edu/course-descriptions/fyrs/",
		  "https://catalog.columbusstate.edu/course-descriptions/geog/",
		  "https://catalog.columbusstate.edu/course-descriptions/geol/",
		  "https://catalog.columbusstate.edu/course-descriptions/germ/",
		  "https://catalog.columbusstate.edu/course-descriptions/grek/",
		  "https://catalog.columbusstate.edu/course-descriptions/hcmg/",
		  "https://catalog.columbusstate.edu/course-descriptions/hesc/",
		  "https://catalog.columbusstate.edu/course-descriptions/hist/",
		  "https://catalog.columbusstate.edu/course-descriptions/hons/",
		  "https://catalog.columbusstate.edu/course-descriptions/ints/",
		  "https://catalog.columbusstate.edu/course-descriptions/isci/",
		  "https://catalog.columbusstate.edu/course-descriptions/ital/",
		  "https://catalog.columbusstate.edu/course-descriptions/itds/",
		  "https://catalog.columbusstate.edu/course-descriptions/itrn/",
		  "https://catalog.columbusstate.edu/course-descriptions/jadm/",
		  "https://catalog.columbusstate.edu/course-descriptions/japn/",
		  "https://catalog.columbusstate.edu/course-descriptions/kins/",
		  "https://catalog.columbusstate.edu/course-descriptions/latn/",
		  "https://catalog.columbusstate.edu/course-descriptions/lead/",
		  "https://catalog.columbusstate.edu/course-descriptions/libr/",
		  "https://catalog.columbusstate.edu/course-descriptions/maed/",
		  "https://catalog.columbusstate.edu/course-descriptions/math/",
		  "https://catalog.columbusstate.edu/course-descriptions/mgmt/",
		  "https://catalog.columbusstate.edu/course-descriptions/mism/",
		  "https://catalog.columbusstate.edu/course-descriptions/mktg/",
		  "https://catalog.columbusstate.edu/course-descriptions/mpac/",
		  "https://catalog.columbusstate.edu/course-descriptions/mpag/",
		  "https://catalog.columbusstate.edu/course-descriptions/mpah/",
		  "https://catalog.columbusstate.edu/course-descriptions/mpaj/",
		  "https://catalog.columbusstate.edu/course-descriptions/mpsa/",
		  "https://catalog.columbusstate.edu/course-descriptions/msal/",
		  "https://catalog.columbusstate.edu/course-descriptions/mshr/",
		  "https://catalog.columbusstate.edu/course-descriptions/msol/",
		  "https://catalog.columbusstate.edu/course-descriptions/mssl/",
		  "https://catalog.columbusstate.edu/course-descriptions/musc/",
		  "https://catalog.columbusstate.edu/course-descriptions/musa/",
		  "https://catalog.columbusstate.edu/course-descriptions/muse/",
		  "https://catalog.columbusstate.edu/course-descriptions/musp/",
		  "https://catalog.columbusstate.edu/course-descriptions/nurs/",
		  "https://catalog.columbusstate.edu/course-descriptions/ontl/",
		  "https://catalog.columbusstate.edu/course-descriptions/peds/",
		  "https://catalog.columbusstate.edu/course-descriptions/pers/",
		  "https://catalog.columbusstate.edu/course-descriptions/phed/",
		  "https://catalog.columbusstate.edu/course-descriptions/phil/",
		  "https://catalog.columbusstate.edu/course-descriptions/phys/",
		  "https://catalog.columbusstate.edu/course-descriptions/pols/",
		  "https://catalog.columbusstate.edu/course-descriptions/port/",
		  "https://catalog.columbusstate.edu/course-descriptions/psyc/",
		  "https://catalog.columbusstate.edu/course-descriptions/read/",
		  "https://catalog.columbusstate.edu/course-descriptions/soci/",
		  "https://catalog.columbusstate.edu/course-descriptions/span/",
		  "https://catalog.columbusstate.edu/course-descriptions/sped/",
		  "https://catalog.columbusstate.edu/course-descriptions/stat/",
		  "https://catalog.columbusstate.edu/course-descriptions/swah/",
		  "https://catalog.columbusstate.edu/course-descriptions/thea/",
		  "https://catalog.columbusstate.edu/course-descriptions/univ/",
		  "https://catalog.columbusstate.edu/course-descriptions/utch/",
		  "https://catalog.columbusstate.edu/course-descriptions/wbit/",
		  "https://catalog.columbusstate.edu/course-descriptions/arte/",
		  "https://catalog.columbusstate.edu/course-descriptions/edci/",
		  "https://catalog.columbusstate.edu/course-descriptions/edmg/",
		  "https://catalog.columbusstate.edu/course-descriptions/edrg/",
		  "https://catalog.columbusstate.edu/course-descriptions/elem/",
		  "https://catalog.columbusstate.edu/course-descriptions/fta/",
		  "https://catalog.columbusstate.edu/course-descriptions/gfa/",
		  "https://catalog.columbusstate.edu/course-descriptions/mba/",
		  "https://catalog.columbusstate.edu/course-descriptions/mph/",
		  "https://catalog.columbusstate.edu/course-descriptions/wmba/"]
	#'''

	#links = ["https://catalog.columbusstate.edu/course-descriptions/wbit/"]

	#fta
	#gfa
	#mba
	#mph

	for url in links:
		list = []
		list.clear()
		page = requests.get(url)
		only_course_descriptions = SoupStrainer(['strong', ['a', {'class':'bubblelink code'}]])
		all_course_prereqs = BeautifulSoup(page.content, 'html.parser', parse_only = only_course_descriptions)
		for string in all_course_prereqs.stripped_strings:
			list.append(string)
		tempList = []
		tempList.clear()
		i = 0
		loop = False
		prereq = False
		temp = ""
		tempNew = ""
		print(url)
		for x in range(len(list)):
			string = list[x]
			if loop == True:
				if "\xa0" in string:
					string = string.replace("\xa0", " ")
					string = string + "~"
				#print(string)
				if prereq == True:
					if string[5:8].isdigit() == True:
				#		print("added to list")
						tempList.append(string)
					else:
						if not tempList:
							prereq = False
						else:
							if string.startswith("Restric") or string.startswith("Repeata") or string.startswith("Columbus State University"):
								prereq = prereqMode(string)
							DatabaseDict[temp]["Prerequisite"] = {}
							for l in range(len(tempList)):
				#				print(tempList[l])
				#				print("added to prerequisite")
								addtoPrerequisite(temp, tempList[l])
							if prereq == True:
								tempNew = tempList[-1]
				#				print(tempNew)
				#				print("added to name 2")
								temp = addtoName(tempNew, tempNew)
				#				print("added to description 2")
								addtoDescription(tempNew, string)
								tempList = tempList[:-1]
								i = 2
							prereq = False
							tempList.clear()
				elif i == 0 and DatabaseDict.get(string) == None and string[-1] != "~" and string[5:8].isdigit() == True:
				#	print("added to name")
					temp = addtoName(string, string)
					i = 1
				elif i == 1 and DatabaseDict.get(string) == None and string[-1] != "~":
				#	print("added to description")
					addtoDescription(temp, string)
					i = 2
				elif i == 2 and DatabaseDict.get(string) == None and string[-1] != "~":	
				#	print("added to credit")
					addtoCredit(temp, string)
					i = 0
				else:
					prereq = prereqMode(string)
					if string.startswith("Columbus State University"):
						loop = loopChange(string)
				#	elif string.startswith("Prereq"):
				#		print("Prereq Mode")
				#	else:
				#		print("removed")
					tempList.clear()
					continue
			else:
				loop = loopChange(string)
				tempList.clear()
				continue

	with open('.\Input\saved_dictionary.pkl', 'wb') as f:
		pickle.dump(DatabaseDict, f)


	#for key, values in DatabaseDict.items():
	#	print(key, ":", values)

def prereqMode(string):
	return SwitchPrereqDict.get(string, False)

def loopChange(string):
	return SwitchLoopDict.get(string, False)

'''
def check(num, string):
	if num == 0 and DatabaseDict.get(string) == None and string[-1] != "~" and string[5:9].isdigit() == True:
		return True
	elif num == 1 and DatabaseDict.get(string) == None and string[-1] != "~":
		return True
	elif num == 2 and DatabaseDict.get(string) == None and string[-1] != "~":
		return True
	else:
		return False
'''
def addtoName(key, string):
	DatabaseDict[key] = {}
	DatabaseDict[key]["Name"] = string
	return string

def addtoDescription(key, string):
	DatabaseDict[key]["Description"] = string

def addtoCredit(key, string):
	string = string.strip("(,)")		
	DatabaseDict[key]["Credits"] = string[-1]

def addtoPrerequisite(key, string):
	DatabaseDict[key]["Prerequisite"][string.replace("~", "")] = ""

def getDictionary():
	return DatabaseDict
