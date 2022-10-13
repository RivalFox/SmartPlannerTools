def analyzeData(path, filename):
    # Open and Read File
    filename = "modifiedInputText.txt"
    inputFile = open(path + "\\" + filename)

    # Initialize an empty list
    classList = []
   
    for line in inputFile:
        line = line.replace(".", "")
        line = line.replace('\n', "")
        line = line.replace(" ", "")

        lineList = (line.split(","))
        classList.append(lineList)
    inputFile.close()
    
    #print(classList)
    topologicalSort(path, classList)
    
    # Check if a subject is a prerequisite of other subject
def checkPrereq(subject, new, target):
    # Find Target Subject
    prereqList = []
    foundNew = False
    foundTarget = False
    
    for prereq in subject:
        if(prereq[0] == target):
            prereqList = prereq
            if(new in prereqList):
                foundNew = True
        if(prereq[0] == new):
            prereqList = prereq
            if(target in prereqList):
                foundTarget = True
                
    # Check if new is in the prerequisite list of target
    return foundNew and foundTarget

def topologicalSort(path, subject):
    
    # Init a copy of Subject List and an empty list to contain results
    copySubject = subject
    result = []
    className = ""
    
    # Iterate until the subject list is empty -> no more nodes in graph
    while(len(subject) != 0):
        # Find subject without any input edges
        for subjects in subject:
            
            # Init empty list to contain subjects in each semester
            semesterList = []
            
            # Get the subjects if the length of the list is 1 -> In-Degree = 0
            if(len(subjects) == 1):
                className = subjects[0]
                semesterList.append(className)
                
                # Remove the subject from current list
                subject.remove(subjects) 
                
                # Append the subject to corresponding semester
                for rest in subject:
                    if(len(rest) == 1 and not checkPrereq(copySubject, rest[0], className)):
                        className = rest[0]
                        semesterList.append(className)
                        
                        # Remove the subject from current list
                        subject.remove(rest)
                        
                # Add each semester to the end result
                result.append(semesterList)
            
            # Remove the subject from remaining list (graph nodes connected with the subject)
            for choosen in semesterList:
                for remaining in subject:
                    if(choosen in remaining):
                        remaining.remove(choosen)                
                    
        #print(subject)
    schedule(path, result)

def schedule(path, sortedResult):
    # Init counter
    with open(".\\" + path + "\\classSchedule.txt", "w") as f:
    # Iterate over result
        for semester in sortedResult:
            for idx in range(len(semester)):
                if(idx == len(semester) - 1):
                    f.writelines(semester[idx] + '\n')
                    #print(semester[idx])
                else:
                    f.writelines(semester[idx] + '\n')
                    #print(semester[idx])
    f.close()

def getClassSchedule():
    return "classSchedule.txt"