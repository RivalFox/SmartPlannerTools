import argparse
import os
from pathlib import Path
from stat import FILE_ATTRIBUTE_INTEGRITY_STREAM

cpath = ""
inputFile = ""
prereqFile = ""

def parse(path):
    global inputFile, prereqFile, cpath

    path = Path(path)

    if path.exists() == False:
        print("The directory does not exist")
        exit()
    else:
        print("The directory does exist")
        cpath = path

    for file in os.listdir(cpath):
        if "Input" in file:
            inputFile = file
        if "Prerequisite" in file:
            prereqFile = file

def getInput():
    return inputFile

def getPrereq():
    return prereqFile

def getPath():
    return cpath
