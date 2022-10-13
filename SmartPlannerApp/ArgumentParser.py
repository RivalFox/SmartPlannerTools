import argparse
import os
import os.path
from pathlib import Path


path = ""
pathName = ""
inputFile = ""
cpscFile = ""
cybrFile = ""

def argParser():
	arg_parse = argparse.ArgumentParser(description='Folder path location')
	arg_parse.add_argument('path', type = Path, help = 'Path of the folder of files')
	findFiles(arg_parse.parse_args())

def findFiles(dirPath):
	global path, pathName, inputFile, cpscFile, cybrFile
	path = dirPath.path
	pathName = str(path)

	for file in os.listdir(path):
		if "Sample" in file:
			inputFile = file
		if "cpsc.pdf" in file:
			cpscFile = file
		if "cybr.pdf" in file:
			cybrFile = file

def getPath():
	return path

def getPathName():
	return pathName
	
def getInput():
	return inputFile

def getCPSC():
	return cpscFile

def getCYBR():
	return cybrFile
