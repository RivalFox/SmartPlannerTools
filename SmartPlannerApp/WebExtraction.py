from sqlite3 import enable_shared_cache
import sys
import requests
from bs4 import BeautifulSoup, SoupStrainer
import time

# *** packages ***
# beautifulsoup4
# requests
# html5lib

DatabaseDict = {}
i = 0

def extractHTML():
	global DatabaseDict, i
	# Webscrapping
	# Requests lib
	#print("Requests")
	links = ["https://catalog.columbusstate.edu/course-descriptions/cpsc/", "https://catalog.columbusstate.edu/course-descriptions/cybr/", "https://catalog.columbusstate.edu/course-descriptions/math/", "https://catalog.columbusstate.edu/course-descriptions/pols/", "https://catalog.columbusstate.edu/course-descriptions/dsci/", "https://catalog.columbusstate.edu/course-descriptions/stat/"]
	for url in links:
		page = requests.get(url)
		only_course_headers = SoupStrainer("div", {'class':'cols noindent'})
		all_course_headers = BeautifulSoup(page.content, 'html.parser', parse_only = only_course_headers)
		i = 0
		for string in all_course_headers.stripped_strings:
			if i == 0:
				DatabaseDict[string] = {}
				DatabaseDict[string]["Name"] = string
				temp = string
				i = i + 1
			elif i == 1:
				DatabaseDict[temp]["Description"] = string
				i = i + 1
			else:
				string = string.strip("(,)")		
				DatabaseDict[temp]["Credits"] = string[-1]		
				i = 0

	#page = requests.get("https://catalog.columbusstate.edu/course-descriptions/cpsc/")
	#page = requests.get("https://catalog.columbusstate.edu/course-descriptions/cybr/")
	#print("Request Status Code(2 ... is good // 4 ... or 5 ... bad):", page.status_code)
	

	# Beautiful Soup
	#print("Beautiful Soup")
	#course_blocks = SoupStrainer(class_="courseblocks")
	
	# the entire page
	#all_page = BeautifulSoup(page.content, 'html.parser')
	
	# Course names and credits 
	#only_course_headers = SoupStrainer("div", {'class':'cols noindent'})
	#all_course_headers = BeautifulSoup(page.content, 'html.parser', parse_only = only_course_headers)
	# printing all of the contents of the course headers as a string

	#for key, value in DatabaseDict.items():
	#	print(key, ':', value)

	# Course descriptions and Prerequesites
	#all_course_descriptions = SoupStrainer("div",{'class':'courseblockextra noindent'})
	#all_course_descriptions = BeautifulSoup(page.content, 'html.parser', parse_only = all_course_descriptions)

	# printing all of the contents of the course descriptions
	#for i in all_course_descriptions.stripped_strings:
	#	print(i)
	
def getDictionary():
	return DatabaseDict

#studentCourses = {
#		"1301" : {
#			"name" : "CPSC 1301",
#			"credits" : 3,
#			"timeOfYear" : {
#				"summer" : True,
#				"spring" : True,
#				"fall" : True,		
#			},
#			"courseBefore" : "",
#			"coursesAfter" : {
#				"code" : "2105",
#				"code" : "1302",
#				"code" : "2159",
#				"code" : "2106"
#			}
#		},
#		"1301K" : {
#			"name" : "CPSC 1301K",
#			"credits" : 4,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"coursesAfter" : {
#				"code" : "2105",
#				"code" : "1302",
#				"code" : "2159",
#				"code" : "2106"
#			}
#		},
#		"1302" : {
#			"name" : "CPSC 1302",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "1301",
#			"courseAfter" : "2108"
#		},
#		"2108" : {
#			"name" : "CPSC 2108",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"3131" : {
#			"name" : "CPSC 3131",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"2159" : {
#			"name" : "CPSC 2159",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"5157" : {
#			"name" : "CPSC 5157",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"2106" : {
#			"name" : "CPSC 2106",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"2105" : {
#			"name" : "CPSC 2105",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"3121" : {
#			"name" : "CPSC 3121",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#		"5155" : {
#			"name" : "CPSC 5155",
#			"credits" : 3,
#			"summer" : True,
#			"spring" : True,
#			"fall" : True,
#			"courseBefore" : "",
#			"courseAfter" : ""
#		},
#	}
